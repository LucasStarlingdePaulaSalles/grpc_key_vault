from __future__ import print_function
import sys
import grpc
import vault_pb2, vault_pb2_grpc

def run():
    if len(sys.argv) != 2:
        print("Please provide server address: python3 client.py <address>")
        return
    addr = sys.argv[1]
    channel = grpc.insecure_channel(addr)
    stub = vault_pb2_grpc.VaultStub(channel)

    while(True):
        args = input().split(',')
        if args[0] == 'T':
            response = stub.terminate(vault_pb2.RequestDT())   
            print(response.retval)
            channel.close()
            return
        elif args[0] == 'I':
            response = stub.insert(vault_pb2.RequestDT(
                key=int(args[1]),
                desc=args[2],
                val=int(args[3]))
            )
            print(response.retval)
        elif args[0] == 'C':
            response = stub.consult(vault_pb2.RequestDT(key=int(args[1])))
            if response.retdesc == "":
                print(-1)
            else:
                print(f"{response.retdesc},{response.retval}")

if __name__ == '__main__':
    run() 