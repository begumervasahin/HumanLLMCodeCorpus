import socket
import sys
import threading
b1 = '127.0.0.1'
a1 = 50007
a2 = 0
b2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    b2.bind((b1, a1))
except socket.error:
    print("The server encountered some problems.")
    sys.exit()
print('The server is on.')
print("Server is ready...")
b2.listen(2)
b3 = []
while a2 < 2:
    connexion, b4 = b2.accept()
    a2 += 1
    print("A client requested a connection, IP address: %s, port: %s" %
          (b4[0], b4[1]))
    b3.append([connexion, b4])
class class1(threading.Thread):
    def fonk1(self, b5, b7):
        threading.Thread.fonk1(self)
        self.b5 = b5[0]
        self.b6 = b5[1]
        self.b7 = b7[0]
        self.b8 = b7[1]
    def fonk2(self):
        while True:
            b9 = self.b5.recv(5000).decode("utf-8")
            self.b7.send(b9.encode("utf-8"))
b10 = class1(b3[0], b3[1])
b11 = class1(b3[1], b3[0])
b10.start()
b11.start()