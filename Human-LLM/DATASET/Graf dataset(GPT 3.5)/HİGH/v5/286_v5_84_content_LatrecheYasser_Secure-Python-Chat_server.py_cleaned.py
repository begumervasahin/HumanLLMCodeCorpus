import socket
import sys
import threading
b1 = '127.0.0.1'
a1 = 50007
a2 = 0
b2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    b2.bind((b1, a1))
except socket.error as e:
    print("Error:", e)
    sys.exit()
print('Server is running on {}:{}'.format(b1, a1))
print("Server is ready to accept connections...")
b2.listen(2)
b3 = []
while a2 < 2:
    client_conn, b4 = b2.accept()
    a2 += 1
    print("New client connected - IP: {}, Port: {}".format(b4[0], b4[1]))
    b3.append((client_conn, b4))
class class1(threading.Thread):
    def fonk1(self, sender, receiver):
        threading.Thread.fonk1(self)
        self.b5 = sender[0]
        self.b6 = sender[1]
        self.b7 = receiver[0]
        self.b8 = receiver[1]
    def fonk2(self):
        while True:
            b9 = self.b5.recv(5000).decode("utf-8")
            self.b7.send(b9.encode("utf-8"))
b10 = class1(b3[0], b3[1])
b11 = class1(b3[1], b3[0])
b10.start()
b11.start()