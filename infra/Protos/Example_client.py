import grpc

import example_pb2
import example_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = example_pb2_grpc.ExampleStub(channel)
    response = stub.Send_icmp(example_pb2.send_msg(uid=200001))
    print("Example client received: " + response.msg)

if __name__ == '__main__':
    run()
