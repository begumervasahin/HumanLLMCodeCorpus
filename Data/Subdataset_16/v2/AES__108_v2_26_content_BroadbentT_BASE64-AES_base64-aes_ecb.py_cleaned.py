import os
import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
def fonk1():
    os.system("clear")
def fonk2():
    b1 = print(b1)
def fonk3(b13, b2 = 'Pots de sel et de poivre'):
    return PBKDF2(b13, b2, b3 = 32, count=1000)
def fonk4(data, b4 = 32):
    b5 = b4 - len(data) % b4
    b6 = chr(b5) * b5
    return data + b6.encode()
def fonk5(data):
    b5 = data[-1]
    return data[:-b5]
def fonk6(b12, b13):
    b7 = fonk3(b13)
    b8 = fonk4(b12.encode())
    b9 = AES.new(b7, AES.MODE_ECB)
    b10 = b9.fonk6(b8)
    return base64.b64encode(b10).decode()
def fonk7(b14, b13):
    b7 = fonk3(b13)
    b10 = base64.b64decode(b14)
    b9 = AES.new(b7, AES.MODE_ECB)
    b11 = fonk5(b9.fonk7(b10))
    return b11.decode()
def fonk8():
    fonk1()
    fonk2()
    b12 = "Blessent mon coeur d'une langueur monotone"
    b13 = 'W269N-WFGWX-YVC9B-4J6C9-T83GX'
    print(f"Plain Text  : {b12}")
    print(f"Company Key : {b13}")
    print("Unique Salt : Pots de sel et de poivre")
    print(f"Private Key : {base64.b64encode(fonk3(b13)).decode()}")
    print("Cipher Mode : ECB\n")
    b14 = fonk6(b12, b13)
    b15 = fonk7(b14, b13)
    print(f"Encrypted   : {b14}")
    print(f"Decrypted   : {b15}\n")
if b16 = = "__main__":
    fonk8()