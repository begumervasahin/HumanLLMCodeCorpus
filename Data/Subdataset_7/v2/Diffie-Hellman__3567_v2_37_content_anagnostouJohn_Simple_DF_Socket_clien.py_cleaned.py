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
    b4 = b3.public_key
    b5 = {"b3": b4}
    b1.send(json.dumps(b5).encode("utf-8"))
    b6 = ""
    while True:
        try:
            b7 = b1.recv(100)
            if not b7:
                break
            b6 += b7.decode("utf-8")
        except socket.error as e:
            print("Error receiving b5 from the server:", e)
            break
    b8 = json.loads(b6)["alice"]
    b3.generate_shared_secret(b8, b9 = True)
    print("Shared Secret Key:", b3.shared_key)
    b1.close()
if b10 = = "__main__":
    fonk1()