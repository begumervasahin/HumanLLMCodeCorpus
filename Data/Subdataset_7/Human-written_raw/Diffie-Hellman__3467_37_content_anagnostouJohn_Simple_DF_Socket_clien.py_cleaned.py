
import socket
import select
import sys
import json
import time
from diffiehellman.diffiehellman import DiffieHellman
b1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
b1.settimeout(5)
b2 = '192.168.168.184'
a1 = 8201
b1.connect((b2, a1))
b3 = DiffieHellman()
b3.generate_public_key()
b4 = {"b3":b3.public_key}
b1.send(json.dumps(b4).encode("utf-8"))
b5 = ""
while True:
    try:
        b6 = ""
        b6 = b1.recv(100)
        while b6 is not "":
            b5+=b6.decode("utf-8")
            b6 = ""
            b6 = b1.recv(100)
        else:
            break
    except socket.error as ex:
        print(ex)
        break
b7 = json.loads(b5)
b3.generate_shared_secret(b7["alice"], b8 = True)
print(b3.shared_key)