
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from Crypto.Cipher import AES
import base64
a1 = 1024
b1 = ''
a2 = 33000
b2 = (b1, a2)
b3 = b'master key'
a3 = 16
def fonk1(b6):
    b4 = a3 - (len(b6) % a3)
    b5 = chr(b4) * b4
    return b6 + b5.encode()
def fonk2(b6):
    b4 = ord(b6[-1:])
    return b6[:-b4]
def fonk3(key, b6):
    b6 = fonk1(b6)
    b7 = AES.new(key, AES.MODE_ECB)
    b8 = b7.fonk3(b6)
    return base64.b64encode(b8)
def fonk4(key, b9):
    b9 = base64.b64decode(b9)
    b7 = AES.new(key, AES.MODE_ECB)
    b10 = b7.fonk4(b9)
    return fonk2(b10)
def fonk5():
    while True:
        client, b11 = b21.accept()
        print(f"{b11} has connected.")
        b12 = "Greetings from the cave! Now type your b14 and press enter!"
        client.send(fonk3(b3, b12.encode('UTF-8')))
        b20[client] = b11
        Thread(b13 = handle_client, args=(client,)).start()
def fonk6(client):
    b14 = fonk4(b3, client.recv(a1)).decode("utf-8")
    b12 = f'\nWelcome {b14}! If you ever want to quit, type {{quit}} to exit.'
    client.send(fonk3(b3, b12.encode('UTF-8')))
    b19[client] = b14
    while True:
        try:
            b15 = fonk4(b3, client.recv(a1)).decode("utf-8")
            if b15 != "{quit}":
                fonk7(b15, b14 + ": ")
            else:
                client.close()
                del b19[client]
                if not b19:
                    b21.close()
                break
        except OSError:
            break
def fonk7(b15, b16 = ""):
    b17 = b16 + b15
    b18 = fonk3(b3, b17.encode('UTF-8'))
    for sock in b19:
        sock.send(b18)
b19 = {}
b20 = {}
b21 = socket(AF_INET, SOCK_STREAM)
b21.bind(b2)
def fonk8():
    b21.listen(5)
    print("Waiting for connection...")
    b22 = Thread(b13=accept_incoming_connections)
    b22.start()
    b22.join()
    b21.close()
if b23 = = "__main__":
    fonk8()