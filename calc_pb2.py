# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calc.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ncalc.proto\x12\ncalculator\"(\n\nAddRequest\x12\x0c\n\x04num1\x18\x01 \x01(\x05\x12\x0c\n\x04num2\x18\x02 \x01(\x05\"\x1d\n\x0b\x41\x64\x64Response\x12\x0e\n\x06result\x18\x01 \x01(\x05\x32\x44\n\nCalculator\x12\x36\n\x03\x41\x64\x64\x12\x16.calculator.AddRequest\x1a\x17.calculator.AddResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'calc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ADDREQUEST']._serialized_start=26
  _globals['_ADDREQUEST']._serialized_end=66
  _globals['_ADDRESPONSE']._serialized_start=68
  _globals['_ADDRESPONSE']._serialized_end=97
  _globals['_CALCULATOR']._serialized_start=99
  _globals['_CALCULATOR']._serialized_end=167
# @@protoc_insertion_point(module_scope)
