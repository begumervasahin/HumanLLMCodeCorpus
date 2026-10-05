import socket
import sys
import threading
HOST = '127.0.0.1'
PORT = 50007
counter = 0
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print("The server encountered some problems.")
    sys.exit()
print('The server is on.')
print("Server is ready...")
mySocket.listen(2)
clients = []
while counter < 2:
    connexion, adresse = mySocket.accept()
    counter += 1
    print("A client requested a connection, IP address: %s, port: %s" %
          (adresse[0], adresse[1]))
    clients.append([connexion, adresse])
class Worker(threading.Thread):
    def __init__(self, client_from, client_to):
        threading.Thread.__init__(self)
        self.client_from = client_from[0]
        self.client_from_add = client_from[1]
        self.client_to = client_to[0]
        self.client_to_add = client_to[1]
    def run(self):
        while True:
            msgClient = self.client_from.recv(5000).decode("utf-8")
            self.client_to.send(msgClient.encode("utf-8"))
from_1_to_2 = Worker(clients[0], clients[1])
from_2_to_1 = Worker(clients[1], clients[0])
from_1_to_2.start()
from_2_to_1.start()