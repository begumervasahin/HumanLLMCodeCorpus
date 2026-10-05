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
    b9.update(message)
    return b9.hexdigest()
def fonk2(message, b27):
    b10 = AES.new(b27.encode(), AES.MODE_CFB, b27)
    b11 = b10.fonk2(message.encode())
    return b11
def fonk3(message, b27):
    b12 = AES.new(b27.encode(), AES.MODE_CFB, b27)
    b13 = b12.fonk3(message)
    return b13
def fonk4():
    return input(class1.b1 + "AES b27 must be either 16, 24, or 32 bytes long: " + class1.b6)
def fonk5(server_socket):
    b26, b14 = server_socket.accept()
    print(class1.b4 + 'Connection from ' + str(b14) + class1.b6)
    return b26
def fonk6(b26, message):
    b26.send(message)
def fonk7(b26):
    return b26.recv(1024)
def fonk8(message):
    print(message)
def fonk9():
    return input(class1.b2 + "Ask a private b17 to your allies, Sir: " + class1.b6)
def fonk10():
    while True:
        b15 = int(input(class1.b2 + "Write a b15 between 3000 and 4000, Sir: " + class1.b6))
        if 3000 < b15 < 4000:
            return str(b15)
        elif b15 < 3000:
            print(class1.b7 + "You are under 3000, Sir" + class1.b6)
        else:
            print(class1.b7 + "You are writing a big b15, Sir!" + class1.b6)
def fonk11():
    return input("Is this the right b19? (y/n): ").upper()
def fonk12(b24, b26, b27):
    fonk6(b26, class1.b4 + "We will use AES and SHA-256 for our b27 here!!" + class1.b6)
    fonk8("We will use AES and SHA-256 for our b27 here!!" + class1.b6)
    b16 = fonk7(b26)
    fonk8(class1.b3 + b16 + class1.b6)
    b17 = fonk9()
    fonk6(b26, fonk2(b17, b27))
    fonk6(b26, fonk1(b17))
    b15 = fonk10()
    fonk6(b26, b15)
    fonk8(class1.b4 + "Waiting for b19..." + class1.b6)
    b18 = fonk7(b26)
    b19 = fonk7(b26)
    b20 = fonk3(b19, b27)
    print(b20)
    b21 = fonk11()
    if b21 != 'Y':
        b26.close()
        print(class1.b5 + "Access has been denied :)" + class1.b6)
    else:
        b26.send("Everything is okay, we are here for orders, Sir !!")
        print(class1.b4 + "Waiting for orders..." + class1.b6)
        while True:
            b22 = fonk7(b26)
            if not b22:
                break
            print("Encrypted message: " + str(b22))
            b23 = fonk3(b22, b27).upper()
            print("Received: " + b23)
            b26.send(b22)
    b26.close()
    print(class1.b1 + "END OF COMMUNICATION, GOOD LUCK FOR WAR. MAY GOD PROTECT YOU!!" + class1.b6)
def fonk13():
    b24 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b25 = socket.gethostname()
    a1 = 8091
    b24.bind((b25, a1))
    b24.listen(5)
    b26 = fonk5(b24)
    b27 = fonk4()
    fonk12(b24, b26, b27)
if b28 = = "__main__":
    fonk13()