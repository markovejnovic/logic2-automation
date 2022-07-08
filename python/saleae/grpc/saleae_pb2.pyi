from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

ANALOG: ChannelType
ASCII: RadixType
BINARY: RadixType
CAPTURE_IN_PROGRESS: ErrorCode
CIRCULAR: CaptureMode
DECIMAL: RadixType
DESCRIPTOR: _descriptor.FileDescriptor
DEVICE_ERROR: ErrorCode
DIGITAL: ChannelType
FALLING: DigitalTriggerType
HEXADECIMAL: RadixType
HIGH: DigitalTriggerLinkedChannelState
INTERNAL_EXCEPTION: ErrorCode
INVALID_REQUEST: ErrorCode
LOAD_CAPTURE_FAILED: ErrorCode
LOGIC_8: DeviceType
LOGIC_PRO_16: DeviceType
LOGIC_PRO_8: DeviceType
LOW: DigitalTriggerLinkedChannelState
MISSING_DEVICE: ErrorCode
OOM: ErrorCode
PULSE_HIGH: DigitalTriggerType
PULSE_LOW: DigitalTriggerType
RISING: DigitalTriggerType
STOP_AFTER_TIME: CaptureMode
STOP_ON_DIGITAL_TRIGGER: CaptureMode
UNKNOWN_CHANNEL_TYPE: ChannelType
UNKNOWN_DEVICE_TYPE: DeviceType
UNKNOWN_ERROR_CODE: ErrorCode
UNKNOWN_RADIX_TYPE: RadixType
UNSUPPORTED_FILE_TYPE: ErrorCode

class AddAnalyzerReply(_message.Message):
    __slots__ = ["analyzer_id"]
    ANALYZER_ID_FIELD_NUMBER: _ClassVar[int]
    analyzer_id: int
    def __init__(self, analyzer_id: _Optional[int] = ...) -> None: ...

class AddAnalyzerRequest(_message.Message):
    __slots__ = ["analyzer_label", "analyzer_name", "capture_id", "settings"]
    class SettingsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AnalyzerSettingValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AnalyzerSettingValue, _Mapping]] = ...) -> None: ...
    ANALYZER_LABEL_FIELD_NUMBER: _ClassVar[int]
    ANALYZER_NAME_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_ID_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    analyzer_label: str
    analyzer_name: str
    capture_id: int
    settings: _containers.MessageMap[str, AnalyzerSettingValue]
    def __init__(self, capture_id: _Optional[int] = ..., analyzer_name: _Optional[str] = ..., analyzer_label: _Optional[str] = ..., settings: _Optional[_Mapping[str, AnalyzerSettingValue]] = ...) -> None: ...

class AnalyzerSettingValue(_message.Message):
    __slots__ = ["bool_value", "double_value", "int64_value", "string_value"]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    bool_value: bool
    double_value: float
    int64_value: int
    string_value: str
    def __init__(self, string_value: _Optional[str] = ..., int64_value: _Optional[int] = ..., bool_value: bool = ..., double_value: _Optional[float] = ...) -> None: ...

class CaptureInfo(_message.Message):
    __slots__ = ["capture_id"]
    CAPTURE_ID_FIELD_NUMBER: _ClassVar[int]
    capture_id: int
    def __init__(self, capture_id: _Optional[int] = ...) -> None: ...

class CaptureSettings(_message.Message):
    __slots__ = ["buffer_size", "digital_trigger_settings", "manual_trigger_settings", "timed_trigger_settings"]
    BUFFER_SIZE_FIELD_NUMBER: _ClassVar[int]
    DIGITAL_TRIGGER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MANUAL_TRIGGER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TIMED_TRIGGER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    buffer_size: int
    digital_trigger_settings: DigitalTriggerSettings
    manual_trigger_settings: ManualTriggerSettings
    timed_trigger_settings: TimedTriggerSettings
    def __init__(self, buffer_size: _Optional[int] = ..., manual_trigger_settings: _Optional[_Union[ManualTriggerSettings, _Mapping]] = ..., timed_trigger_settings: _Optional[_Union[TimedTriggerSettings, _Mapping]] = ..., digital_trigger_settings: _Optional[_Union[DigitalTriggerSettings, _Mapping]] = ...) -> None: ...

class ChannelIdentifier(_message.Message):
    __slots__ = ["device_id", "index", "type"]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    device_id: int
    index: int
    type: ChannelType
    def __init__(self, device_id: _Optional[int] = ..., type: _Optional[_Union[ChannelType, str]] = ..., index: _Optional[int] = ...) -> None: ...

class CloseCaptureReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CloseCaptureRequest(_message.Message):
    __slots__ = ["capture_id"]
    CAPTURE_ID_FIELD_NUMBER: _ClassVar[int]
    capture_id: int
    def __init__(self, capture_id: _Optional[int] = ...) -> None: ...

class Device(_message.Message):
    __slots__ = ["device_id", "device_type", "serial_number"]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    device_id: int
    device_type: DeviceType
    serial_number: str
    def __init__(self, device_id: _Optional[int] = ..., device_type: _Optional[_Union[DeviceType, str]] = ..., serial_number: _Optional[str] = ...) -> None: ...

class DigitalTriggerLinkedChannel(_message.Message):
    __slots__ = ["channel_index", "state"]
    CHANNEL_INDEX_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    channel_index: int
    state: DigitalTriggerLinkedChannelState
    def __init__(self, channel_index: _Optional[int] = ..., state: _Optional[_Union[DigitalTriggerLinkedChannelState, str]] = ...) -> None: ...

class DigitalTriggerSettings(_message.Message):
    __slots__ = ["linked_channels", "max_pulse_duration", "min_pulse_duration", "post_trigger_seconds", "pre_trigger_seconds", "trigger_channel_index", "trigger_type"]
    LINKED_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    MAX_PULSE_DURATION_FIELD_NUMBER: _ClassVar[int]
    MIN_PULSE_DURATION_FIELD_NUMBER: _ClassVar[int]
    POST_TRIGGER_SECONDS_FIELD_NUMBER: _ClassVar[int]
    PRE_TRIGGER_SECONDS_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_CHANNEL_INDEX_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_TYPE_FIELD_NUMBER: _ClassVar[int]
    linked_channels: _containers.RepeatedCompositeFieldContainer[DigitalTriggerLinkedChannel]
    max_pulse_duration: float
    min_pulse_duration: float
    post_trigger_seconds: float
    pre_trigger_seconds: float
    trigger_channel_index: int
    trigger_type: DigitalTriggerType
    def __init__(self, trigger_type: _Optional[_Union[DigitalTriggerType, str]] = ..., pre_trigger_seconds: _Optional[float] = ..., post_trigger_seconds: _Optional[float] = ..., trigger_channel_index: _Optional[int] = ..., min_pulse_duration: _Optional[float] = ..., max_pulse_duration: _Optional[float] = ..., linked_channels: _Optional[_Iterable[_Union[DigitalTriggerLinkedChannel, _Mapping]]] = ...) -> None: ...

class ExportAnalyzerLegacyReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExportAnalyzerLegacyRequest(_message.Message):
    __slots__ = ["analyzer_id", "capture_id", "filepath", "radix_type"]
    ANALYZER_ID_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_ID_FIELD_NUMBER: _ClassVar[int]
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    RADIX_TYPE_FIELD_NUMBER: _ClassVar[int]
    analyzer_id: int
    capture_id: int
    filepath: str
    radix_type: RadixType
    def __init__(self, capture_id: _Optional[int] = ..., filepath: _Optional[str] = ..., analyzer_id: _Optional[int] = ..., radix_type: _Optional[_Union[RadixType, str]] = ...) -> None: ...

class ExportDataTableReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExportDataTableRequest(_message.Message):
    __slots__ = ["analyzer_ids", "capture_id", "filepath", "iso8601"]
    ANALYZER_IDS_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_ID_FIELD_NUMBER: _ClassVar[int]
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    ISO8601_FIELD_NUMBER: _ClassVar[int]
    analyzer_ids: _containers.RepeatedScalarFieldContainer[int]
    capture_id: int
    filepath: str
    iso8601: bool
    def __init__(self, capture_id: _Optional[int] = ..., filepath: _Optional[str] = ..., analyzer_ids: _Optional[_Iterable[int]] = ..., iso8601: bool = ...) -> None: ...

class ExportRawDataBinaryReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExportRawDataBinaryRequest(_message.Message):
    __slots__ = ["analog_downsample_ratio", "capture_id", "channels", "directory"]
    ANALOG_DOWNSAMPLE_RATIO_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    analog_downsample_ratio: int
    capture_id: int
    channels: _containers.RepeatedCompositeFieldContainer[ChannelIdentifier]
    directory: str
    def __init__(self, capture_id: _Optional[int] = ..., directory: _Optional[str] = ..., channels: _Optional[_Iterable[_Union[ChannelIdentifier, _Mapping]]] = ..., analog_downsample_ratio: _Optional[int] = ...) -> None: ...

class ExportRawDataCsvReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExportRawDataCsvRequest(_message.Message):
    __slots__ = ["analog_downsample_ratio", "capture_id", "channels", "directory", "iso8601"]
    ANALOG_DOWNSAMPLE_RATIO_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    ISO8601_FIELD_NUMBER: _ClassVar[int]
    analog_downsample_ratio: int
    capture_id: int
    channels: _containers.RepeatedCompositeFieldContainer[ChannelIdentifier]
    directory: str
    iso8601: bool
    def __init__(self, capture_id: _Optional[int] = ..., directory: _Optional[str] = ..., channels: _Optional[_Iterable[_Union[ChannelIdentifier, _Mapping]]] = ..., analog_downsample_ratio: _Optional[int] = ..., iso8601: bool = ...) -> None: ...

class GetDevicesReply(_message.Message):
    __slots__ = ["devices"]
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[Device]
    def __init__(self, devices: _Optional[_Iterable[_Union[Device, _Mapping]]] = ...) -> None: ...

class GetDevicesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GlitchFilterEntry(_message.Message):
    __slots__ = ["channel_index", "pulse_width"]
    CHANNEL_INDEX_FIELD_NUMBER: _ClassVar[int]
    PULSE_WIDTH_FIELD_NUMBER: _ClassVar[int]
    channel_index: int
    pulse_width: float
    def __init__(self, channel_index: _Optional[int] = ..., pulse_width: _Optional[float] = ...) -> None: ...

class LoadCaptureReply(_message.Message):
    __slots__ = ["capture_info"]
    CAPTURE_INFO_FIELD_NUMBER: _ClassVar[int]
    capture_info: CaptureInfo
    def __init__(self, capture_info: _Optional[_Union[CaptureInfo, _Mapping]] = ...) -> None: ...

class LoadCaptureRequest(_message.Message):
    __slots__ = ["filepath"]
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    filepath: str
    def __init__(self, filepath: _Optional[str] = ...) -> None: ...

class LogicDeviceConfiguration(_message.Message):
    __slots__ = ["analog_sample_rate", "digital_sample_rate", "digital_threshold", "enabled_analog_channels", "enabled_digital_channels", "glitch_filters"]
    ANALOG_SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    DIGITAL_SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    DIGITAL_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    ENABLED_ANALOG_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_DIGITAL_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    GLITCH_FILTERS_FIELD_NUMBER: _ClassVar[int]
    analog_sample_rate: int
    digital_sample_rate: int
    digital_threshold: float
    enabled_analog_channels: _containers.RepeatedScalarFieldContainer[int]
    enabled_digital_channels: _containers.RepeatedScalarFieldContainer[int]
    glitch_filters: _containers.RepeatedCompositeFieldContainer[GlitchFilterEntry]
    def __init__(self, enabled_digital_channels: _Optional[_Iterable[int]] = ..., enabled_analog_channels: _Optional[_Iterable[int]] = ..., digital_sample_rate: _Optional[int] = ..., analog_sample_rate: _Optional[int] = ..., digital_threshold: _Optional[float] = ..., glitch_filters: _Optional[_Iterable[_Union[GlitchFilterEntry, _Mapping]]] = ...) -> None: ...

class ManualTriggerSettings(_message.Message):
    __slots__ = ["pre_trigger_seconds"]
    PRE_TRIGGER_SECONDS_FIELD_NUMBER: _ClassVar[int]
    pre_trigger_seconds: float
    def __init__(self, pre_trigger_seconds: _Optional[float] = ...) -> None: ...

class RemoveAnalyzerReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RemoveAnalyzerRequest(_message.Message):
    __slots__ = ["analyzer_id", "capture_id"]
    ANALYZER_ID_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_ID_FIELD_NUMBER: _ClassVar[int]
    analyzer_id: int
    capture_id: int
    def __init__(self, capture_id: _Optional[int] = ..., analyzer_id: _Optional[int] = ...) -> None: ...

class SaveCaptureReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SaveCaptureRequest(_message.Message):
    __slots__ = ["capture_id", "filepath"]
    CAPTURE_ID_FIELD_NUMBER: _ClassVar[int]
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    capture_id: int
    filepath: str
    def __init__(self, capture_id: _Optional[int] = ..., filepath: _Optional[str] = ...) -> None: ...

class StartCaptureReply(_message.Message):
    __slots__ = ["capture_info"]
    CAPTURE_INFO_FIELD_NUMBER: _ClassVar[int]
    capture_info: CaptureInfo
    def __init__(self, capture_info: _Optional[_Union[CaptureInfo, _Mapping]] = ...) -> None: ...

class StartCaptureRequest(_message.Message):
    __slots__ = ["capture_settings", "device_serial_number", "logic_device_configuration"]
    CAPTURE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    LOGIC_DEVICE_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    capture_settings: CaptureSettings
    device_serial_number: str
    logic_device_configuration: LogicDeviceConfiguration
    def __init__(self, device_serial_number: _Optional[str] = ..., logic_device_configuration: _Optional[_Union[LogicDeviceConfiguration, _Mapping]] = ..., capture_settings: _Optional[_Union[CaptureSettings, _Mapping]] = ...) -> None: ...

class StopCaptureReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class StopCaptureRequest(_message.Message):
    __slots__ = ["capture_id"]
    CAPTURE_ID_FIELD_NUMBER: _ClassVar[int]
    capture_id: int
    def __init__(self, capture_id: _Optional[int] = ...) -> None: ...

class TimedTriggerSettings(_message.Message):
    __slots__ = ["pre_trigger_seconds", "trigger_seconds"]
    PRE_TRIGGER_SECONDS_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_SECONDS_FIELD_NUMBER: _ClassVar[int]
    pre_trigger_seconds: float
    trigger_seconds: float
    def __init__(self, trigger_seconds: _Optional[float] = ..., pre_trigger_seconds: _Optional[float] = ...) -> None: ...

class WaitCaptureReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class WaitCaptureRequest(_message.Message):
    __slots__ = ["capture_id"]
    CAPTURE_ID_FIELD_NUMBER: _ClassVar[int]
    capture_id: int
    def __init__(self, capture_id: _Optional[int] = ...) -> None: ...

class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class RadixType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class DeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ChannelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class DigitalTriggerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class DigitalTriggerLinkedChannelState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class CaptureMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
