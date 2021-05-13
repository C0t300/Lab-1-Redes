import socket as skt

serverAddr = "localhost"
serverPort = 50100
sCliente = skt.socket(skt.AF_INET, skt.SOCK_STREAM)

sCliente.connect((serverAddr, serverPort)) #Handshake

send = "start"
sCliente.send(send.encode())
print("start sent")
response = sCliente.recv(2048).decode()
print("response received", response)
flag = True
if response == "go":
    wins = 0
    ties = 0
    loses = 0
    while flag:
        send = input("Ingrese jugada: ")
        sCliente.send(send.encode())
        response = sCliente.recv(2048).decode()
        bot, resultado = response.split("|")
        print("El bot jugó", bot)
        if resultado == "win":
            print("Ganaste")
        elif resultado == "tie":
            print("Empataste")
        elif resultado == "lose":
            print("Perdiste")
        print("wins", wins)
        print("ties", ties)
        print("loses", loses)
        if wins >= 3:
            print("Ganaste")
            game = input("Desea jugar de nuevo? Y/N")
            if game == "N":
                flag = False
                sCliente.send("END".encode())
            else:
                wins = 0
                ties = 0
                loses = 0
else:
    print("El servidor no esta disponible.")
sCliente.close()