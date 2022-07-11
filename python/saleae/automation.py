from contextlib import contextmanager
from typing import List, Optional, Union, Dict
from dataclasses import dataclass, field
from enum import Enum
import grpc
import logging
import re

from saleae.grpc import saleae_pb2, saleae_pb2_grpc


logger = logging.getLogger(__name__)

class SaleaeError(Exception):
    """
    The base class for all Saleae exceptions. Do not catch this directly.
    """
    pass

class UnknownError(SaleaeError):
    """
    This indicates that the error message from the Logic 2 software was not understood by the python library. 
    This could indicate a version mismatch.
    """
    pass

class InternalServerError(SaleaeError):
    """
    An unexpected error occurred in the Logic 2 software. Please submit these errors to Saleae support.
    """
    pass

class InvalidRequestError(SaleaeError):
    """
    The socket request was invalid. See exception message for details.
    """
    pass

class LoadCaptureFailedError(SaleaeError):
    """
    Error loading a saved capture. 
    This could indicate that the file does not exist, or the file was saved with a newer version of the Logic 2 software, or that the file was not a valid saved file. 
    Try manually loading the file in the Logic 2 software for more information.
    """
    pass

class ExportError(SaleaeError):
    """
    An error occurred either while exporting raw data, a single protocol analyzer, or the protocol analyzer data table.
    Check the exception message for more details.
    """
    pass

class MissingDeviceError(SaleaeError):
    """
    The device ID supplied to the start_capture function is not currently attached to the system, or it has not been detected by the software.
    Use the get_devices function to check available devices.
    For general support for device not detected errors, see this support article:
    https://support.saleae.com/troubleshooting/logic-not-detected
    """
    pass

class CaptureError(SaleaeError):
    """
    The base class for all capture related errors. We recommend all automation applications handle this exception type.
    Capture failures occur rarely, and for a handful of reasons. We recommend logging the exception message for later troubleshooting.
    We do not recommend attempting to access or save captures that end in an error. Instead, we recommend starting a new capture.
    Check the exception message for details.
    """
    pass

class DeviceError(CaptureError):
    """
    This error represents any device related error while capturing. USB communication or bandwidth errors, missing calibration, device disconnection while recording, and more.
    Check the exception message for details. 
    """
    pass

class OOMError(CaptureError):
    """
    This exception indicates that the capture was automatically terminated because the capture buffer was filled.
    """
    pass

class RadixType(Enum):
    BINARY = saleae_pb2.RADIX_TYPE_BINARY
    DECIMAL = saleae_pb2.RADIX_TYPE_DECIMAL
    HEXADECIMAL = saleae_pb2.RADIX_TYPE_HEXADECIMAL
    ASCII = saleae_pb2.RADIX_TYPE_ASCII

@contextmanager
def error_handler():
    try:
        yield
    except grpc.RpcError as exc:
        raise grpc_error_to_exception(exc) from None

error_message_re = re.compile(r"^(\d+): (.*)$")

def grpc_error_to_exception(exc: grpc.RpcError):
    if exc.code() == grpc.StatusCode.ABORTED:
        message = exc.details()
        return grpc_error_msg_to_exception(message)
    else:
        return exc

grpc_error_code_to_exception_type = {
    saleae_pb2.ERROR_CODE_UNSPECIFIED: UnknownError,

    saleae_pb2.ERROR_CODE_INTERNAL_EXCEPTION: InternalServerError,
    saleae_pb2.ERROR_CODE_INVALID_REQUEST: InvalidRequestError,

    saleae_pb2.ERROR_CODE_LOAD_CAPTURE_FAILED: LoadCaptureFailedError,
    saleae_pb2.ERROR_CODE_EXPORT_FAILED: ExportError,

    saleae_pb2.ERROR_CODE_MISSING_DEVICE: MissingDeviceError,
    saleae_pb2.ERROR_CODE_DEVICE_ERROR: DeviceError,
    saleae_pb2.ERROR_CODE_OOM: OOMError,
}
def grpc_error_msg_to_exception(msg: str):
    match = error_message_re.match(msg)
    if match is None:
        return UnknownError(msg)
    
    code = int(match.group(1))
    error_msg = match.group(2)

    exc_type = grpc_error_code_to_exception_type.get(code, UnknownError)
    return exc_type(error_msg)


@dataclass
class AnalyzerHandle:
    analyzer_id: int


class DeviceConfiguration:
    pass


@dataclass
class GlitchFilterEntry:
    channel_index: int
    pulse_width_seconds: float


@dataclass
class LogicDeviceConfiguration(DeviceConfiguration):
    enabled_analog_channels: List[int] = field(default_factory=list)
    enabled_digital_channels: List[int] = field(default_factory=list)

    analog_sample_rate: Optional[int] = None
    digital_sample_rate: Optional[int] = None

    digital_threshold_volts: Optional[float] = None

    glitch_filters: List[GlitchFilterEntry] = field(default_factory=list)


class DigitalTriggerType(Enum):
    RISING = saleae_pb2.DIGITAL_TRIGGER_TYPE_RISING
    FALLING = saleae_pb2.DIGITAL_TRIGGER_TYPE_FALLING
    PULSE_HIGH = saleae_pb2.DIGITAL_TRIGGER_TYPE_PULSE_HIGH
    PULSE_LOW = saleae_pb2.DIGITAL_TRIGGER_TYPE_PULSE_LOW


class DigitalTriggerLinkedChannelState(Enum):
    LOW = saleae_pb2.DIGITAL_TRIGGER_LINKED_CHANNEL_STATE_LOW
    HIGH = saleae_pb2.DIGITAL_TRIGGER_LINKED_CHANNEL_STATE_HIGH


@dataclass
class DigitalTriggerLinkedChannel:
    channel_index: int
    state: DigitalTriggerLinkedChannelState


@dataclass
class DigitalTriggerCaptureMode:
    trigger_type: DigitalTriggerType

    trigger_channel_index: int

    min_pulse_width_seconds: Optional[float] = None
    max_pulse_width_seconds: Optional[float] = None

    linked_channels: List[DigitalTriggerLinkedChannel] = field(default_factory=list)

    # Seconds of data at end of capture to keep. If unspecified, all data will be kept.
    trim_data_seconds: Optional[float] = None

    # Seconds of data to record after triggering
    after_trigger_seconds: Optional[float] = None

@dataclass
class TimedCaptureMode:
    # Trigger after X seconds
    duration_seconds: float

    # Seconds of data at end of capture to keep. If unspecified, all data will be kept.
    trim_data_seconds: Optional[float] = None


@dataclass
class ManualCaptureMode:
    """
    When this is used, a capture must be triggered/stopped manually.
    
    """
    # Seconds of data at end of capture to keep. If unspecified, all data will be kept.
    trim_data_seconds: Optional[float] = None


CaptureMode = Union[ManualCaptureMode, TimedCaptureMode, DigitalTriggerCaptureMode]

@dataclass
class CaptureConfiguration:
    # Capture buffer size (in megabytes)
    buffer_size: Optional[int] = None
    capture_mode: CaptureMode = field(default_factory=ManualCaptureMode)


class Manager:
    def __init__(self, port: int):
        """
        """
        self.channel = grpc.insecure_channel(f'127.0.0.1:{port}')
        self.channel.subscribe(lambda value: logger.info(f'sub {value}'))
        self._stub = saleae_pb2_grpc.ManagerStub(self.channel)

    def close(self):
        """
        Close connection to Saleae backend, and shut it down if it was created by Manager.

        """
        self.channel.close()
        self.channel = None
        self._stub = None

    @property
    def stub(self) -> saleae_pb2_grpc.ManagerStub:
        if self._stub is None:
            raise RuntimeError("Cannot use Manager after it has been closed")
        return self._stub

    def get_devices(self):
        request = saleae_pb2.GetDevicesRequest()
        with error_handler():
            reply: saleae_pb2.GetDevicesReply = self.stub.GetDevices(request)

    def start_capture(
        self,
        *,
        device_configuration: DeviceConfiguration,
        device_serial_number: str,
        capture_configuration: Optional[CaptureConfiguration] = None,
    ) -> "Capture":
        request = saleae_pb2.StartCaptureRequest()
        request.device_serial_number = device_serial_number

        if isinstance(device_configuration, LogicDeviceConfiguration):
            request.logic_device_configuration.enabled_analog_channels[
                :
            ] = device_configuration.enabled_analog_channels
            request.logic_device_configuration.enabled_digital_channels[
                :
            ] = device_configuration.enabled_digital_channels
            if device_configuration.analog_sample_rate is not None:
                request.logic_device_configuration.analog_sample_rate = (
                    device_configuration.analog_sample_rate
                )
            if device_configuration.digital_sample_rate is not None:
                request.logic_device_configuration.digital_sample_rate = (
                    device_configuration.digital_sample_rate
                )
            if device_configuration.digital_threshold_volts is not None:
                request.logic_device_configuration.digital_threshold_volts = (
                    device_configuration.digital_threshold_volts
                )
            request.logic_device_configuration.glitch_filters.extend(
                [
                    saleae_pb2.GlitchFilterEntry(
                        channel_index=glitch_filter.channel_index,
                        pulse_width_seconds=glitch_filter.pulse_width_seconds,
                    )
                    for glitch_filter in device_configuration.glitch_filters
                ]
            )
        else:
            raise TypeError("Invalid device configuration type")
        
        if capture_configuration is not None:
            if capture_configuration.buffer_size:
                request.capture_configuration.buffer_size = capture_configuration.buffer_size

            if capture_configuration.capture_mode is not None:
                trigger = capture_configuration.capture_mode

                if isinstance(trigger, ManualCaptureMode):
                    request.capture_configuration.manual_capture_mode.CopyFrom(saleae_pb2.ManualCaptureMode(
                        trim_data_seconds=trigger.trim_data_seconds
                    ))

                elif isinstance(trigger, TimedCaptureMode):
                    request.capture_configuration.timed_capture_mode.CopyFrom(saleae_pb2.TimedCaptureMode(
                        duration_seconds=trigger.duration_seconds,
                        trim_data_seconds=trigger.trim_data_seconds,
                    ))

                elif isinstance(trigger, DigitalTriggerCaptureMode):
                    request.capture_configuration.digital_capture_mode.CopyFrom(saleae_pb2.DigitalTriggerCaptureMode(
                        trigger_channel_index=trigger.trigger_channel_index,
                        trigger_type=trigger.trigger_type.value,
                        min_pulse_width_seconds=trigger.min_pulse_width_seconds,
                        max_pulse_width_seconds=trigger.max_pulse_width_seconds,
                        after_trigger_seconds=trigger.after_trigger_seconds,
                        trim_data_seconds=trigger.trim_data_seconds,
                        linked_channels=[
                            saleae_pb2.DigitalTriggerLinkedChannel(
                                channel_index=linked_channel.channel_index,
                                state=linked_channel.state.value,
                            )
                            for linked_channel in trigger.linked_channels
                        ]
                    ))
                else:
                    raise TypeError("Unexpected trigger type")

        with error_handler():
            reply: saleae_pb2.StartCaptureReply = self.stub.StartCapture(request)

        return Capture(self, reply.capture_info.capture_id)

    def load_capture(self, filepath: str) -> 'Capture':
        """
        Load a capture.

        The returned Capture object will be fully loaded (`wait_until_done` not required).

        Raises:
            InvalidFileError

        """
        request = saleae_pb2.LoadCaptureRequest(filepath=filepath)
        with error_handler():
            reply: saleae_pb2.LoadCaptureReply = self.stub.LoadCapture(request)

        return Capture(self, reply.capture_info.capture_id)




class Capture:
    def __init__(self, manager: Manager, capture_id: int):
        self.manager = manager
        self.capture_id = capture_id

    def add_analyzer(self, name: str, *, label: Optional[str]=None, settings: Optional[Dict[str, Union[str, int, float, bool]]]=None):
        analyzer_settings = {}

        if settings is not None:
            for key, value in settings.items():
                if isinstance(value, str):
                    v = saleae_pb2.AnalyzerSettingValue(string_value=value)
                elif isinstance(value, int):
                    v = saleae_pb2.AnalyzerSettingValue(int64_value=value)
                elif isinstance(value, float):
                    v = saleae_pb2.AnalyzerSettingValue(double_value=value)
                elif isinstance(value, bool):
                    v = saleae_pb2.AnalyzerSettingValue(bool_value=value)
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
        request = saleae_pb2.SaveCaptureRequest(capture_id=self.capture_id, filepath=filepath)
        try:
            reply = self.manager.stub.SaveCapture(request)
        except grpc.RpcError as exc:
            raise grpc_error_to_exception(exc) from None

    def export_analyzer_legacy(self, filepath: str, analyzer: AnalyzerHandle, radix: RadixType):
        request = saleae_pb2.ExportAnalyzerLegacyRequest(
            capture_id=self.capture_id,
            filepath=filepath,
            analyzer_id=analyzer.analyzer_id,
            radix_type=radix.value
        )

        try:
            reply = self.manager.stub.ExportAnalyzerLegacy(request)
        except grpc.RpcError as exc:
            raise grpc_error_to_exception(exc) from None

    def export_data_table(self, filepath: str, analyzers: List['AnalyzerHandle'], *, radix: RadixType, iso8601: bool = False):
        request = saleae_pb2.ExportDataTableRequest(
            capture_id=self.capture_id,
            filepath=filepath,
            analyzer_ids=[h.analyzer_id for h in analyzers],
            iso8601=iso8601,
            radix_type=radix.value)

        with error_handler():
            reply = self.manager.stub.ExportDataTable(request)

    def export_raw_data_csv(self, directory: str, *, analog_channels: Optional[List[int]] = None,
                            digital_channels: Optional[List[int]] = None,
                            analog_downsample_ratio: int = 1, iso8601: bool = False):
        channels = []
        if analog_channels:
            channels.extend([saleae_pb2.ChannelIdentifier(type=saleae_pb2.CHANNEL_TYPE_ANALOG, index=ch) for ch in analog_channels])
        if digital_channels:
            channels.extend([saleae_pb2.ChannelIdentifier(type=saleae_pb2.CHANNEL_TYPE_DIGITAL, index=ch) for ch in digital_channels])

        request = saleae_pb2.ExportRawDataCsvRequest(
            capture_id=self.capture_id,
            directory=directory,
            channels=channels,
            analog_downsample_ratio=analog_downsample_ratio,
            iso8601=iso8601
        )

        with error_handler():
            self.manager.stub.ExportRawDataCsv(request)

    def export_raw_data_binary(self, directory: str, *, analog_channels: Optional[List[int]] = None,
                            digital_channels: Optional[List[int]] = None,
                            analog_downsample_ratio: int = 1):
        channels = []
        if analog_channels:
            channels.extend([saleae_pb2.ChannelIdentifier(type=saleae_pb2.CHANNEL_TYPE_ANALOG, index=ch) for ch in analog_channels])
        if digital_channels:
            channels.extend([saleae_pb2.ChannelIdentifier(type=saleae_pb2.CHANNEL_TYPE_DIGITAL, index=ch) for ch in digital_channels])

        request = saleae_pb2.ExportRawDataBinaryRequest(
            capture_id=self.capture_id,
            directory=directory,
            channels=channels,
            analog_downsample_ratio=analog_downsample_ratio,
        )

        with error_handler():
            self.manager.stub.ExportRawDataBinary(request)

    def close(self):
        request = saleae_pb2.CloseCaptureRequest(capture_id=self.capture_id)
        with error_handler():
            self.manager.stub.CloseCapture(request)

    def stop(self):
        request = saleae_pb2.StopCaptureRequest(capture_id=self.capture_id)
        with error_handler():
            self.manager.stub.StopCapture(request)

    def wait(self):
        request = saleae_pb2.WaitCaptureRequest(capture_id=self.capture_id)
        with error_handler():
            self.manager.stub.WaitCapture(request)


    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()
