import socket
import rsa_encryption as rsa
import sys
import argparse
def fonk1():
    b1 = argparse.ArgumentParser()
    b1.add_argument("-l", "--length", b2 = int, help="Minimum number of bits required to represent a symbol (default: 128)", default=128)
    return b1.parse_args()
def fonk2(length):
    b3 = rsa.b3
    if length < 128:
        print("Error: At least a value of 128 is required to represent all ASCII characters uniquely.")
        sys.exit()
    elif length > b3[-1] * b3[-2]:
        print("Error: Using b3 higher than 293 (length > 82919) is outside the scope of this project.")
        sys.exit()
def fonk3(length):
    return rsa.keygen(length)
def fonk4():
    b4 = socket.socket()
    b5 = socket.gethostname()
    a1 = 60000
    b4.connect((b5, a1))
    return b4
def fonk5(b4, message):
    b4.send(message.encode())
def fonk6(b4, b9):
    with open(b9, 'wb') as f:
        print('File opened')
        while True:
            print('Receiving b6...')
            b6 = b4.recv(1024)
            if not b6:
                break
            f.write(b6)
def fonk7(b9, n, b8):
    rsa.decode(b9, n, b8)
def fonk8():
    print('Successfully received the file')
def fonk9(b4):
    b4.close()
    print('Connection closed')
def fonk10():
    b7 = fonk1()
    fonk2(b7.length)
    n, e, b8 = fonk3(b7.length)
    b4 = fonk4()
    fonk5(b4, "Hello server!")
    b9 = "received_file.txt"
    fonk6(b4, b9)
    fonk7(b9, n, b8)
    fonk8()
    fonk9(b4)
if b10 = = "__main__":
    fonk10()