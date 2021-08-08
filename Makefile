VDIR=vault
CDIR=compound

run_serv_arm:
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. vault.proto 
	python3 ./vault_server.py $(arg)

run_cli_arm:
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. vault.proto 
	python3 ./vault_client.py $(arg)

run_serv_comp:
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. vault.proto 
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. compound.proto 
	python3 server.py $(arg1) $(arg2) $(arg3)

run_cli_comp:
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. compound.proto 
	python3 ./client.py $(arg)


clean:
	rm -f ./*_pb2* 2> /dev/null
	rm -rf ./__pycache__ 2> /dev/null