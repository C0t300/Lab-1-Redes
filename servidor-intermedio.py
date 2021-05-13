import socket as skt
import random

def startCachipun():

    serverAddr = "localhost"
    serverPort = 50102

    cSocket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
    print("iniciado socket con cachipun")

    enviar = "game"
    cSocket.sendto(enviar.encode(), (serverAddr, serverPort))
    print("enviado game")

    msg, addr = cSocket.recvfrom(2048)
    print("mensaje", msg.decode(), "recibido")
    if "OK" in msg.decode():
        ok, port = msg.decode().split("|")
        cSocket.close()
        return port
    cSocket.close()
    return False

def runCachipun(port):
    serverAddr = "localhost"
    serverPort = int(port)

    cSocket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)

    enviar = "play"
    cSocket.sendto(enviar.encode(), (serverAddr, serverPort))

    msg, addr = cSocket.recvfrom(2048)
    cSocket.close()
    return msg.decode()

def closeCachipun(port):
    serverAddr = "localhost"
    serverPort = int(port)

    cSocket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)

    enviar = "close"
    cSocket.sendto(enviar.encode(), (serverAddr, serverPort))
    return

def playCachipun(player, bot):
    if player == bot:
        return "tie", bot
    if player == "tijera":
        if bot == "piedra":
            return "lose", bot
        elif bot == "papel":
            return "win", bot
    elif player == "papel":
        if bot == "tijera":
            return "lose", bot
        elif bot == "piedra":
            return "win", bot
    elif player == "piedra":
        if bot == "papel":
            return "lose", bot
        elif bot == "tijera":
            return "win", bot

run = True
serverPort = 50100
while run:

    sSocketTCP = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
    sSocketTCP.bind(("", serverPort))
    sSocketTCP.listen(1)

    print("Servidor TCP escuchando en ", serverPort)

    cSocket, cAddr = sSocketTCP.accept()
    print("Conexion aceptada")
    msg = cSocket.recv(2048).decode()
    print("mensaje recibido: ", msg)

    if msg == "start":
        print("start iniciado")
        port = startCachipun()
        if port is not False:
            cSocket.send("go".encode())
            msg = cSocket.recv(2048).decode()
            while msg != "END":
                bot = runCachipun(port)
                win, bot = playCachipun(msg, bot)
                send = bot + "|" + win
                cSocket.send(send.encode())
                msg = cSocket.recv(2048).decode()
        else:
            cSocket.send("notGO".encode())

cSocket.close()