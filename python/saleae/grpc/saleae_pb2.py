# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: saleae/grpc/saleae.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18saleae/grpc/saleae.proto\x12\x11saleae.automation\"f\n\x06\x44\x65vice\x12\x11\n\tdevice_id\x18\x01 \x01(\x04\x12\x32\n\x0b\x64\x65vice_type\x18\x02 \x01(\x0e\x32\x1d.saleae.automation.DeviceType\x12\x15\n\rserial_number\x18\x03 \x01(\t\"c\n\x11\x43hannelIdentifier\x12\x11\n\tdevice_id\x18\x01 \x01(\x04\x12,\n\x04type\x18\x02 \x01(\x0e\x32\x1e.saleae.automation.ChannelType\x12\r\n\x05index\x18\x03 \x01(\x04\"!\n\x0b\x43\x61ptureInfo\x12\x12\n\ncapture_id\x18\x01 \x01(\x04\"\xf5\x01\n\x18LogicDeviceConfiguration\x12 \n\x18\x65nabled_digital_channels\x18\x01 \x03(\r\x12\x1f\n\x17\x65nabled_analog_channels\x18\x02 \x03(\r\x12\x1b\n\x13\x64igital_sample_rate\x18\x03 \x01(\r\x12\x1a\n\x12\x61nalog_sample_rate\x18\x04 \x01(\r\x12\x1f\n\x17\x64igital_threshold_volts\x18\x05 \x01(\x01\x12<\n\x0eglitch_filters\x18\x06 \x03(\x0b\x32$.saleae.automation.GlitchFilterEntry\"G\n\x11GlitchFilterEntry\x12\x15\n\rchannel_index\x18\x01 \x01(\r\x12\x1b\n\x13pulse_width_seconds\x18\x02 \x01(\x01\".\n\x11ManualCaptureMode\x12\x19\n\x11trim_data_seconds\x18\x01 \x01(\x01\"G\n\x10TimedCaptureMode\x12\x18\n\x10\x64uration_seconds\x18\x01 \x01(\x01\x12\x19\n\x11trim_data_seconds\x18\x02 \x01(\x01\"x\n\x1b\x44igitalTriggerLinkedChannel\x12\x15\n\rchannel_index\x18\x01 \x01(\r\x12\x42\n\x05state\x18\x02 \x01(\x0e\x32\x33.saleae.automation.DigitalTriggerLinkedChannelState\"\xbc\x02\n\x19\x44igitalTriggerCaptureMode\x12;\n\x0ctrigger_type\x18\x01 \x01(\x0e\x32%.saleae.automation.DigitalTriggerType\x12\x1d\n\x15\x61\x66ter_trigger_seconds\x18\x02 \x01(\x01\x12\x19\n\x11trim_data_seconds\x18\x03 \x01(\x01\x12\x1d\n\x15trigger_channel_index\x18\x04 \x01(\r\x12\x1f\n\x17min_pulse_width_seconds\x18\x05 \x01(\x01\x12\x1f\n\x17max_pulse_width_seconds\x18\x06 \x01(\x01\x12G\n\x0flinked_channels\x18\x07 \x03(\x0b\x32..saleae.automation.DigitalTriggerLinkedChannel\"\x91\x02\n\x14\x43\x61ptureConfiguration\x12\x13\n\x0b\x62uffer_size\x18\x01 \x01(\r\x12\x43\n\x13manual_capture_mode\x18\x02 \x01(\x0b\x32$.saleae.automation.ManualCaptureModeH\x00\x12\x41\n\x12timed_capture_mode\x18\x03 \x01(\x0b\x32#.saleae.automation.TimedCaptureModeH\x00\x12L\n\x14\x64igital_capture_mode\x18\x04 \x01(\x0b\x32,.saleae.automation.DigitalTriggerCaptureModeH\x00\x42\x0e\n\x0c\x63\x61pture_mode\"\x13\n\x11GetDevicesRequest\"=\n\x0fGetDevicesReply\x12*\n\x07\x64\x65vices\x18\x01 \x03(\x0b\x32\x19.saleae.automation.Device\"\xe6\x01\n\x13StartCaptureRequest\x12\x1c\n\x14\x64\x65vice_serial_number\x18\x01 \x01(\t\x12Q\n\x1alogic_device_configuration\x18\x02 \x01(\x0b\x32+.saleae.automation.LogicDeviceConfigurationH\x00\x12\x46\n\x15\x63\x61pture_configuration\x18\x03 \x01(\x0b\x32\'.saleae.automation.CaptureConfigurationB\x16\n\x14\x64\x65vice_configuration\"I\n\x11StartCaptureReply\x12\x34\n\x0c\x63\x61pture_info\x18\x01 \x01(\x0b\x32\x1e.saleae.automation.CaptureInfo\"(\n\x12StopCaptureRequest\x12\x12\n\ncapture_id\x18\x01 \x01(\x04\"\x12\n\x10StopCaptureReply\"(\n\x12WaitCaptureRequest\x12\x12\n\ncapture_id\x18\x01 \x01(\x04\"\x12\n\x10WaitCaptureReply\"&\n\x12LoadCaptureRequest\x12\x10\n\x08\x66ilepath\x18\x01 \x01(\t\"H\n\x10LoadCaptureReply\x12\x34\n\x0c\x63\x61pture_info\x18\x01 \x01(\x0b\x32\x1e.saleae.automation.CaptureInfo\":\n\x12SaveCaptureRequest\x12\x12\n\ncapture_id\x18\x01 \x01(\x04\x12\x10\n\x08\x66ilepath\x18\x02 \x01(\t\"\x12\n\x10SaveCaptureReply\")\n\x13\x43loseCaptureRequest\x12\x12\n\ncapture_id\x18\x01 \x01(\x04\"\x13\n\x11\x43loseCaptureReply\"\xaa\x01\n\x17\x45xportRawDataCsvRequest\x12\x12\n\ncapture_id\x18\x01 \x01(\x04\x12\x11\n\tdirectory\x18\x02 \x01(\t\x12\x36\n\x08\x63hannels\x18\x03 \x03(\x0b\x32$.saleae.automation.ChannelIdentifier\x12\x1f\n\x17\x61nalog_downsample_ratio\x18\x04 \x01(\x04\x12\x0f\n\x07iso8601\x18\x05 \x01(\x08\"\x17\n\x15\x45xportRawDataCsvReply\"\x9c\x01\n\x1a\x45xportRawDataBinaryRequest\x12\x12\n\ncapture_id\x18\x01 \x01(\x04\x12\x11\n\tdirectory\x18\x02 \x01(\t\x12\x36\n\x08\x63hannels\x18\x03 \x03(\x0b\x32$.saleae.automation.ChannelIdentifier\x12\x1f\n\x17\x61nalog_downsample_ratio\x18\x04 \x01(\x04\"\x1a\n\x18\x45xportRawDataBinaryReply\"|\n\x14\x41nalyzerSettingValue\x12\x16\n\x0cstring_value\x18\x01 \x01(\tH\x00\x12\x15\n\x0bint64_value\x18\x02 \x01(\x03H\x00\x12\x14\n\nbool_value\x18\x03 \x01(\x08H\x00\x12\x16\n\x0c\x64ouble_value\x18\x04 \x01(\x01H\x00\x42\x07\n\x05value\"\xf8\x01\n\x12\x41\x64\x64\x41nalyzerRequest\x12\x12\n\ncapture_id\x18\x01 \x01(\x04\x12\x15\n\ranalyzer_name\x18\x02 \x01(\t\x12\x16\n\x0e\x61nalyzer_label\x18\x03 \x01(\t\x12\x45\n\x08settings\x18\x04 \x03(\x0b\x32\x33.saleae.automation.AddAnalyzerRequest.SettingsEntry\x1aX\n\rSettingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x36\n\x05value\x18\x02 \x01(\x0b\x32\'.saleae.automation.AnalyzerSettingValue:\x02\x38\x01\"\'\n\x10\x41\x64\x64\x41nalyzerReply\x12\x13\n\x0b\x61nalyzer_id\x18\x01 \x01(\x04\"@\n\x15RemoveAnalyzerRequest\x12\x12\n\ncapture_id\x18\x01 \x01(\x04\x12\x13\n\x0b\x61nalyzer_id\x18\x02 \x01(\x04\"\x15\n\x13RemoveAnalyzerReply\"\x97\x01\n\x16\x45xportDataTableRequest\x12\x12\n\ncapture_id\x18\x01 \x01(\x04\x12\x10\n\x08\x66ilepath\x18\x02 \x01(\t\x12\x14\n\x0c\x61nalyzer_ids\x18\x03 \x03(\x04\x12\x0f\n\x07iso8601\x18\x05 \x01(\x08\x12\x30\n\nradix_type\x18\x06 \x01(\x0e\x32\x1c.saleae.automation.RadixType\"\x16\n\x14\x45xportDataTableReply\"\x8a\x01\n\x1b\x45xportAnalyzerLegacyRequest\x12\x12\n\ncapture_id\x18\x01 \x01(\x04\x12\x10\n\x08\x66ilepath\x18\x02 \x01(\t\x12\x13\n\x0b\x61nalyzer_id\x18\x03 \x01(\x04\x12\x30\n\nradix_type\x18\x04 \x01(\x0e\x32\x1c.saleae.automation.RadixType\"\x1b\n\x19\x45xportAnalyzerLegacyReply*\xfc\x01\n\tErrorCode\x12\x1a\n\x16\x45RROR_CODE_UNSPECIFIED\x10\x00\x12!\n\x1d\x45RROR_CODE_INTERNAL_EXCEPTION\x10\x01\x12\x1e\n\x1a\x45RROR_CODE_INVALID_REQUEST\x10\n\x12\"\n\x1e\x45RROR_CODE_LOAD_CAPTURE_FAILED\x10\x14\x12\x1c\n\x18\x45RROR_CODE_EXPORT_FAILED\x10\x15\x12\x1d\n\x19\x45RROR_CODE_MISSING_DEVICE\x10\x32\x12\x1b\n\x17\x45RROR_CODE_DEVICE_ERROR\x10\x33\x12\x12\n\x0e\x45RROR_CODE_OOM\x10\x34*\x88\x01\n\tRadixType\x12\x1a\n\x16RADIX_TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11RADIX_TYPE_BINARY\x10\x01\x12\x16\n\x12RADIX_TYPE_DECIMAL\x10\x02\x12\x1a\n\x16RADIX_TYPE_HEXADECIMAL\x10\x03\x12\x14\n\x10RADIX_TYPE_ASCII\x10\x04*}\n\nDeviceType\x12\x1b\n\x17\x44\x45VICE_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13\x44\x45VICE_TYPE_LOGIC_8\x10\x01\x12\x1b\n\x17\x44\x45VICE_TYPE_LOGIC_PRO_8\x10\x02\x12\x1c\n\x18\x44\x45VICE_TYPE_LOGIC_PRO_16\x10\x03*^\n\x0b\x43hannelType\x12\x1c\n\x18\x43HANNEL_TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14\x43HANNEL_TYPE_DIGITAL\x10\x01\x12\x17\n\x13\x43HANNEL_TYPE_ANALOG\x10\x02*\xc6\x01\n\x12\x44igitalTriggerType\x12$\n DIGITAL_TRIGGER_TYPE_UNSPECIFIED\x10\x00\x12\x1f\n\x1b\x44IGITAL_TRIGGER_TYPE_RISING\x10\x01\x12 \n\x1c\x44IGITAL_TRIGGER_TYPE_FALLING\x10\x02\x12#\n\x1f\x44IGITAL_TRIGGER_TYPE_PULSE_HIGH\x10\x03\x12\"\n\x1e\x44IGITAL_TRIGGER_TYPE_PULSE_LOW\x10\x04*\xb5\x01\n DigitalTriggerLinkedChannelState\x12\x34\n0DIGITAL_TRIGGER_LINKED_CHANNEL_STATE_UNSPECIFIED\x10\x00\x12,\n(DIGITAL_TRIGGER_LINKED_CHANNEL_STATE_LOW\x10\x01\x12-\n)DIGITAL_TRIGGER_LINKED_CHANNEL_STATE_HIGH\x10\x02\x32\x9c\n\n\x07Manager\x12X\n\nGetDevices\x12$.saleae.automation.GetDevicesRequest\x1a\".saleae.automation.GetDevicesReply\"\x00\x12^\n\x0cStartCapture\x12&.saleae.automation.StartCaptureRequest\x1a$.saleae.automation.StartCaptureReply\"\x00\x12[\n\x0bStopCapture\x12%.saleae.automation.StopCaptureRequest\x1a#.saleae.automation.StopCaptureReply\"\x00\x12[\n\x0bWaitCapture\x12%.saleae.automation.WaitCaptureRequest\x1a#.saleae.automation.WaitCaptureReply\"\x00\x12[\n\x0bLoadCapture\x12%.saleae.automation.LoadCaptureRequest\x1a#.saleae.automation.LoadCaptureReply\"\x00\x12[\n\x0bSaveCapture\x12%.saleae.automation.SaveCaptureRequest\x1a#.saleae.automation.SaveCaptureReply\"\x00\x12^\n\x0c\x43loseCapture\x12&.saleae.automation.CloseCaptureRequest\x1a$.saleae.automation.CloseCaptureReply\"\x00\x12[\n\x0b\x41\x64\x64\x41nalyzer\x12%.saleae.automation.AddAnalyzerRequest\x1a#.saleae.automation.AddAnalyzerReply\"\x00\x12\x64\n\x0eRemoveAnalyzer\x12(.saleae.automation.RemoveAnalyzerRequest\x1a&.saleae.automation.RemoveAnalyzerReply\"\x00\x12j\n\x10\x45xportRawDataCsv\x12*.saleae.automation.ExportRawDataCsvRequest\x1a(.saleae.automation.ExportRawDataCsvReply\"\x00\x12s\n\x13\x45xportRawDataBinary\x12-.saleae.automation.ExportRawDataBinaryRequest\x1a+.saleae.automation.ExportRawDataBinaryReply\"\x00\x12g\n\x0f\x45xportDataTable\x12).saleae.automation.ExportDataTableRequest\x1a\'.saleae.automation.ExportDataTableReply\"\x00\x12v\n\x14\x45xportAnalyzerLegacy\x12..saleae.automation.ExportAnalyzerLegacyRequest\x1a,.saleae.automation.ExportAnalyzerLegacyReply\"\x00\x42 \n\x06saleaeB\x0bSaleaeProtoP\x01\xa2\x02\x06Saleaeb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'saleae.grpc.saleae_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\006saleaeB\013SaleaeProtoP\001\242\002\006Saleae'
  _ADDANALYZERREQUEST_SETTINGSENTRY._options = None
  _ADDANALYZERREQUEST_SETTINGSENTRY._serialized_options = b'8\001'
  _ERRORCODE._serialized_start=3461
  _ERRORCODE._serialized_end=3713
  _RADIXTYPE._serialized_start=3716
  _RADIXTYPE._serialized_end=3852
  _DEVICETYPE._serialized_start=3854
  _DEVICETYPE._serialized_end=3979
  _CHANNELTYPE._serialized_start=3981
  _CHANNELTYPE._serialized_end=4075
  _DIGITALTRIGGERTYPE._serialized_start=4078
  _DIGITALTRIGGERTYPE._serialized_end=4276
  _DIGITALTRIGGERLINKEDCHANNELSTATE._serialized_start=4279
  _DIGITALTRIGGERLINKEDCHANNELSTATE._serialized_end=4460
  _DEVICE._serialized_start=47
  _DEVICE._serialized_end=149
  _CHANNELIDENTIFIER._serialized_start=151
  _CHANNELIDENTIFIER._serialized_end=250
  _CAPTUREINFO._serialized_start=252
  _CAPTUREINFO._serialized_end=285
  _LOGICDEVICECONFIGURATION._serialized_start=288
  _LOGICDEVICECONFIGURATION._serialized_end=533
  _GLITCHFILTERENTRY._serialized_start=535
  _GLITCHFILTERENTRY._serialized_end=606
  _MANUALCAPTUREMODE._serialized_start=608
  _MANUALCAPTUREMODE._serialized_end=654
  _TIMEDCAPTUREMODE._serialized_start=656
  _TIMEDCAPTUREMODE._serialized_end=727
  _DIGITALTRIGGERLINKEDCHANNEL._serialized_start=729
  _DIGITALTRIGGERLINKEDCHANNEL._serialized_end=849
  _DIGITALTRIGGERCAPTUREMODE._serialized_start=852
  _DIGITALTRIGGERCAPTUREMODE._serialized_end=1168
  _CAPTURECONFIGURATION._serialized_start=1171
  _CAPTURECONFIGURATION._serialized_end=1444
  _GETDEVICESREQUEST._serialized_start=1446
  _GETDEVICESREQUEST._serialized_end=1465
  _GETDEVICESREPLY._serialized_start=1467
  _GETDEVICESREPLY._serialized_end=1528
  _STARTCAPTUREREQUEST._serialized_start=1531
  _STARTCAPTUREREQUEST._serialized_end=1761
  _STARTCAPTUREREPLY._serialized_start=1763
  _STARTCAPTUREREPLY._serialized_end=1836
  _STOPCAPTUREREQUEST._serialized_start=1838
  _STOPCAPTUREREQUEST._serialized_end=1878
  _STOPCAPTUREREPLY._serialized_start=1880
  _STOPCAPTUREREPLY._serialized_end=1898
  _WAITCAPTUREREQUEST._serialized_start=1900
  _WAITCAPTUREREQUEST._serialized_end=1940
  _WAITCAPTUREREPLY._serialized_start=1942
  _WAITCAPTUREREPLY._serialized_end=1960
  _LOADCAPTUREREQUEST._serialized_start=1962
  _LOADCAPTUREREQUEST._serialized_end=2000
  _LOADCAPTUREREPLY._serialized_start=2002
  _LOADCAPTUREREPLY._serialized_end=2074
  _SAVECAPTUREREQUEST._serialized_start=2076
  _SAVECAPTUREREQUEST._serialized_end=2134
  _SAVECAPTUREREPLY._serialized_start=2136
  _SAVECAPTUREREPLY._serialized_end=2154
  _CLOSECAPTUREREQUEST._serialized_start=2156
  _CLOSECAPTUREREQUEST._serialized_end=2197
  _CLOSECAPTUREREPLY._serialized_start=2199
  _CLOSECAPTUREREPLY._serialized_end=2218
  _EXPORTRAWDATACSVREQUEST._serialized_start=2221
  _EXPORTRAWDATACSVREQUEST._serialized_end=2391
  _EXPORTRAWDATACSVREPLY._serialized_start=2393
  _EXPORTRAWDATACSVREPLY._serialized_end=2416
  _EXPORTRAWDATABINARYREQUEST._serialized_start=2419
  _EXPORTRAWDATABINARYREQUEST._serialized_end=2575
  _EXPORTRAWDATABINARYREPLY._serialized_start=2577
  _EXPORTRAWDATABINARYREPLY._serialized_end=2603
  _ANALYZERSETTINGVALUE._serialized_start=2605
  _ANALYZERSETTINGVALUE._serialized_end=2729
  _ADDANALYZERREQUEST._serialized_start=2732
  _ADDANALYZERREQUEST._serialized_end=2980
  _ADDANALYZERREQUEST_SETTINGSENTRY._serialized_start=2892
  _ADDANALYZERREQUEST_SETTINGSENTRY._serialized_end=2980
  _ADDANALYZERREPLY._serialized_start=2982
  _ADDANALYZERREPLY._serialized_end=3021
  _REMOVEANALYZERREQUEST._serialized_start=3023
  _REMOVEANALYZERREQUEST._serialized_end=3087
  _REMOVEANALYZERREPLY._serialized_start=3089
  _REMOVEANALYZERREPLY._serialized_end=3110
  _EXPORTDATATABLEREQUEST._serialized_start=3113
  _EXPORTDATATABLEREQUEST._serialized_end=3264
  _EXPORTDATATABLEREPLY._serialized_start=3266
  _EXPORTDATATABLEREPLY._serialized_end=3288
  _EXPORTANALYZERLEGACYREQUEST._serialized_start=3291
  _EXPORTANALYZERLEGACYREQUEST._serialized_end=3429
  _EXPORTANALYZERLEGACYREPLY._serialized_start=3431
  _EXPORTANALYZERLEGACYREPLY._serialized_end=3458
  _MANAGER._serialized_start=4463
  _MANAGER._serialized_end=5771
# @@protoc_insertion_point(module_scope)