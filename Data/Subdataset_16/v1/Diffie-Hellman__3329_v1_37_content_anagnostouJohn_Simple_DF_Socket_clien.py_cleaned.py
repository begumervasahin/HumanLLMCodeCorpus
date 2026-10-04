
import socket
import json
from diffiehellman.diffiehellman import DiffieHellman
b1 = '192.168.168.184'
a1 = 8201
a2 = 5
a3 = 100
def fonk1(ip_address, port):
    b2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b2.settimeout(a2)
    b2.connect((ip_address, port))
    return b2
def fonk2(b2, public_key):
    b3 = json.dumps({"b6": public_key}).encode("utf-8")
    b2.send(b3)
def fonk3(b2):
    b4 = ""
    while True:
        try:
            b5 = b2.recv(a3).decode("utf-8")
            if b5:
                b4 += b5
            else:
                break
        except socket.error as ex:
            print(ex)
            break
    return b4
def fonk4():
    b2 = fonk1(b1, a1)
    b6 = DiffieHellman()
    b6.generate_public_key()
    fonk2(b2, b6.public_key)
    b4 = fonk3(b2)
    b7 = json.loads(b4)
    b6.generate_shared_secret(b7["alice"], b8 = True)
    print(b6.shared_key)
    b2.close()
if b9 = = '__main__':
    fonk4()