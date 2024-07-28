import grpc
import calc_pb2
import calc_pb2_grpc

def run(num1, num2):
    # create a channle to connect to server
    with grpc.insecure_channel("localhost:50051") as channel:
        # create a stub using client class
        stub = calc_pb2_grpc.CalculatorStub(channel)
        # call the stub to call service
        resp = stub.Add(calc_pb2.AddRequest(num1=num1, num2=num2))
    print(f"Resp: {resp.result}")


if __name__ == '__main__':
    num1 = int(input("Please input num1: "))
    num2 = int(input("Please input num2: "))
    run(num1, num2)


