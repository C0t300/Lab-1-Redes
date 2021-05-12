import socket as skt

serverAddr = "localhost"
serverPort = 50100

cSocket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)

enviar = "Hola123"
cSocket.sendto(enviar.encode(), (serverAddr, serverPort))

msg, addr = cSocket.recvfrom(2048)
print(msg.decode())
cSocket.close()