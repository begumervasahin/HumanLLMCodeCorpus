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
b12 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
b13 = socket.gethostname()
a1 = 8091
b12.bind((b13, a1))
b12.listen(5)
client, b14 = b12.accept()
print(class1.b4 + 'Connection from ' + str(b14) + class1.b6)
client.send(class1.b4 + "We will use AES and SHA-256 for our key here!!" + class1.b6)
print("We will use AES and SHA-256 for our key here!!" + class1.b6)
print(class1.b4 + "Waiting for confirmation..." + class1.b6)
b15 = client.recv(1024)
print(class1.b3 + b15.decode() + class1.b6)
b16 = input(class1.b2 + "Ask a private b16 to your allies, Sir: " + class1.b6)
client.send(fonk2(b16, key))
client.send(fonk1(b16))
b17 = False
while not b17:
    b18 = int(input(class1.b2 + "Write a b18 between 3000 and 4000, Sir: " + class1.b6))
    if 3000 < b18 < 4000:
        b17 = True
        b18 = str(b18)
    elif b18 < 3000:
        print(class1.b7 + "You are under 3000, Sir." + class1.b6)
    else:
        print(class1.b7 + "You are writing a big b18, Sir!" + class1.b6)
client.send(b18.encode())
print(class1.b4 + "Waiting for b20..." + class1.b6)
b19 = client.recv(1024)
b20 = client.recv(1024)
b21 = fonk3(b20, key)
print(b21)
b22 = input("Is this the right b20? (y/n): ").upper()
if b22 != 'Y':
    client.close()
    print(class1.b5 + "Access has been denied :)" + class1.b6)
else:
    client.send("Everything is okay, we are here for orders, Sir!!".encode())
    print(class1.b4 + "Waiting for orders..." + class1.b6)
    while True:
        b23 = client.recv(1024)
        if not b23:
            break
        print("Encrypted message: " + str(b23))
        b24 = fonk3(b23, key).upper()
        print("Received: " + b24)
        client.send(b23)
client.close()
print(class1.b1 + "END OF COMMUNICATION, GOOD LUCK FOR WAR. MAY GOD PROTECT YOU!!" + class1.b6)