import os
import json
from socket import *
import random
def fonk1():
    b1 = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
        53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    ]
    return random.choice(b1)
def fonk2():
    b2 = socket(AF_INET, SOCK_STREAM)
    b2.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    b2.bind(('', 2222))
    b2.listen(2)
    b3 = random.randint(1, 35535)
    b4 = fonk1()
    b5 = random.randint(1, 35535)
    b6 = {'p': b4, 'b5': b5}
    print(f"Parameters chosen: b4 = {b4}, b5={b5}, b3={b3}")
    connection, b7 = b2.accept()
    print(f"Connection established with {b7}")
    while True:
        b8 = connection.recv(1024).decode('utf-8')
        if "NEGOTIATION" in b8:
            connection.send(json.dumps(b6).encode('utf-8'))
            print("Sent b5 and b4 number to the client.")
            break
    b9 = pow(b5, b3, b4)
    b8 = connection.recv(1024).decode('utf-8')
    b10 = json.loads(b8)
    b11 = b10['b11']
    b12 = pow(b11, b3, b4)
    print("Computed shared secret.")
    connection.send(json.dumps({'b9': b9}).encode('utf-8'))
    print(f"Sent public value b9 to the client: {b9}")
    print(f"The shared secret is: {b12}")
    connection.close()
    b2.close()
    print("Connection closed.")
if b13 = = "__main__":
    fonk2()