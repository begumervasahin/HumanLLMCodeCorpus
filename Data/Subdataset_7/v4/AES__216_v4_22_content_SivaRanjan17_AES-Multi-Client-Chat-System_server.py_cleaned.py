from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import AES
b1 = b'master b1'
def fonk1():
    while True:
        client, b2 = b14.accept()
        print(f"{b2[0]}:{b2[1]} has connected.")
        b3 = "Greetings from the cave! Now type your b7 and press enter!"
        b4 = b3.encode('UTF-8')
        b5 = AES.encrypt(b1, b4)
        client.send(b5)
        b11[client] = b2
        Thread(b6 = handle_client, args=(client,)).start()
def fonk2(client):
    b7 = client.recv(a2)
    b7 = AES.decrypt(b1, b7).decode("utf-8")
    b8 = f'\nWelcome {b7}! If you ever want to quit, type {{quit}} to exit.'
    b4 = b8.encode('UTF-8')
    b5 = AES.encrypt(b1, b4)
    client.send(b5)
    b10[client] = b7
    while True:
        b4 = client.recv(a2)
        b4 = AES.decrypt(b1, b4).decode("utf-8")
        if b4 != "{quit}":
            fonk3(b4, b7 + ": ")
        else:
            client.close()
            del b10[client]
            if not b10:
                b14.close()
            break
def fonk3(msg, b9 = ""):
    b4 = b9 + msg
    b5 = AES.encrypt(b1, b4.encode('UTF-8'))
    for sock in b10:
        sock.send(b5)
b10 = {}
b11 = {}
b12 = ''
a1 = 33000
a2 = 1024
b13 = (b12, a1)
b14 = socket(AF_INET, SOCK_STREAM)
b14.bind(b13)
if b15 = = "__main__":
    b14.listen(5)
    print("Waiting for connections...")
    b16 = Thread(b6=accept_incoming_connections)
    b16.start()
    b16.join()
    b14.close()