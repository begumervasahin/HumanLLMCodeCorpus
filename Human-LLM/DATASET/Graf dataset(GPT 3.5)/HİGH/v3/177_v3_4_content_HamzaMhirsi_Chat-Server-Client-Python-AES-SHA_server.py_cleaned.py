import socket
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
class class1:
    b1 = '\033[95m'
    b2 = '\033[94m'
    b3 = '\033[92m'
    b4 = '\033[93m'
    b5 = '\033[91m'
    b6 = '\033[0m'
    b7 = '\033[1m'
    b8 = '\033[4m'
def fonk1(message):
    b9 = SHA256.new()
    b9.update(message.encode())
    return b9.hexdigest()
def fonk2(message, key):
    b10 = AES.new(key.encode(), AES.MODE_CFB, key.encode())
    return b10.fonk2(message.encode())
def fonk3(message, key):
    b10 = AES.new(key.encode(), AES.MODE_CFB, key.encode())
    b11 = b10.fonk3(message)
    return b11.decode()
def fonk4(server_socket):
    b16, b12 = server_socket.accept()
    print(class1.b4 + 'Connection from ' + str(b12) + class1.b6)
    return b16
def fonk5(b16, message):
    b16.send(message.encode())
def fonk6(b16):
    return b16.recv(1024)
def fonk7():
    return input(class1.b4 + "Waiting for confirmation..." + class1.b6)
def fonk8(prompt):
    return input(prompt)
def fonk9(message):
    print(message)
def fonk10(message):
    print("Encrypted message: " + str(message))
def fonk11(message):
    print("Received: " + message)
def fonk12(b20):
    return 3000 < b20 < 4000
def fonk13(b13):
    return b13 = = 'Y'
b14 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
b15 = socket.gethostname()
a1 = 8091
b14.bind((b15, a1))
b14.listen(5)
b16 = fonk4(b14)
fonk5(b16, class1.b4 + "We will use AES and SHA-256 for our key here!!" + class1.b6)
fonk9("We will use AES and SHA-256 for our key here!!" + class1.b6)
b17 = fonk6(b16)
fonk9(class1.b3 + b17.decode() + class1.b6)
b18 = fonk8(class1.b2 + "Ask a private b18 to your allies, Sir: " + class1.b6)
fonk5(b16, fonk2(b18, key))
fonk5(b16, fonk1(b18))
b19 = False
while not b19:
    b20 = int(fonk8(class1.b2 + "Write a b20 between 3000 and 4000, Sir: " + class1.b6))
    if fonk12(b20):
        b19 = True
        b20 = str(b20)
    elif b20 < 3000:
        print(class1.b7 + "You are under 3000, Sir." + class1.b6)
    else:
        print(class1.b7 + "You are writing a big b20, Sir!" + class1.b6)
fonk5(b16, b20)
fonk9(class1.b4 + "Waiting for b22..." + class1.b6)
b21 = fonk6(b16)
b22 = fonk6(b16)
b23 = fonk3(b22, key)
fonk11(b23)
b13 = fonk8("Is this the right b22? (y/n): ").upper()
if fonk13(b13):
    fonk5(b16, "Everything is okay, we are here for orders, Sir!!".encode())
    fonk9(class1.b4 + "Waiting for orders..." + class1.b6)
    while True:
        b24 = fonk6(b16)
        if not b24:
            break
        fonk10(b24)
        b25 = fonk3(b24, key).upper()
        fonk11(b25)
b16.close()
print(class1.b1 + "END OF COMMUNICATION, GOOD LUCK FOR WAR. MAY GOD PROTECT YOU!!" + class1.b6)