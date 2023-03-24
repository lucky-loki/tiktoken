import argparse
import asyncio
import logging

import grpc
from api.tokeniser import tiktoken_pb2_grpc
from services.tokenizer import tokenizer

parser = argparse.ArgumentParser()
parser.add_argument('--port', '-p', default="localhost:50051", help='server port listen on')

async def serve(listen_addr: str) -> None:
    server = grpc.aio.server()
    tiktoken_pb2_grpc.add_TiktokeniserServicer_to_server(tokenizer.Tokeniser(), server)
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve(parser.parse_args().port))
