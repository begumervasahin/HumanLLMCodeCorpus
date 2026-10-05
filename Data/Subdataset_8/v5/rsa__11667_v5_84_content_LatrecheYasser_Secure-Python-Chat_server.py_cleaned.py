import socket
import sys
import threading
HOST = '127.0.0.1'
PORT = 50007
client_count = 0
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server_socket.bind((HOST, PORT))
except socket.error as e:
    print("Error:", e)
    sys.exit()
print('Server is running on {}:{}'.format(HOST, PORT))
print("Server is ready to accept connections...")
server_socket.listen(2)
clients = []
while client_count < 2:
    client_conn, client_addr = server_socket.accept()
    client_count += 1
    print("New client connected - IP: {}, Port: {}".format(client_addr[0], client_addr[1]))
    clients.append((client_conn, client_addr))
class ClientHandler(threading.Thread):
    def __init__(self, sender, receiver):
        threading.Thread.__init__(self)
        self.sender_conn = sender[0]
        self.sender_addr = sender[1]
        self.receiver_conn = receiver[0]
        self.receiver_addr = receiver[1]
    def run(self):
        while True:
            message = self.sender_conn.recv(5000).decode("utf-8")
            self.receiver_conn.send(message.encode("utf-8"))
client1_to_client2 = ClientHandler(clients[0], clients[1])
client2_to_client1 = ClientHandler(clients[1], clients[0])
client1_to_client2.start()
client2_to_client1.start()