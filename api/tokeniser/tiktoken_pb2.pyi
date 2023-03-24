from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetTokenNumByEncodingNameRequest(_message.Message):
    __slots__ = ["encoding_name", "text"]
    ENCODING_NAME_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    encoding_name: str
    text: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, encoding_name: _Optional[str] = ..., text: _Optional[_Iterable[str]] = ...) -> None: ...

class GetTokenNumByModelRequest(_message.Message):
    __slots__ = ["model", "text"]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    model: str
    text: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, model: _Optional[str] = ..., text: _Optional[_Iterable[str]] = ...) -> None: ...

class GetTokenNumReply(_message.Message):
    __slots__ = ["n_tokens"]
    N_TOKENS_FIELD_NUMBER: _ClassVar[int]
    n_tokens: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, n_tokens: _Optional[_Iterable[int]] = ...) -> None: ...

class ListEncodingNamesReply(_message.Message):
    __slots__ = ["encoding_names"]
    ENCODING_NAMES_FIELD_NUMBER: _ClassVar[int]
    encoding_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, encoding_names: _Optional[_Iterable[str]] = ...) -> None: ...

class ListEncodingNamesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
