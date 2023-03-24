import grpc
import tiktoken

from api.tokeniser import tiktoken_pb2
from api.tokeniser import tiktoken_pb2_grpc


class Tokeniser(tiktoken_pb2_grpc.TiktokeniserServicer):

    async def ListEncodingNames(self, request, context) -> tiktoken_pb2.ListEncodingNamesReply:
        return tiktoken_pb2.ListEncodingNamesReply(encoding_names=tiktoken.list_encoding_names())

    async def GetTokenNumByEncodingName(self, request: tiktoken_pb2.GetTokenNumByEncodingNameRequest,
                          context: grpc.aio.ServicerContext) -> tiktoken_pb2.GetTokenNumReply:
        enc = tiktoken.get_encoding(request.encoding_name)
        n_tokens = [len(enc.encode(text)) for text in request.text]
        return tiktoken_pb2.GetTokenNumReply(n_tokens=n_tokens)

    async def GetTokenNumByModel(self, request: tiktoken_pb2.GetTokenNumByModelRequest,
                                 context: grpc.aio.ServicerContext) -> tiktoken_pb2.GetTokenNumReply:
        enc = tiktoken.encoding_for_model(request.model)
        n_tokens = [len(enc.encode(text)) for text in request.text]
        return tiktoken_pb2.GetTokenNumReply(n_tokens=n_tokens)