import os
import base64
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
def fonk1():
    os.system("clear")
def fonk2():
    b1 = print(b1)
def fonk3(b14, b2 = 'Pots de sel et de poivre'):
    return PBKDF2(b14, b2, b3 = 32, count=1000)
def fonk4(data, b4 = 32):
    b5 = b4 - len(data) % b4
    b6 = chr(b5) * b5
    return data + b6.encode()
def fonk5(data):
    b5 = data[-1]
    return data[:-b5]
def fonk6(b13, b14):
    b7 = fonk3(b14)
    b8 = fonk4(b13.encode())
    b9 = Random.new().read(AES.b4)
    b10 = AES.new(b7, AES.MODE_CBC, b9)
    b11 = b9 + b10.fonk6(b8)
    return base64.b64encode(b11).decode()
def fonk7(b15, b14):
    b7 = fonk3(b14)
    b11 = base64.b64decode(b15)
    b9 = b11[:AES.b4]
    b10 = AES.new(b7, AES.MODE_CBC, b9)
    b12 = fonk5(b10.fonk7(b11[AES.b4:]))
    return b12.decode()
def fonk8():
    fonk1()
    fonk2()
    b13 = "Blessent mon coeur d'une langueur monotone"
    b14 = 'W269N-WFGWX-YVC9B-4J6C9-T83GX'
    print(f"Plain Text  : {b13}")
    print(f"Company Key : {b14}")
    print("Unique Salt : Pots de sel et de poivre")
    print(f"Private Key : {base64.b64encode(fonk3(b14)).decode()}")
    print("Cipher Mode : CBC\n")
    b15 = fonk6(b13, b14)
    b16 = fonk7(b15, b14)
    print(f"Encrypted   : {b15}")
    print(f"Decrypted   : {b16}\n")
if b17 = = "__main__":
    fonk8()