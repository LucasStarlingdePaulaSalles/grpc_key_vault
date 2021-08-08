from concurrent import futures
import sys
import grpc
import vault_pb2, vault_pb2_grpc

class Vault(vault_pb2_grpc.VaultServicer):
    def insert(self, req, context):
        # print(f"insert {req.key}:({req.desc}, {req.val})")
        if req.key in storage.keys():
            return vault_pb2.ResponseDT(retval=-1)
        storage[req.key] = (req.desc, req.val)
        return vault_pb2.ResponseDT(retval=0)


    def consult(self, req, context):
        # print(f"consult {req.key}")
        if req.key in storage.keys():
            return vault_pb2.ResponseDT(retval=storage[req.key][1], retdesc=storage[req.key][0])
        return vault_pb2.ResponseDT(retval=0, retdesc="")

    def terminate(self, r,  context):
        # print("Terminating in 1 ...")
        server.stop(1)
        return vault_pb2.ResponseDT(retval=0)


def serve():
    if len(sys.argv) != 2:
        print("Please provide server port: python3 server.py <port_number>")
        return
    port = sys.argv[1]
    global storage
    storage = {}
    global server 
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    vault_pb2_grpc.add_VaultServicer_to_server(Vault(), server)
    addr = 'localhost:%s' % str(port)
    server.add_insecure_port(addr)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()