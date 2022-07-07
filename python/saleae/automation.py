from enum import Enum
from os import PathLike
from typing import List, Optional, Union

from dataclasses import dataclass

from saleae.grpc import saleae_pb2
from saleae.grpc import saleae_pb2_grpc
import time

import grpc
import grpc_status.rpc_status

import os
import os.path

import logging
import re

from saleae.grpc.saleae_pb2 import AnalyzerSettingValue, ChannelIdentifier, ErrorCode

logger = logging.getLogger(__name__)

class UnknownError(Exception):
    pass

class InternalServerError(Exception):
    pass

class InvalidRequest(Exception):
    pass

class RadixType(Enum):
    BINARY = 1
    DECIMAL = 2
    HEXADECIMAL = 3
    ASCII = 4


def to_grpc_radix_type(type: RadixType) -> saleae_pb2.RadixType:
    if type == RadixType.BINARY:
        return saleae_pb2.BINARY
    elif type == RadixType.DECIMAL:
        return saleae_pb2.DECIMAL
    elif type == RadixType.HEXADECIMAL:
        return saleae_pb2.HEXADECIMAL
    elif type == RadixType.ASCII:
        return saleae_pb2.ASCII

    raise RuntimeError(f"Unrecognized radix type: {type}")


error_message_re = re.compile(r"^(\d+): (.*)$")

def grpc_error_to_exception(exc: grpc.RpcError):
    if exc.code() == grpc.StatusCode.ABORTED:
        message = exc.details()
        return grpc_error_msg_to_exception(message)
    else:
        return exc

def grpc_error_msg_to_exception(msg: str):
    code_to_exception_type = {
        ErrorCode.INTERNAL_EXCEPTION: InternalServerError,
        ErrorCode.INVALID_REQUEST: InvalidRequest,
    }

    match = error_message_re.match(msg)
    if match is None:
        return UnknownError(msg)
    
    code = int(match.group(1))
    error_msg = match.group(2)

    exc_type = code_to_exception_type.get(code, UnknownError)
    return exc_type(error_msg)


class Manager:
    def __init__(self, port: int):
        """
        """
        self.channel = grpc.insecure_channel(f'127.0.0.1:{port}')
        self.channel.subscribe(lambda value: logger.info(f'sub {value}'))
        self.stub = saleae_pb2_grpc.ManagerStub(self.channel)

    def close(self):
        """
        Close connection to Saleae backend, and shut it down if it was created by Manager.

        """
        self.channel.close()
        self.channel = None
        self.stub = None

    def get_devices(self):
        request = saleae_pb2.GetDevicesRequest()
        reply: saleae_pb2.GetDevicesReply = self.stub.GetDevices(request)

    def load_capture(self, filepath: str) -> 'Capture':
        """
        Load a capture.

        The returned Capture object will be fully loaded (`wait_until_done` not required).

        Raises:
            InvalidFileError

        """
        request = saleae_pb2.LoadCaptureRequest(filepath=filepath)
        reply: saleae_pb2.LoadCaptureReply = self.stub.LoadCapture(request)
        return Capture(self, reply.capture_info.capture_id)




class Capture:
    def __init__(self, manager: Manager, capture_id: int):
        self.manager = manager
        self.capture_id = capture_id

    def add_analyzer(self, name: str, *, label: str, settings: dict[str, Union[str, int, float, bool]]):
        analyzer_settings = {}

        for key, value in settings.items():
            if isinstance(value, str):
                v = AnalyzerSettingValue(string_value=value)
            elif isinstance(value, int):
                v = AnalyzerSettingValue(int64_value=value)
            elif isinstance(value, float):
                v = AnalyzerSettingValue(double_value=value)
            elif isinstance(value, bool):
                v = AnalyzerSettingValue(bool_value=value)
            else:
                raise RuntimeError("Unsupported analyzer setting value type")

            analyzer_settings[key] = v

        request = saleae_pb2.AddAnalyzerRequest(capture_id=self.capture_id, analyzer_name=name, analyzer_label=label, settings=analyzer_settings)

        try:
            reply = self.manager.stub.AddAnalyzer(request)
        except grpc.RpcError as exc:
            raise grpc_error_to_exception(exc) from None

        return AnalyzerHandle(analyzer_id=reply.analyzer_id)

    def remove_analyzer(self, analyzer: 'AnalyzerHandle'):
        request = saleae_pb2.RemoveAnalyzerRequest(capture_id=self.capture_id, analyzer_id=analyzer.analyzer_id)
        self.manager.stub.RemoveAnalyzer(request)

    def save_capture(self, filepath: str):
        request = saleae_pb2.SaveCaptureRequest(filepath=filepath)
        try:
            reply = self.manager.stub.SaveCapture(request)
        except grpc.RpcError as exc:
            raise grpc_error_to_exception(exc) from None

    def export_analyzer_legacy(self, filepath: str, analyzer: 'AnalyzerHandle', radix: 'RadixType'):
        request = saleae_pb2.ExportAnalyzerLegacyRequest(
            capture_id=self.capture_id,
            filepath=filepath,
            analyzer_id=analyzer.analyzer_id,
            radix_type=to_grpc_radix_type(radix)
        )

        try:
            reply = self.manager.stub.ExportAnalyzerLegacy(request)
        except grpc.RpcError as exc:
            raise grpc_error_to_exception(exc) from None

    def export_data_table(self, filepath: str, analyzers: List['AnalyzerHandle']):
        request = saleae_pb2.ExportDataTableRequest(
            capture_id=self.capture_id,
            filepath=filepath,
            analyzer_ids=[h.analyzer_id for h in analyzers])

        try:
            reply = self.manager.stub.ExportDataTable(request)
        except grpc.RpcError as exc:
            raise grpc_error_to_exception(exc) from None

    def export_raw_data_csv(self, directory: str, *, analog_channels: Optional[List[int]] = None,
                            digital_channels: Optional[List[int]] = None,
                            analog_downsample_ratio: int = 1, iso8601: bool = False):
        channels = []
        if analog_channels:
            channels.extend([saleae_pb2.ChannelIdentifier(type=saleae_pb2.ANALOG, index=ch) for ch in analog_channels])
        if digital_channels:
            channels.extend([saleae_pb2.ChannelIdentifier(type=saleae_pb2.DIGITAL, index=ch) for ch in digital_channels])

        request = saleae_pb2.ExportRawDataCsvRequest(
            capture_id=self.capture_id,
            directory=directory,
            channels=channels,
            analog_downsample_ratio=analog_downsample_ratio,
            iso8601=iso8601
        )

        try:
            self.manager.stub.ExportRawDataCsv(request)
        except grpc.RpcError as exc:
            raise grpc_error_to_exception(exc) from None

    def export_raw_data_binary(self, directory: str, *, analog_channels: Optional[List[int]] = None,
                            digital_channels: Optional[List[int]] = None,
                            analog_downsample_ratio: int = 1):
        channels = []
        if analog_channels:
            channels.extend([saleae_pb2.ChannelIdentifier(type=saleae_pb2.ANALOG, index=ch) for ch in analog_channels])
        if digital_channels:
            channels.extend([saleae_pb2.ChannelIdentifier(type=saleae_pb2.DIGITAL, index=ch) for ch in digital_channels])

        request = saleae_pb2.ExportRawDataBinaryRequest(
            capture_id=self.capture_id,
            directory=directory,
            channels=channels,
            analog_downsample_ratio=analog_downsample_ratio,
        )

        try:
            self.manager.stub.ExportRawDataBinary(request)
        except grpc.RpcError as exc:
            raise grpc_error_to_exception(exc) from None

    def close(self):
        request = saleae_pb2.CloseCaptureRequest(capture_id=self.capture_id)
        self.manager.stub.CloseCapture(request)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO)

    manager = Manager(port=50051)
    manager.get_devices()

    captures = []

    #for _ in range(5):
        #for name in ('cap1', 'cap2', 'cap3'):
            #path = os.path.join(os.getcwd(), f'{name}.sal')
            #captures.append(manager.load_capture(path))



    for name in ('cap1',):
        path = os.path.join(os.getcwd(), f'{name}.sal')
        print('loading')
        with manager.load_capture(path) as cap:
            cap.export_raw_data_csv(
                directory=os.path.join(os.getcwd(), f'export_{name}'),
                analog_channels=[0,1,2],
                digital_channels=[0])

    for cap in captures:
        cap.close()

@dataclass
class AnalyzerHandle:
    analyzer_id: int
