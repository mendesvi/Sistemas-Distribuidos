import os
import queue
import random
import socket
import sys
import threading
import time

IP = "127.0.0.1"


def criarServidor(porta, sendQueue, vizinho):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((IP, porta))
        s.listen()
        conn, addr = s.accept()
        enviar = threading.Thread(
            target=enviarMsg, args=(conn, sendQueue))
        enviar.start()
        while True:
            data = str(conn.recv(1024).decode())
            if data == "Exit" or not data:
                conn.close()
                os._exit(1)
            readQueue.put(vizinho+data)


def criarCliente(porta, sendQueue, vizinho):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((IP, porta))
        enviar = threading.Thread(
            target=enviarMsg, args=(s, sendQueue))
        enviar.start()
        while True:
            data = str(s.recv(1024).decode())
            if data == "Exit":
                s.close()
                os._exit(1)
            readQueue.put(vizinho+data)


def enviarMsg(socket, sendQueue):
    while True:
        mensagem = sendQueue.get()
        socket.sendall(mensagem.encode())
        if mensagem == "Exit":
            socket.close()
            os._exit(1)


readQueue = queue.Queue[str]()

sendQueue1 = queue.Queue[str]()
sendQueue2 = queue.Queue[str]()
sendQueue3 = queue.Queue[str]()
sendQueue4 = queue.Queue[str]()

enderecosEnvio = queue.Queue[socket.socket]()

id = sys.argv[1]

porta1 = 0
porta2 = 0
porta3 = 0
porta4 = 0

if id == 'A':
    porta1 = 50000
    porta2 = 50001
elif id == 'B':
    porta1 = 50002
    porta3 = 50000
elif id == 'C':
    porta1 = 50003
    porta3 = 50001
    porta4 = 50002
elif id == 'D':
    porta1 = 50004
    porta2 = 50005
    porta3 = 50003
elif id == 'E':
    porta1 = 50006
    porta2 = 50007
    porta3 = 50004
elif id == 'F':
    porta1 = 50008
    porta2 = 50009
    porta3 = 50006
elif id == 'G':
    porta1 = 50010
    porta2 = 50011
    porta3 = 50007
    porta4 = 50008
elif id == 'H':
    porta1 = 50012
    porta3 = 50005
    porta4 = 50010
elif id == 'I':
    porta1 = 50013
    porta3 = 50011
    porta4 = 50012
elif id == 'J':
    porta3 = 50009
    porta4 = 50013
