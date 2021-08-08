from __future__ import print_function
import sys
import grpc
import vault_pb2, vault_pb2_grpc

def run():
    if len(sys.argv) != 2: # wrong execution 
        print("Please provide server address: python3 client.py <address>")
        return
    
    # connection with grpc server
    addr = sys.argv[1]
    channel = grpc.insecure_channel(addr)
    stub = vault_pb2_grpc.VaultStub(channel)

    # cli execution
    while(True):
        # command and parameters parsing
        args = input().split(',')

        # command selection
        if args[0] == 'T': #termination
            response = stub.terminate(vault_pb2.RequestDT())   
            print(response.retval)
            channel.close()
            return
        elif args[0] == 'I': #insertion
            response = stub.insert(vault_pb2.RequestDT(
                key=int(args[1]),
                desc=args[2],
                val=int(args[3]))
            )
            print(response.retval)
        elif args[0] == 'C': #consult
            response = stub.consult(vault_pb2.RequestDT(key=int(args[1])))
            if response.retdesc == "":
                print(-1)
            else:
                print(f"{response.retdesc},{response.retval}")

if __name__ == '__main__':
    run() 