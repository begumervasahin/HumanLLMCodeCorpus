from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import AES
MASTER_KEY = b'master key'
def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        print(f"Client {client_address[0]}:{client_address[1]} has connected.")
        send_encrypted_message(client, "Greetings from the server! Please type your name and press enter.")
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()
def handle_client(client):
    name = decrypt_message(client.recv(BUFSIZ)).decode("utf-8")
    welcome_msg = f"\nWelcome {name}! If you ever want to quit, type {{quit}} to exit."
    send_encrypted_message(client, welcome_msg)
    clients[client] = name
    while True:
        message = decrypt_message(client.recv(BUFSIZ)).decode("utf-8")
        if message != "{quit}":
            broadcast_message(message, name + ": ")
        else:
            close_client_connection(client)
            break
def broadcast_message(msg, prefix=""):
    encrypted_message = encrypt_message(prefix + msg)
    for sock in clients:
        sock.send(encrypted_message)
def send_encrypted_message(client, msg):
    encrypted_msg = encrypt_message(msg)
    client.send(encrypted_msg)
def encrypt_message(msg):
    return AES.encrypt(MASTER_KEY, msg.encode('UTF-8'))
def decrypt_message(msg):
    return AES.decrypt(MASTER_KEY, msg)
def close_client_connection(client):
    client.close()
    del clients[client]
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