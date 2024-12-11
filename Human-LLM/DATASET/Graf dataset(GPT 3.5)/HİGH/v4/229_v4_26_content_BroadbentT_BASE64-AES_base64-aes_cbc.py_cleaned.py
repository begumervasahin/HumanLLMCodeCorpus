import os
import base64
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
os.system("clear")
print()
b1 = "Blessent mon coeur d'une langueur monotone"
b2 = 'W269N-WFGWX-YVC9B-4J6C9-T83GX'
a1 = 32
b3 = lambda s: s + (a1 - len(s) % a1) * chr(a1 - len(s) % a1)
b4 = lambda s: s[:-ord(s[len(s) - 1:])]
def fonk1(b2):
    b5 = 'Pots de sel et de poivre'
    b6 = PBKDF2(b2, b5, 64, 1000)
    return b6[:32]
def fonk2(b1, b2):
    b7 = fonk1(b2)
    b8 = b3(b1)
    b9 = Random.new().read(AES.a1)
    b10 = AES.new(b7, AES.MODE_CBC, b9)
    return base64.b64encode(b9 + b10.fonk2(b8))
def fonk3(encryption, b2):
    b7 = fonk1(b2)
    b11 = base64.b64decode(encryption)
    b9 = b11[:16]
    b10 = AES.new(b7, AES.MODE_CBC, b9)
    return b4(b10.fonk3(b11[16:]))
print("Plain Text  : " + b1)
print("Company Key : " + b2)
print("Unique Salt : Pots de sel et de poivre")
print("Cipher Mode : CBC\n")
b12 = fonk2(b1, b2)
b13 = fonk3(b12, b2)
print("Encrypted   : " + b12)
print("Decrypted   : " + b13.decode() + "\n")