VDIR=vault

run_serv_arm:
	python3 -m grpc_tools.protoc -I$(VDIR) --python_out=$(VDIR) --grpc_python_out=$(VDIR) vault.proto 
	python3 $(VDIR)/server.py $(arg) 

run_cli_arm:
	python3 -m grpc_tools.protoc -I$(VDIR) --python_out=$(VDIR) --grpc_python_out=$(VDIR) vault.proto 
	python3 $(VDIR)/client.py $(arg) 


clean:
	rm -f $(VDIR)/vault_pb2* 2> /dev/null
	rm -rf $(VDIR)/__pycache__ 2> /dev/null