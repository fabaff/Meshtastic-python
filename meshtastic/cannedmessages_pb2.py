# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cannedmessages.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cannedmessages.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\023com.geeksville.meshB\031CannedMessageConfigProtosH\003Z!github.com/meshtastic/gomeshproto',
  serialized_pb=b'\n\x14\x63\x61nnedmessages.proto\"w\n\x19\x43\x61nnedMessageModuleConfig\x12\x15\n\rmessagesPart1\x18\x0b \x01(\t\x12\x15\n\rmessagesPart2\x18\x0c \x01(\t\x12\x15\n\rmessagesPart3\x18\r \x01(\t\x12\x15\n\rmessagesPart4\x18\x0e \x01(\tBU\n\x13\x63om.geeksville.meshB\x19\x43\x61nnedMessageConfigProtosH\x03Z!github.com/meshtastic/gomeshprotob\x06proto3'
)




_CANNEDMESSAGEMODULECONFIG = _descriptor.Descriptor(
  name='CannedMessageModuleConfig',
  full_name='CannedMessageModuleConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='messagesPart1', full_name='CannedMessageModuleConfig.messagesPart1', index=0,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='messagesPart2', full_name='CannedMessageModuleConfig.messagesPart2', index=1,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='messagesPart3', full_name='CannedMessageModuleConfig.messagesPart3', index=2,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='messagesPart4', full_name='CannedMessageModuleConfig.messagesPart4', index=3,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=143,
)

DESCRIPTOR.message_types_by_name['CannedMessageModuleConfig'] = _CANNEDMESSAGEMODULECONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CannedMessageModuleConfig = _reflection.GeneratedProtocolMessageType('CannedMessageModuleConfig', (_message.Message,), {
  'DESCRIPTOR' : _CANNEDMESSAGEMODULECONFIG,
  '__module__' : 'cannedmessages_pb2'
  # @@protoc_insertion_point(class_scope:CannedMessageModuleConfig)
  })
_sym_db.RegisterMessage(CannedMessageModuleConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
