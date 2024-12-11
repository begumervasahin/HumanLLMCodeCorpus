from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import AES
b1 = b'master b1'
def fonk1():
    while True:
        client, b2 = b16.accept()
        print(f"Client {b2[0]}:{b2[1]} has connected.")
        b3 = "Greetings from the server! Please type your b6 and press enter."
        b4 = AES.encrypt(b1, b3.encode('UTF-8'))
        client.send(b4)
        b13[client] = b2
        Thread(b5 = handle_client, args=(client,)).start()
def fonk2(client):
    b6 = AES.decrypt(b1, client.recv(a2)).decode("utf-8")
    b7 = f"Welcome {b6}! If you ever want to quit, type {{quit}} to exit."
    b8 = AES.encrypt(b1, b7.encode('UTF-8'))
    client.send(b8)
    b12[client] = b6
    while True:
        b9 = AES.decrypt(b1, client.recv(a2)).decode("utf-8")
        if b9 != "{quit}":
            fonk3(b9, b6 + ": ")
        else:
            client.close()
            del b12[client]
            if not b12:
                b16.close()
            break
def fonk3(msg, b10 = ""):
    b9 = b10 + msg
    b11 = AES.encrypt(b1, b9.encode('UTF-8'))
    for sock in b12:
        sock.send(b11)
b12 = {}
b13 = {}
b14 = ''
a1 = 33000
a2 = 1024
b15 = (b14, a1)
b16 = socket(AF_INET, SOCK_STREAM)
b16.bind(b15)
if b17 = = "__main__":
    b16.listen(5)
    print("Waiting for connections...")
    b18 = Thread(b5=accept_incoming_connections)
    b18.start()
    b18.join()
    b16.close()