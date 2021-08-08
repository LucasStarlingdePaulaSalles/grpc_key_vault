# Grpc key vault
Implementation for second practical work of Fundamentos de Sistemas Paralelos e Distribuidos, ministered by professor Dorgival.
Departamento de Ciência da Computação, Universidade Federal de Minas Gerais.
Lucas Starling de Paula Salles, 2016006697

This project has two parts to it, the vault service and the compound service. 

## Vault service
Simple grpc client server pair this service is a simple key vault application. The service stores a string and integer pair as the value associated with an integer key. The developed methods are quite simple, `insert` receives a key-value pair and stores it if the key is available or an error if the key in unavailable. The `consult` method receives a key and returns the value associated with it, if it exists, and an error if it doesn't. Finally, `terminate` cleses the server's execution. The error values are numerical values specified by the project's descryption. This storage on this service was a simple python dictionary, since it wasn't specifyed that the memory needed to be permanent.
The client for this service is a simple cli that implements the commands as described.

## Compound service
A grpc application that connects to two Vault services via grpc stubs. This application has only two methods, `consult` and `terminate` which behave much like the ones from the Vault service. The `consult` method fetches information from both the vault services the Compound server is connected to, and returns it as specifyed. The `terminate` procedure closes down the Vault services and the Compound service.
The client for this service is also a simple implementation of the specification. Output happens as described.

