# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/tokeniser/tiktoken.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x61pi/tokeniser/tiktoken.proto\x12\ttokeniser\"\x1a\n\x18ListEncodingNamesRequest\"0\n\x16ListEncodingNamesReply\x12\x16\n\x0e\x65ncoding_names\x18\x01 \x03(\t\"G\n GetTokenNumByEncodingNameRequest\x12\x15\n\rencoding_name\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x03(\t\"$\n\x10GetTokenNumReply\x12\x10\n\x08n_tokens\x18\x01 \x03(\x03\"8\n\x19GetTokenNumByModelRequest\x12\r\n\x05model\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x03(\t2\xb1\x02\n\x0cTiktokeniser\x12]\n\x11ListEncodingNames\x12#.tokeniser.ListEncodingNamesRequest\x1a!.tokeniser.ListEncodingNamesReply\"\x00\x12g\n\x19GetTokenNumByEncodingName\x12+.tokeniser.GetTokenNumByEncodingNameRequest\x1a\x1b.tokeniser.GetTokenNumReply\"\x00\x12Y\n\x12GetTokenNumByModel\x12$.tokeniser.GetTokenNumByModelRequest\x1a\x1b.tokeniser.GetTokenNumReply\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.tokeniser.tiktoken_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LISTENCODINGNAMESREQUEST._serialized_start=43
  _LISTENCODINGNAMESREQUEST._serialized_end=69
  _LISTENCODINGNAMESREPLY._serialized_start=71
  _LISTENCODINGNAMESREPLY._serialized_end=119
  _GETTOKENNUMBYENCODINGNAMEREQUEST._serialized_start=121
  _GETTOKENNUMBYENCODINGNAMEREQUEST._serialized_end=192
  _GETTOKENNUMREPLY._serialized_start=194
  _GETTOKENNUMREPLY._serialized_end=230
  _GETTOKENNUMBYMODELREQUEST._serialized_start=232
  _GETTOKENNUMBYMODELREQUEST._serialized_end=288
  _TIKTOKENISER._serialized_start=291
  _TIKTOKENISER._serialized_end=596
# @@protoc_insertion_point(module_scope)
