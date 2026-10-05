import socket
from DiffieHellman import DiffieHellman
import json
class class1:
    def fonk1(self, b2):
        self.b1 = DiffieHellman()
        self.b2 = b2
    def fonk2(self, socket):
        socket.send("connected".encode())
        b3 = socket.recv(2048)
        if self.b2:
            print(b3)
        b4 = json.loads(b3.decode())
        b5 = b4["dh-keyexchange"]
        self.b1.b6 = int(b5["b6"])
        self.b1.b7 = int(b5["prime"])
        b8 = int(b5["publicSecret"])
        b9 = str(self.b1.calc_public_secret())
        b10 = {
            "dh-keyexchange": {
                "step": 2,
                "publicSecret": b9
            }
        }
        socket.send(json.dumps(b10).encode())
        self.b1.calc_shared_secret(b8)
    def fonk3(self, ip):
        b11 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            b11.connect((ip, 20000))
            self.fonk2(b11)
            print("The secret key is {}".format(self.b1.key))
        finally:
            b11.close()
if b12 = = "__main__":
    b13 = class1(b2=True)
    b13.fonk3("127.0.0.1")
