from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import AES
key = b'master key'
def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        print(f"Client {client_address[0]}:{client_address[1]} has connected.")
        greeting = "Greetings from the server! Please type your name and press enter."
        encrypted_greeting = AES.encrypt(key, greeting.encode('UTF-8'))
        client.send(encrypted_greeting)
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()
def handle_client(client):
    name = AES.decrypt(key, client.recv(BUFSIZ)).decode("utf-8")
    welcome_msg = f"Welcome {name}! If you ever want to quit, type {{quit}} to exit."
    encrypted_welcome_msg = AES.encrypt(key, welcome_msg.encode('UTF-8'))
    client.send(encrypted_welcome_msg)
    clients[client] = name
    while True:
        message = AES.decrypt(key, client.recv(BUFSIZ)).decode("utf-8")
        if message != "{quit}":
            broadcast(message, name + ": ")
        else:
            client.close()
            del clients[client]
            if not clients:
                SERVER.close()
            break
def broadcast(msg, prefix=""):
    message = prefix + msg
    encrypted_message = AES.encrypt(key, message.encode('UTF-8'))
    for sock in clients:
        sock.send(encrypted_message)
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
    print("Waiting for connections...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()