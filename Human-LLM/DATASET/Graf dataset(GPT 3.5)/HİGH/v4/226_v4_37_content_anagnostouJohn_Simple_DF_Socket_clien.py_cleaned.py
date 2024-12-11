import socket
import json
from diffiehellman.diffiehellman import DiffieHellman
def fonk1():
    b1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b1.settimeout(5)
    b2 = '192.168.168.184'
    a1 = 8201
    try:
        b1.connect((b2, a1))
    except socket.error as e:
        print("Error connecting to the server:", e)
        return
    b3 = DiffieHellman()
    b3.generate_public_key()
    b4 = {"b3": b3.public_key}
    b1.send(json.dumps(b4).encode("utf-8"))
    b5 = ""
    while True:
        try:
            b6 = b1.recv(100)
            if not b6:
                break
            b5 += b6.decode("utf-8")
        except socket.error as e:
            print("Error receiving b4 from the server:", e)
            break
    b7 = json.loads(b5)["alice"]
    b3.generate_shared_secret(b7, b8 = True)
    print("Shared Secret Key:", b3.shared_key)
    b1.close()
if b9 = = "__main__":
    fonk1()