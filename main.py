import argparse
import asyncio
import datetime
import logging

import grpc
from api.tokeniser import tiktoken_pb2_grpc
from services.tokenizer import tokenizer

parser = argparse.ArgumentParser()
parser.add_argument('--port', '-p', default="localhost:50051", help='server port listen on')
parser.add_argument("--log_file", '-f', default="log/out.log-" + str(datetime.date.today()), help='server log file write to')

async def serve(listen_addr: str) -> None:
    server = grpc.aio.server()
    tiktoken_pb2_grpc.add_TiktokeniserServicer_to_server(tokenizer.Tokeniser(), server)
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s",
                        handlers=[
                            logging.FileHandler(args.log_file),
                            logging.StreamHandler()
                        ])
    asyncio.run(serve(args.port))
