import socket
import rsa_encryption as rsa
import sys
import argparse
def fonk1():
    b1 = argparse.ArgumentParser(description="Client for securely receiving a file via RSA encryption.")
    b1.add_argument("-l", "--length", b2 = int, default=128,
                        b3 = "Minimum length required to represent a symbol (default: 128)")
    return b1.parse_args()
def fonk2(b6):
    b4 = rsa.b4
    if b6.length < 128:
        print("Error: The minimum value of 128 is required to represent all ASCII characters uniquely.")
        sys.exit()
    elif b6.length > b4[-1] * b4[-2]:
        print("Error: Using b4 higher than 293 (length > 82919) is outside the scope of this project.")
        sys.exit()
def fonk3(b8, b10):
    with open(b10, 'wb') as f:
        print('File opened')
        while True:
            print('Receiving b5...')
            b5 = b8.recv(1024)
            if not b5:
                break
            f.write(b5)
    print('File received successfully')
def fonk4(b10, n, b7):
    rsa.decode(b10, n, b7)
    print('File decrypted successfully')
def fonk5():
    b6 = fonk1()
    fonk2(b6)
    n, e, b7 = rsa.keygen(b6.length)
    b8 = socket.socket()
    b9 = socket.gethostname()
    a1 = 60000
    b8.connect((b9, a1))
    b8.send(b"Hello server!")
    b10 = "received_file.txt"
    fonk3(b8, b10)
    fonk4(b10, n, b7)
    b8.close()
    print('Connection closed')
if b11 = = "__main__":
    fonk5()