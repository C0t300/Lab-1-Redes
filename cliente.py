import socket as skt

serverAddr = "localhost"
serverPort = 50102
sCliente = skt.socket(skt.AF_INET, skt.SOCK_STREAM)

sCliente.connect((serverAddr, serverPort)) #Handshake

send = input("Que ingresar: ")
sCliente.send(send.encode())
response = sCliente.recv(2048).decode()
print(response)
sCliente.close()