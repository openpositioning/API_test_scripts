# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: traj.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntraj.proto\"\xdf\x04\n\nTrajectory\x12\x17\n\x0f\x61ndroid_version\x18\x01 \x01(\t\x12 \n\x08imu_data\x18\x02 \x03(\x0b\x32\x0e.Motion_Sample\x12\x1d\n\x08pdr_data\x18\x03 \x03(\x0b\x32\x0b.Pdr_Sample\x12\'\n\rposition_data\x18\x04 \x03(\x0b\x32\x10.Position_Sample\x12\'\n\rpressure_data\x18\x05 \x03(\x0b\x32\x10.Pressure_Sample\x12!\n\nlight_data\x18\x06 \x03(\x0b\x32\r.Light_Sample\x12\x1f\n\tgnss_data\x18\x07 \x03(\x0b\x32\x0c.GNSS_Sample\x12\x1f\n\twifi_data\x18\x08 \x03(\x0b\x32\x0c.WiFi_Sample\x12\x1a\n\x08\x61ps_data\x18\t \x03(\x0b\x32\x08.AP_Data\x12\x17\n\x0fstart_timestamp\x18\n \x01(\x03\x12\x17\n\x0f\x64\x61ta_identifier\x18\x0b \x01(\t\x12(\n\x12\x61\x63\x63\x65lerometer_info\x18\x0c \x01(\x0b\x32\x0c.Sensor_Info\x12$\n\x0egyroscope_info\x18\r \x01(\x0b\x32\x0c.Sensor_Info\x12*\n\x14rotation_vector_info\x18\x0e \x01(\x0b\x32\x0c.Sensor_Info\x12\'\n\x11magnetometer_info\x18\x0f \x01(\x0b\x32\x0c.Sensor_Info\x12$\n\x0e\x62\x61rometer_info\x18\x10 \x01(\x0b\x32\x0c.Sensor_Info\x12\'\n\x11light_sensor_info\x18\x11 \x01(\x0b\x32\x0c.Sensor_Info\">\n\nPdr_Sample\x12\x1a\n\x12relative_timestamp\x18\x01 \x01(\x03\x12\t\n\x01x\x18\x02 \x01(\x02\x12\t\n\x01y\x18\x03 \x01(\x02\"\x85\x02\n\rMotion_Sample\x12\x1a\n\x12relative_timestamp\x18\x01 \x01(\x03\x12\r\n\x05\x61\x63\x63_x\x18\x02 \x01(\x02\x12\r\n\x05\x61\x63\x63_y\x18\x03 \x01(\x02\x12\r\n\x05\x61\x63\x63_z\x18\x04 \x01(\x02\x12\r\n\x05gyr_x\x18\x05 \x01(\x02\x12\r\n\x05gyr_y\x18\x06 \x01(\x02\x12\r\n\x05gyr_z\x18\x07 \x01(\x02\x12\x19\n\x11rotation_vector_x\x18\x08 \x01(\x02\x12\x19\n\x11rotation_vector_y\x18\t \x01(\x02\x12\x19\n\x11rotation_vector_z\x18\n \x01(\x02\x12\x19\n\x11rotation_vector_w\x18\x0b \x01(\x02\x12\x12\n\nstep_count\x18\x0c \x01(\x05\"Z\n\x0fPosition_Sample\x12\x1a\n\x12relative_timestamp\x18\x01 \x01(\x03\x12\r\n\x05mag_x\x18\x02 \x01(\x02\x12\r\n\x05mag_y\x18\x03 \x01(\x02\x12\r\n\x05mag_z\x18\x04 \x01(\x02\"?\n\x0fPressure_Sample\x12\x1a\n\x12relative_timestamp\x18\x01 \x01(\x03\x12\x10\n\x08pressure\x18\x02 \x01(\x02\"9\n\x0cLight_Sample\x12\x1a\n\x12relative_timestamp\x18\x01 \x01(\x03\x12\r\n\x05light\x18\x02 \x01(\x02\"\x93\x01\n\x0bGNSS_Sample\x12\x1a\n\x12relative_timestamp\x18\x01 \x01(\x03\x12\x10\n\x08latitude\x18\x02 \x01(\x02\x12\x11\n\tlongitude\x18\x03 \x01(\x02\x12\x10\n\x08\x61ltitude\x18\x04 \x01(\x02\x12\x10\n\x08\x61\x63\x63uracy\x18\x05 \x01(\x02\x12\r\n\x05speed\x18\x06 \x01(\x02\x12\x10\n\x08provider\x18\x07 \x01(\t\"G\n\x0bWiFi_Sample\x12\x1a\n\x12relative_timestamp\x18\x01 \x01(\x03\x12\x1c\n\tmac_scans\x18\x02 \x03(\x0b\x32\t.Mac_Scan\"A\n\x08Mac_Scan\x12\x1a\n\x12relative_timestamp\x18\x01 \x01(\x03\x12\x0b\n\x03mac\x18\x02 \x01(\x03\x12\x0c\n\x04rssi\x18\x03 \x01(\x05\"7\n\x07\x41P_Data\x12\x0b\n\x03mac\x18\x01 \x01(\x03\x12\x0c\n\x04ssid\x18\x02 \x01(\t\x12\x11\n\tfrequency\x18\x03 \x01(\x03\"m\n\x0bSensor_Info\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06vendor\x18\x02 \x01(\t\x12\x12\n\nresolution\x18\x03 \x01(\x02\x12\r\n\x05power\x18\x04 \x01(\x02\x12\x0f\n\x07version\x18\x05 \x01(\x05\x12\x0c\n\x04type\x18\x06 \x01(\x05\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'traj_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_TRAJECTORY']._serialized_start=15
  _globals['_TRAJECTORY']._serialized_end=622
  _globals['_PDR_SAMPLE']._serialized_start=624
  _globals['_PDR_SAMPLE']._serialized_end=686
  _globals['_MOTION_SAMPLE']._serialized_start=689
  _globals['_MOTION_SAMPLE']._serialized_end=950
  _globals['_POSITION_SAMPLE']._serialized_start=952
  _globals['_POSITION_SAMPLE']._serialized_end=1042
  _globals['_PRESSURE_SAMPLE']._serialized_start=1044
  _globals['_PRESSURE_SAMPLE']._serialized_end=1107
  _globals['_LIGHT_SAMPLE']._serialized_start=1109
  _globals['_LIGHT_SAMPLE']._serialized_end=1166
  _globals['_GNSS_SAMPLE']._serialized_start=1169
  _globals['_GNSS_SAMPLE']._serialized_end=1316
  _globals['_WIFI_SAMPLE']._serialized_start=1318
  _globals['_WIFI_SAMPLE']._serialized_end=1389
  _globals['_MAC_SCAN']._serialized_start=1391
  _globals['_MAC_SCAN']._serialized_end=1456
  _globals['_AP_DATA']._serialized_start=1458
  _globals['_AP_DATA']._serialized_end=1513
  _globals['_SENSOR_INFO']._serialized_start=1515
  _globals['_SENSOR_INFO']._serialized_end=1624
# @@protoc_insertion_point(module_scope)