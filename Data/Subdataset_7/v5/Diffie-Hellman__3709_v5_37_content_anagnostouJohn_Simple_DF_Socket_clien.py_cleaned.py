import socket
import json
from diffiehellman.diffiehellman import DiffieHellman
def fonk1(ip, port):
    try:
        b1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        b1.settimeout(5)
        b1.connect((ip, port))
        return b1
    except socket.error as e:
        print("Error connecting to the server:", e)
        return None
def fonk2(socket):
    b2 = ""
    try:
        while True:
            b3 = socket.recv(100)
            if not b3:
                break
            b2 += b3.decode("utf-8")
    except socket.error as e:
        print("Error receiving b6 from the server:", e)
    return b2
def fonk3():
    b4 = '192.168.168.184'
    a1 = 8201
    b1 = fonk1(b4, a1)
    if not b1:
        return
    b5 = DiffieHellman()
    b5.generate_public_key()
    b6 = {"b5": b5.public_key}
    b1.send(json.dumps(b6).encode("utf-8"))
    b2 = fonk2(b1)
    b7 = json.loads(b2)["alice"]
    b5.generate_shared_secret(b7, b8 = True)
    print("Shared Secret Key:", b5.shared_key)
    b1.close()
if b9 = = "__main__":
    fonk3()