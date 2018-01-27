# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ncel/utils/logging.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ncel/utils/logging.proto',
  package='logging',
  syntax='proto2',
  serialized_pb=_b('\n\x18ncel/utils/logging.proto\x12\x07logging\"S\n\x07NcelLog\x12#\n\x06header\x18\x01 \x03(\x0b\x32\x13.logging.NcelHeader\x12#\n\x07\x65ntries\x18\x02 \x03(\x0b\x32\x12.logging.NcelEntry\"\x8a\x02\n\nNcelHeader\x12\x14\n\x0ctotal_params\x18\x01 \x01(\x05\x12\x1a\n\x12model_architecture\x18\x02 \x01(\t\x12\x16\n\x0e\x65val_filenames\x18\x03 \x03(\t\x12\x12\n\nstart_step\x18\x04 \x01(\x05\x12\x12\n\nstart_time\x18\x05 \x01(\x03\x12\x13\n\x0bmodel_label\x18\x06 \x03(\t\x12\x32\n\x05\x66lags\x18\x64 \x03(\x0b\x32#.logging.NcelHeader.CommandLineFlag\x12\x12\n\nextra_logs\x18\x65 \x03(\t\x1a-\n\x0f\x43ommandLineFlag\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x96\x02\n\tNcelEntry\x12\x0c\n\x04step\x18\x01 \x01(\x05\x12\x1a\n\x12\x63\x61ndidate_accuracy\x18\x02 \x01(\x02\x12\x18\n\x10mention_accuracy\x18\x03 \x01(\x02\x12\x19\n\x11\x64ocument_accuracy\x18\x04 \x01(\x02\x12\x12\n\ntotal_cost\x18\x05 \x01(\x02\x12\x0f\n\x07l2_cost\x18\x06 \x01(\x02\x12\x1e\n\x16time_per_token_seconds\x18\x07 \x01(\x02\x12\x15\n\rlearning_rate\x18\x08 \x01(\x02\x12\x13\n\x0bmodel_label\x18\t \x01(\t\x12%\n\nevaluation\x18\n \x03(\x0b\x32\x11.logging.EvalData\x12\x12\n\ncheckpoint\x18\x0b \x01(\t\"\xb1\x01\n\x08\x45valData\x12\x1f\n\x17\x65val_candidate_accuracy\x18\x01 \x01(\x02\x12\x1d\n\x15\x65val_mention_accuracy\x18\x02 \x01(\x02\x12\x1e\n\x16\x65val_document_accuracy\x18\x03 \x01(\x02\x12\x10\n\x08\x66ilename\x18\x04 \x01(\t\x12\x1e\n\x16time_per_token_seconds\x18\x05 \x01(\x02\x12\x13\n\x0breport_path\x18\x06 \x01(\t')
)




_NCELLOG = _descriptor.Descriptor(
  name='NcelLog',
  full_name='logging.NcelLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='logging.NcelLog.header', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entries', full_name='logging.NcelLog.entries', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=120,
)


_NCELHEADER_COMMANDLINEFLAG = _descriptor.Descriptor(
  name='CommandLineFlag',
  full_name='logging.NcelHeader.CommandLineFlag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='logging.NcelHeader.CommandLineFlag.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='logging.NcelHeader.CommandLineFlag.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=344,
  serialized_end=389,
)

_NCELHEADER = _descriptor.Descriptor(
  name='NcelHeader',
  full_name='logging.NcelHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total_params', full_name='logging.NcelHeader.total_params', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_architecture', full_name='logging.NcelHeader.model_architecture', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eval_filenames', full_name='logging.NcelHeader.eval_filenames', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_step', full_name='logging.NcelHeader.start_step', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='logging.NcelHeader.start_time', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_label', full_name='logging.NcelHeader.model_label', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flags', full_name='logging.NcelHeader.flags', index=6,
      number=100, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extra_logs', full_name='logging.NcelHeader.extra_logs', index=7,
      number=101, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_NCELHEADER_COMMANDLINEFLAG, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=123,
  serialized_end=389,
)


_NCELENTRY = _descriptor.Descriptor(
  name='NcelEntry',
  full_name='logging.NcelEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='step', full_name='logging.NcelEntry.step', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='candidate_accuracy', full_name='logging.NcelEntry.candidate_accuracy', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mention_accuracy', full_name='logging.NcelEntry.mention_accuracy', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='document_accuracy', full_name='logging.NcelEntry.document_accuracy', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_cost', full_name='logging.NcelEntry.total_cost', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='l2_cost', full_name='logging.NcelEntry.l2_cost', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_per_token_seconds', full_name='logging.NcelEntry.time_per_token_seconds', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='learning_rate', full_name='logging.NcelEntry.learning_rate', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_label', full_name='logging.NcelEntry.model_label', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='evaluation', full_name='logging.NcelEntry.evaluation', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkpoint', full_name='logging.NcelEntry.checkpoint', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=392,
  serialized_end=670,
)


_EVALDATA = _descriptor.Descriptor(
  name='EvalData',
  full_name='logging.EvalData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='eval_candidate_accuracy', full_name='logging.EvalData.eval_candidate_accuracy', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eval_mention_accuracy', full_name='logging.EvalData.eval_mention_accuracy', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eval_document_accuracy', full_name='logging.EvalData.eval_document_accuracy', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filename', full_name='logging.EvalData.filename', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_per_token_seconds', full_name='logging.EvalData.time_per_token_seconds', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='report_path', full_name='logging.EvalData.report_path', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=673,
  serialized_end=850,
)

_NCELLOG.fields_by_name['header'].message_type = _NCELHEADER
_NCELLOG.fields_by_name['entries'].message_type = _NCELENTRY
_NCELHEADER_COMMANDLINEFLAG.containing_type = _NCELHEADER
_NCELHEADER.fields_by_name['flags'].message_type = _NCELHEADER_COMMANDLINEFLAG
_NCELENTRY.fields_by_name['evaluation'].message_type = _EVALDATA
DESCRIPTOR.message_types_by_name['NcelLog'] = _NCELLOG
DESCRIPTOR.message_types_by_name['NcelHeader'] = _NCELHEADER
DESCRIPTOR.message_types_by_name['NcelEntry'] = _NCELENTRY
DESCRIPTOR.message_types_by_name['EvalData'] = _EVALDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NcelLog = _reflection.GeneratedProtocolMessageType('NcelLog', (_message.Message,), dict(
  DESCRIPTOR = _NCELLOG,
  __module__ = 'ncel.utils.logging_pb2'
  # @@protoc_insertion_point(class_scope:logging.NcelLog)
  ))
_sym_db.RegisterMessage(NcelLog)

NcelHeader = _reflection.GeneratedProtocolMessageType('NcelHeader', (_message.Message,), dict(

  CommandLineFlag = _reflection.GeneratedProtocolMessageType('CommandLineFlag', (_message.Message,), dict(
    DESCRIPTOR = _NCELHEADER_COMMANDLINEFLAG,
    __module__ = 'ncel.utils.logging_pb2'
    # @@protoc_insertion_point(class_scope:logging.NcelHeader.CommandLineFlag)
    ))
  ,
  DESCRIPTOR = _NCELHEADER,
  __module__ = 'ncel.utils.logging_pb2'
  # @@protoc_insertion_point(class_scope:logging.NcelHeader)
  ))
_sym_db.RegisterMessage(NcelHeader)
_sym_db.RegisterMessage(NcelHeader.CommandLineFlag)

NcelEntry = _reflection.GeneratedProtocolMessageType('NcelEntry', (_message.Message,), dict(
  DESCRIPTOR = _NCELENTRY,
  __module__ = 'ncel.utils.logging_pb2'
  # @@protoc_insertion_point(class_scope:logging.NcelEntry)
  ))
_sym_db.RegisterMessage(NcelEntry)

EvalData = _reflection.GeneratedProtocolMessageType('EvalData', (_message.Message,), dict(
  DESCRIPTOR = _EVALDATA,
  __module__ = 'ncel.utils.logging_pb2'
  # @@protoc_insertion_point(class_scope:logging.EvalData)
  ))
_sym_db.RegisterMessage(EvalData)


# @@protoc_insertion_point(module_scope)
