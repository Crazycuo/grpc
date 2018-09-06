from concurrent import futures
import time

import grpc

import example_pb2
import example_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class Example(example_pb2_grpc.ExampleServicer):

    def Send_icmp(self, request, context):
        return example_pb2.ack_msg(msg='Hello user: %d' %request.uid)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_ExampleServicer_to_server(Example(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
