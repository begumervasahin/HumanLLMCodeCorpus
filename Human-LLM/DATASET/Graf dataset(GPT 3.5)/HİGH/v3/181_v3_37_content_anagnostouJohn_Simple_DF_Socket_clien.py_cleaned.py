import socket
import json
from diffiehellman.diffiehellman import DiffieHellman
def fonk1(b5, a1):
    b1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b1.settimeout(5)
    try:
        b1.connect((b5, a1))
    except socket.error as e:
        print("Error connecting to the server:", e)
        return None
    return b1
def fonk2(b1, b7):
    b2 = {"b6": b7}
    b1.send(json.dumps(b2).encode("utf-8"))
def fonk3(b1):
    b3 = ""
    while True:
        try:
            b4 = b1.recv(100)
            if not b4:
                break
            b3 += b4.decode("utf-8")
        except socket.error as e:
            print("Error receiving b2 from the server:", e)
            break
    return json.loads(b3)["alice"]
def fonk4():
    b5 = '192.168.168.184'
    a1 = 8201
    b1 = fonk1(b5, a1)
    if not b1:
        return
    b6 = DiffieHellman()
    b6.generate_public_key()
    b7 = b6.public_key
    fonk2(b1, b7)
    b8 = fonk3(b1)
    b6.generate_shared_secret(b8, b9 = True)
    print("Shared Secret Key:", b6.shared_key)
    b1.close()
if b10 = = "__main__":
    fonk4()