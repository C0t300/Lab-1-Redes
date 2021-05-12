import socket as skt

serverPort = 50102

sSocket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)

sSocket.bind(("", serverPort))

sSocket.listen(1)

print("Servidor TCP escuchando en ", serverPort)

cSocket, cAddr = sSocket.accept()
msg = cSocket.recv(2048).decode()

response = "Largo de msg es de" + str(len(msg)) + " y el msg es" + str(msg)
cSocket.send(response.encode())
cSocket.close()