
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import AES
b1 = b'master b1'
def fonk1():
    while True:
        client, b2 = b13.accept()
        print("%s:%s has connected." % b2)
        b3 = "Greetings from the cave! Now type your b6 and press enter!"
        b3 = b3.encode('UTF-8')
        b4 = AES.encrypt(b1, b3)
        client.send(b4)
        b10[client] = b2
        Thread(b5 = handle_client, args=(client,)).start()
def fonk2(client):
    b6 = client.recv(a2)
    b6 = AES.decrypt(b1, b6).decode("utf-8")
    b7 = '\nWelcome %s! If you ever want to quit, type {quit} to exit.' % b6
    b3 = b7.encode('UTF-8')
    b4 = AES.encrypt(b1, b3)
    client.send(b4)
    b9[client] = b6
    while True:
        b3 = client.recv(a2)
        b3 = AES.decrypt(b1, b3).decode("utf-8")
        if b3 != "{quit}":
            fonk3(b3, b6+": ")
        else:
            client.close()
            del b9[client]
            if bool(b9) == False:
                b13.close()
            break
def fonk3(msg, b8 = ""):
    b3 = b8 + msg
    b4 = AES.encrypt(b1, b3)
    for sock in b9:
        sock.send(b4)
b9 = {}
b10 = {}
b11 = ''
a1 = 33000
a2 = 1024
b12 = (b11, a1)
b13 = socket(AF_INET, SOCK_STREAM)
b13.bind(b12)
if b14 = = "__main__":
    b13.listen(5)
    print("Waiting for connection...")
    b15 = Thread(b5=accept_incoming_connections)
    b15.start()
    b15.join()
    b13.close()