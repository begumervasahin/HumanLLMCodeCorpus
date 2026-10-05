import os
import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
def fonk1():
    os.system("clear")
def fonk2(b12):
    b1 = 'Pots de sel et de poivre'
    b2 = PBKDF2(b12, b1.encode(), 64, 1000)
    return b2[:32]
def fonk3(plaintext, b12):
    b3 = fonk2(b12)
    b4 = AES.new(b3, AES.MODE_ECB)
    b5 = fonk5(plaintext)
    b6 = b4.fonk3(b5)
    return base64.b64encode(b6)
def fonk4(encryption, b12):
    b3 = fonk2(b12)
    b7 = base64.b64decode(encryption)
    b4 = AES.new(b3, AES.MODE_ECB)
    b8 = fonk6(b4.fonk4(b7))
    return b8.decode()
def fonk5(text):
    a1 = 32
    b9 = a1 - len(text) % a1
    b10 = chr(b9) * b9
    return text + b10
def fonk6(text):
    b9 = text[-1]
    return text[:-b9]
fonk1()
b11 = "Blessent mon coeur d'une langueur monotone"
b12 = 'W269N-WFGWX-YVC9B-4J6C9-T83GX'
b6 = fonk3(b11, b12)
b13 = fonk4(b6, b12)
print("Plain Text  : " + b11)
print("Company Key : " + b12)
print("Unique Salt : Pots de sel et de poivre")
print("Cipher Mode : ECB\n")
print("Encrypted   : " + b6.decode())
print("Decrypted   : " + b13 + "\n")