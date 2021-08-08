from concurrent import futures
import sys
import grpc
from vault import vault_pb2, vault_pb2_grpc
import compound_pb2, compound_pb2_grpc

class Compound(compound_pb2_grpc.CompoundServicer):
    def consult(self, req, context):
        print(f"consult {req.key}")

        return compound_pb2.ResponseDT()

    def terminate(self, r,  context):
        # print("Terminating in 1 ...")
        server.stop(1)
        return compound_pb2.ResponseDT(retval=0)


def serve():
    if len(sys.argv) != 4:
        print("Please provide server arguments: python3 server.py <server_port> <vault1_address> <vault2_address>")
        return
    port = sys.argv[1]
    vault1_addr = sys.argv[2]
    vault2_addr = sys.argv[3]


    global server 
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    compound_pb2_grpc.add_CompoundServicer_to_server(Compound(), server)
    addr = 'localhost:%s' % str(port)
    server.add_insecure_port(addr)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()