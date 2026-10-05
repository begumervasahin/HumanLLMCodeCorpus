from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import AES
KEY = b'master key'
def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        message = "Greetings from the cave! Now type your name and press enter!"
        ciphertext = AES.encrypt(KEY, message.encode('UTF-8'))
        client.send(ciphertext)
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()
def handle_client(client):
    name = AES.decrypt(KEY, client.recv(BUFSIZ)).decode("utf-8")
    welcome = '\nWelcome %s! If you ever want to quit, type {quit} to exit.' % name
    ciphertext = AES.encrypt(KEY, welcome.encode('UTF-8'))
    client.send(ciphertext)
    clients[client] = name
    while True:
        message = AES.decrypt(KEY, client.recv(BUFSIZ)).decode("utf-8")
        if message != "{quit}":
            broadcast(message, name+": ")
        else:
            client.close()
            del clients[client]
            if not clients:
                SERVER.close()
            break
def broadcast(msg, prefix=""):
    message = prefix + msg
    ciphertext = AES.encrypt(KEY, message.encode('UTF-8'))
    for sock in clients:
        sock.send(ciphertext)
clients = {}
addresses = {}
HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)
if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()