from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import AES
b1 = b'master key'
def fonk1():
    while True:
        client, b2 = b14.accept()
        print(f"Client {b2[0]}:{b2[1]} has connected.")
        fonk4(client, "Greetings from the server! Please type your b4 and press enter.")
        b11[client] = b2
        Thread(b3 = handle_client, args=(client,)).start()
def fonk2(client):
    b4 = fonk6(client.recv(a2)).decode("utf-8")
    b5 = f"\nWelcome {b4}! If you ever want to quit, type {{quit}} to exit."
    fonk4(client, b5)
    b10[client] = b4
    while True:
        b6 = fonk6(client.recv(a2)).decode("utf-8")
        if b6 != "{quit}":
            fonk3(b6, b4 + ": ")
        else:
            fonk7(client)
            break
def fonk3(msg, b7 = ""):
    b8 = fonk5(b7 + msg)
    for sock in b10:
        sock.send(b8)
def fonk4(client, msg):
    b9 = fonk5(msg)
    client.send(b9)
def fonk5(msg):
    return AES.encrypt(b1, msg.encode('UTF-8'))
def fonk6(msg):
    return AES.decrypt(b1, msg)
def fonk7(client):
    client.close()
    del b10[client]
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
    b16 = Thread(b3=accept_incoming_connections)
    b16.start()
    b16.join()
    b14.close()