from __future__ import print_function
import sys
import grpc
import compound_pb2, compound_pb2_grpc


def run():
    if len(sys.argv) != 2:
        print("Please provide server address: python3 client.py <address>")
        return
    addr = sys.argv[1]
    channel = grpc.insecure_channel(addr)
    stub = compound_pb2_grpc.CompoundStub(channel)

    while(True):
        args = input().split(',')
        
        if args[0] == 'T':
            response = stub.terminate(compound_pb2.RequestDT())   
            print(response.val1)
            channel.close()
            return
        elif args[0] == 'C':
            response = stub.consult(compound_pb2.RequestDT(key=int(args[1])))
            print(f"{response.str1},{response.val1},{response.str2},{response.val2}")

if __name__ == '__main__':
    run() 