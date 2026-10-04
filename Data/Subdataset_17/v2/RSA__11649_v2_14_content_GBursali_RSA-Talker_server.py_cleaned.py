import socket
import threading
from Crypto.PublicKey import RSA
class Server:
    def __init__(self):
        self.PORT = 1423
        self.CODING = "ISO-8859-1"
        self.TEXTCODE = "UTF-8"
        self.sock = socket.socket()
        self.sock.bind(('', self.PORT))
        self.sock.listen()
        self.clients = []
        threading.Thread(target=self.accept_clients).start()
    def accept_clients(self):
        while True:
            conn, addr = self.sock.accept()
            client = Client(conn, addr)
            self.clients.append(client)
            print("Client connected.")
            threading.Thread(target=self.handle_client, args=(client,)).start()
    def handle_client(self, client):
        while True:
            data = self.receive_data(client.socket)
            if data == '':
                continue
            name, message = data.split(':', 1)
            message_bytes = message.encode(self.CODING)
            try:
                public_key = RSA.importKey(message_bytes)
                print("Public key received.")
                client.set_key(public_key, name)
            except Exception as e:
                print(f"Error importing key: {e}")
                self.broadcast_message(message_bytes, client, name)
    def broadcast_message(self, message, client, target_name=None):
        sender = self.get_client_by_name(target_name)
        if sender and sender.key:
            try:
                encrypted_message = sender.key.encrypt(self.encode_text(client.name) + b'->' + message, b'')[0]
                for user in self.clients:
                    if user.name != client.name:
                        user.send_data(encrypted_message)
            except Exception as e:
                print(f"Error sending data: {e}")
    def get_client_by_name(self, name):
        for client in self.clients:
            if client.name == name:
                return client
        return None
    def receive_data(self, connection):
        try:
            data = connection.recv(16384).decode(self.CODING)
            return data
        except Exception as e:
            print(f"Error receiving data: {e}")
            return ''
    def encode_text(self, text):
        try:
            return text.encode(self.TEXTCODE)
        except UnicodeEncodeError:
            return text.encode(self.CODING)
class Client:
    def __init__(self, connection, address):
        self.socket = connection
        self.key = None
        self.name = None
        self.address = address
    def set_key(self, key, name):
        if self.key is not None:
            return
        self.key = key
        self.name = name
    def send_data(self, data):
        try:
            self.socket.send(data)
        except Exception as e:
            print(f"Error sending data to client: {e}")
if __name__ == "__main__":
    server = Server()