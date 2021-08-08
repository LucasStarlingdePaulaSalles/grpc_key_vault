from concurrent import futures
import sys
import grpc
import vault_pb2, vault_pb2_grpc
import compound_pb2, compound_pb2_grpc

class Compound(compound_pb2_grpc.CompoundServicer):
    def consult(self, req, context):
        siga_response = stub_vault1.consult(vault_pb2.RequestDT(key=req.key))
        name = siga_response.retdesc
        matr = siga_response.retval
        if name != "":
            mat_response = stub_vault2.consult(vault_pb2.RequestDT(key=matr))
            course = mat_response.retdesc
            cred = mat_response.retval
            if course == "":
                course = "N/M"

            return compound_pb2.ResponseDT(str1=name,
             val1=matr,
             str2=course,
             val2=cred)

        return compound_pb2.ResponseDT(str1="",val1=0,str2="",val2=0)

    def terminate(self, r,  context):
        vault1_resp = stub_vault1.terminate(vault_pb2.RequestDT())
        vault1_t = vault1_resp.retval
        channel_vault1.close()

        vault2_resp = stub_vault2.terminate(vault_pb2.RequestDT())
        vault2_t = vault2_resp.retval
        channel_vault2.close()

        # print("Terminating in 1 ...")
        server.stop(1)
        return compound_pb2.ResponseDT(val1=vault1_t+vault2_t)


def serve():
    if len(sys.argv) != 4:
        print("Please provide server arguments: python3 server.py <server_port> <vault1_address> <vault2_address>")
        return
    port = sys.argv[1]
    vault1_addr = sys.argv[2]
    vault2_addr = sys.argv[3]

    global channel_vault1
    channel_vault1 = grpc.insecure_channel(vault1_addr)
    global stub_vault1
    stub_vault1 = vault_pb2_grpc.VaultStub(channel_vault1)

    global channel_vault2
    channel_vault2 = grpc.insecure_channel(vault2_addr)
    global stub_vault2
    stub_vault2 = vault_pb2_grpc.VaultStub(channel_vault2)

    global server 
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    compound_pb2_grpc.add_CompoundServicer_to_server(Compound(), server)
    addr = 'localhost:%s' % str(port)
    server.add_insecure_port(addr)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()