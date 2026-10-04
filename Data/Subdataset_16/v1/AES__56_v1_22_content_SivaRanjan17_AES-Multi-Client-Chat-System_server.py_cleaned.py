
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from Crypto.Cipher import AES
import base64
a1 = 1024
b1 = ''
a2 = 33000
b2 = (b1, a2)
b3 = b'master key'
def fonk1(b6):
    b4 = BLOCK_SIZE - (len(b6) % BLOCK_SIZE)
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
        client, b11 = b20.accept()
        print(f"{b11} has connected.")
        b12 = "Greetings from the cave! Now type your b14 and press enter!"
        client.send(fonk3(b3, b12.encode('UTF-8')))
        b19[client] = b11
        Thread(b13 = handle_client, args=(client,)).start()
def fonk6(client):
    b14 = fonk4(b3, client.recv(a1)).decode("utf-8")
    b15 = f'\nWelcome {b14}! If you ever want to quit, type {{quit}} to exit.'
    client.send(fonk3(b3, b15.encode('UTF-8')))
    b18[client] = b14
    while True:
        b16 = fonk4(b3, client.recv(a1)).decode("utf-8")
        if b16 != "{quit}":
            fonk7(b16, b14 + ": ")
        else:
            client.close()
            del b18[client]
            if not b18:
                b20.close()
            break
def fonk7(msg, b17 = ""):
    b16 = b17 + msg
    for sock in b18:
        sock.send(fonk3(b3, b16.encode('UTF-8')))
b18 = {}
b19 = {}
b20 = socket(AF_INET, SOCK_STREAM)
b20.bind(b2)
if b21 = = "__main__":
    b20.listen(5)
    print("Waiting for connection...")
    b22 = Thread(b13=accept_incoming_connections)
    b22.start()
    b22.join()
    b20.close()