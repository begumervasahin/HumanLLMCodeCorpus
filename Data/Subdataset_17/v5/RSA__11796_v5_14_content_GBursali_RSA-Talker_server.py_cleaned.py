import socket
import threading
from Crypto.PublicKey import RSA
class Server:
    def __init__(self, port=1423, public_text="Baglandi.", coding="ISO-8859-1", textcode="UTF-8"):
        self.PORT = port
        self.PUBLIC_TEXT = public_text
        self.CODING = coding
        self.TEXTCODE = textcode
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
            print("KullanÄ±cÄ± katÄ±ldÄ±.")
            threading.Thread(target=self.listen_to_client, args=(client,)).start()
    def listen_to_client(self, client):
        while True:
            data = self.receive_data(client.socket)
            if not data:
                continue
            name, key_data = self.parse_data(data)
            if key_data:
                try:
                    public_key = RSA.importKey(key_data)
                    print("Public Key AlÄ±ndÄ±...")
                    client.set_key(public_key, name)
                except ValueError:
                    self.broadcast(key_data, client, name)
    def parse_data(self, data):
        parts = data.split(':')
        name = parts[0]
        key_data = ':'.join(parts[1:]).encode(self.CODING)
        return name, key_data
    def receive_data(self, connection):
        return connection.recv(16384).decode(self.CODING)
    def broadcast(self, data, client, target=None):
        sender = self.get_client_by_name(target)
        encrypted_data = sender.key.encrypt(self.encode_text(client.name) + b'->' + data, b'')[0]
        for user in self.clients:
            if user.name != client.name:
                user.send(encrypted_data)
    def get_client_by_name(self, name):
        for client in self.clients:
            if client.name == name:
                return client
        return None
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
        if self.key is None:
            self.key = key
            self.name = name
    def send(self, data):
        self.socket.send(data)
if __name__ == "__main__":
    server = Server()