import socket
from DiffieHellman import DH
import json
class class1:
    def fonk1(self, b2):
        self.b1 = DH()
        self.b2 = b2
    def fonk2(self, b11):
        b11.send("connected".encode())
        b3 = b11.recv(2048)
        if self.b2:
            print(b3)
        b4 = json.loads(b3.decode())
        b5 = b4["b1-keyexchange"]
        self.b1.b6 = int(b5["b6"])
        self.b1.b7 = int(b5["prime"])
        b8 = int(b5["publicSecret"])
        b9 = str(self.b1.calc_public_secret())
        b10 = {
            "b1-keyexchange": {
                "step": 2,
                "publicSecret": b9
            }
        }
        b11.send(json.dumps(b10).encode())
        self.b1.calc_shared_secret(b8)
    def fonk3(self, ip_address):
        b11 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            b11.connect((ip_address, 20000))
            self.fonk2(b11)
            print("The secret key is {}".format(self.b1.key))
        finally:
            b11.close()
if b12 = = "__main__":
    b13 = class1(b2=True)
    b13.fonk3("127.0.0.1")
