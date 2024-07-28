import grpc
from concurrent import futures
import calc_pb2, calc_pb2_grpc

class CalculatorService(calc_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.num1 + request.num2
        return calc_pb2.AddResponse(result=result)
    
def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # add service to server
    calc_pb2_grpc.add_CalculatorServicer_to_server(CalculatorService(), server)
    # start the server
    print('Starting server. Listening on port 50051.')
    server.add_insecure_port('[::]:50051')
    server.start()
    # keep server running
    server.wait_for_termination()

if __name__ == '__main__':
    serve()