# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: testim_pb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='testim_pb.proto',
  package='',
  serialized_pb=_b('\n\x0ftestim_pb.proto\"Y\n\x0blogin_proxy\x12\x12\n\nim_account\x18\x01 \x02(\x0c\x12\x11\n\tauth_code\x18\x02 \x02(\x0c\x12\x0e\n\x06im_uid\x18\x03 \x02(\x05\x12\x13\n\x0bproxy_topic\x18\x04 \x01(\x0c\"3\n\terrorinfo\x12\x12\n\nerror_code\x18\x01 \x02(\x05\x12\x12\n\nerror_info\x18\x02 \x01(\x0c\"\xce\x01\n\x0bmsg_content\x12\x0b\n\x03msg\x18\x01 \x02(\x0c\x12\x0f\n\x07msg_url\x18\x02 \x01(\x0c\x12\x11\n\tvoice_len\x18\x03 \x01(\x05\x12\x11\n\tlongitude\x18\x04 \x01(\x01\x12\x10\n\x08latitude\x18\x05 \x01(\x01\x12\x16\n\x0bthumb_width\x18\x06 \x01(\x05:\x01\x30\x12\x16\n\x0bthumb_hight\x18\x07 \x01(\x05:\x01\x30\x12\x10\n\x08nickname\x18\x08 \x01(\x0c\x12\x12\n\navatar_url\x18\t \x01(\x0c\x12\x13\n\x0bred_pket_id\x18\n \x01(\x05\"?\n\x0flogin_proxy_ack\x12\x11\n\tsessionid\x18\x01 \x01(\x05\x12\x19\n\x05\x65rror\x18\x02 \x01(\x0b\x32\n.errorinfo\"\x90\x01\n\x07msgbody\x12\x19\n\x03msg\x18\x01 \x02(\x0b\x32\x0c.msg_content\x12\x12\n\nmsg_serial\x18\x02 \x01(\x0c\x12\x0c\n\x04time\x18\x03 \x01(\x03\x12\x16\n\x0estrange_stauts\x18\x04 \x01(\x05\x12\x14\n\x0cmsg_serial_t\x18\x05 \x01(\x03\x12\x1a\n\x05gtype\x18\x06 \x01(\x0e\x32\x0b.group_type\"`\n\x0bmsgbody_ack\x12\x19\n\x05\x65rror\x18\x01 \x02(\x0b\x32\n.errorinfo\x12\x12\n\nmsg_serial\x18\x02 \x01(\x0c\x12\x0c\n\x04time\x18\x03 \x01(\x03\x12\x14\n\x0cmsg_serial_t\x18\x04 \x01(\x03*[\n\ngroup_type\x12\x11\n\runknown_group\x10\x00\x12\x12\n\x0e\x62usiness_group\x10\x01\x12\x10\n\x0c\x63ommon_group\x10\x02\x12\x14\n\x10\x64iscussion_group\x10\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_GROUP_TYPE = _descriptor.EnumDescriptor(
  name='group_type',
  full_name='group_type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='unknown_group', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='business_group', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='common_group', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='discussion_group', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=682,
  serialized_end=773,
)
_sym_db.RegisterEnumDescriptor(_GROUP_TYPE)

group_type = enum_type_wrapper.EnumTypeWrapper(_GROUP_TYPE)
unknown_group = 0
business_group = 1
common_group = 2
discussion_group = 3



_LOGIN_PROXY = _descriptor.Descriptor(
  name='login_proxy',
  full_name='login_proxy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='im_account', full_name='login_proxy.im_account', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auth_code', full_name='login_proxy.auth_code', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='im_uid', full_name='login_proxy.im_uid', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='proxy_topic', full_name='login_proxy.proxy_topic', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=108,
)


_ERRORINFO = _descriptor.Descriptor(
  name='errorinfo',
  full_name='errorinfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='errorinfo.error_code', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_info', full_name='errorinfo.error_info', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=161,
)


_MSG_CONTENT = _descriptor.Descriptor(
  name='msg_content',
  full_name='msg_content',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='msg_content.msg', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg_url', full_name='msg_content.msg_url', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='voice_len', full_name='msg_content.voice_len', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='msg_content.longitude', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='msg_content.latitude', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='thumb_width', full_name='msg_content.thumb_width', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='thumb_hight', full_name='msg_content.thumb_hight', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='msg_content.nickname', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar_url', full_name='msg_content.avatar_url', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='red_pket_id', full_name='msg_content.red_pket_id', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=164,
  serialized_end=370,
)


_LOGIN_PROXY_ACK = _descriptor.Descriptor(
  name='login_proxy_ack',
  full_name='login_proxy_ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sessionid', full_name='login_proxy_ack.sessionid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='login_proxy_ack.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=372,
  serialized_end=435,
)


_MSGBODY = _descriptor.Descriptor(
  name='msgbody',
  full_name='msgbody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='msgbody.msg', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg_serial', full_name='msgbody.msg_serial', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='msgbody.time', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='strange_stauts', full_name='msgbody.strange_stauts', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg_serial_t', full_name='msgbody.msg_serial_t', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gtype', full_name='msgbody.gtype', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=438,
  serialized_end=582,
)


_MSGBODY_ACK = _descriptor.Descriptor(
  name='msgbody_ack',
  full_name='msgbody_ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='msgbody_ack.error', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg_serial', full_name='msgbody_ack.msg_serial', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='msgbody_ack.time', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg_serial_t', full_name='msgbody_ack.msg_serial_t', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=584,
  serialized_end=680,
)

_LOGIN_PROXY_ACK.fields_by_name['error'].message_type = _ERRORINFO
_MSGBODY.fields_by_name['msg'].message_type = _MSG_CONTENT
_MSGBODY.fields_by_name['gtype'].enum_type = _GROUP_TYPE
_MSGBODY_ACK.fields_by_name['error'].message_type = _ERRORINFO
DESCRIPTOR.message_types_by_name['login_proxy'] = _LOGIN_PROXY
DESCRIPTOR.message_types_by_name['errorinfo'] = _ERRORINFO
DESCRIPTOR.message_types_by_name['msg_content'] = _MSG_CONTENT
DESCRIPTOR.message_types_by_name['login_proxy_ack'] = _LOGIN_PROXY_ACK
DESCRIPTOR.message_types_by_name['msgbody'] = _MSGBODY
DESCRIPTOR.message_types_by_name['msgbody_ack'] = _MSGBODY_ACK
DESCRIPTOR.enum_types_by_name['group_type'] = _GROUP_TYPE

login_proxy = _reflection.GeneratedProtocolMessageType('login_proxy', (_message.Message,), dict(
  DESCRIPTOR = _LOGIN_PROXY,
  __module__ = 'testim_pb_pb2'
  # @@protoc_insertion_point(class_scope:login_proxy)
  ))
_sym_db.RegisterMessage(login_proxy)

errorinfo = _reflection.GeneratedProtocolMessageType('errorinfo', (_message.Message,), dict(
  DESCRIPTOR = _ERRORINFO,
  __module__ = 'testim_pb_pb2'
  # @@protoc_insertion_point(class_scope:errorinfo)
  ))
_sym_db.RegisterMessage(errorinfo)

msg_content = _reflection.GeneratedProtocolMessageType('msg_content', (_message.Message,), dict(
  DESCRIPTOR = _MSG_CONTENT,
  __module__ = 'testim_pb_pb2'
  # @@protoc_insertion_point(class_scope:msg_content)
  ))
_sym_db.RegisterMessage(msg_content)

login_proxy_ack = _reflection.GeneratedProtocolMessageType('login_proxy_ack', (_message.Message,), dict(
  DESCRIPTOR = _LOGIN_PROXY_ACK,
  __module__ = 'testim_pb_pb2'
  # @@protoc_insertion_point(class_scope:login_proxy_ack)
  ))
_sym_db.RegisterMessage(login_proxy_ack)

msgbody = _reflection.GeneratedProtocolMessageType('msgbody', (_message.Message,), dict(
  DESCRIPTOR = _MSGBODY,
  __module__ = 'testim_pb_pb2'
  # @@protoc_insertion_point(class_scope:msgbody)
  ))
_sym_db.RegisterMessage(msgbody)

msgbody_ack = _reflection.GeneratedProtocolMessageType('msgbody_ack', (_message.Message,), dict(
  DESCRIPTOR = _MSGBODY_ACK,
  __module__ = 'testim_pb_pb2'
  # @@protoc_insertion_point(class_scope:msgbody_ack)
  ))
_sym_db.RegisterMessage(msgbody_ack)


# @@protoc_insertion_point(module_scope)
