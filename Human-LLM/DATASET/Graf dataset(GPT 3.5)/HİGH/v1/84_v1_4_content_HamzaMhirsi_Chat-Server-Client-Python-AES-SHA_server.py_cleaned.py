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
    b10 = b9.hexdigest()
    return b10
def fonk2(message, key):
    b11 = AES.new(key.encode(), AES.MODE_CFB, key.encode())
    b12 = b11.fonk2(message.encode())
    return b12
def fonk3(message, key):
    b13 = AES.new(key.encode(), AES.MODE_CFB, key.encode())
    b14 = b13.fonk3(message)
    return b14.decode()
b15 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
b16 = socket.gethostname()
a1 = 8091
b15.bind((b16, a1))
b15.listen(5)
client, b17 = b15.accept()
print(class1.b4 + 'Connection from ' + str(b17) + class1.b6)
client.send(class1.b4 + "We will use AES and SHA-256 for our key here!!" + class1.b6)
print("We will use AES and SHA-256 for our key here!!" + class1.b6)
print(class1.b4 + "Waiting for confirmation..." + class1.b6)
b18 = client.recv(1024)
print(class1.b3 + b18.decode() + class1.b6)
b19 = input(class1.b2 + "Ask a private b19 to your allies Sir: " + class1.b6)
client.send(fonk2(b19, key))
client.send(fonk1(b19))
b20 = False
while not b20:
    b21 = int(input(class1.b2 + "Write a number between 3000 and 4000 Sir: " + class1.b6))
    if 3000 < b21 < 4000:
        b20 = True
        b21 = str(b21)
    elif b21 < 3000:
        print(class1.b7 + "You are under 3000 Sir" + class1.b6)
    else:
        print(class1.b7 + "You are writing a big number Sir!!" + class1.b6)
client.send(b21.encode())
print(class1.b4 + "Waiting for answer..." + class1.b6)
b22 = client.recv(1024)
b23 = client.recv(1024)
b24 = fonk3(b23, key)
print(b24)
b25 = input("This is the right answer y/n: ").upper()
if b25 != 'Y':
    client.close()
    print(class1.b5 + "Access has been denied :)" + class1.b6)
else:
    client.send("Every think is okay, we are here for b27 Sir !!".encode())
    print(class1.b4 + "Waiting for orders..." + class1.b6)
    while True:
        b26 = client.recv(1024)
        if not b26:
            break
        print("Crypted message: " + str(b26))
        b27 = fonk3(b26, key).upper()
        print("Received: " + b27)
        client.send(b26)
client.close()
print(class1.b1 + "END OF COMMUNICATION, GOOD LUCK FOR WAR MAY GOD PROTECT YOU !!" + class1.b6)