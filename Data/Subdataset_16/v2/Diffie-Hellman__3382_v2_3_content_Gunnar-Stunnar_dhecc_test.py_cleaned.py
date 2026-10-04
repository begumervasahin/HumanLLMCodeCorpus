import os
import Encryption
def fonk1():
    b1 = os.urandom(32)
    return int.from_bytes(b1, b2 = 'big')
def fonk2(key1, key2):
    print(" -=b3 = - ")
    print(key1)
    print(key2)
def fonk3(b11, b12):
    print("\n-=public b3 = -")
    print(b11.getPubKey())
    print(b12.getPubKey())
def fonk4(b11, b12):
    b11.DHEC(b12.getPubKey())
    b12.DHEC(b11.getPubKey())
def fonk5(b11, b12):
    print("\n-=TEST b4 = -")
    b5 = b11.encrypt("howdy" + " " + 128 * ",")
    b6 = b12.decrypt(b5)
    print(b6)
    b7 = b12.encrypt("howdy2")
    b8 = b11.decrypt(b7)
    print(b8)
def fonk6():
    b9 = fonk1()
    b10 = fonk1()
    fonk2(b9, b10)
    b11 = Encryption.AESCipher(b9)
    b12 = Encryption.AESCipher(b10)
    fonk3(b11, b12)
    fonk4(b11, b12)
    fonk5(b11, b12)
if b13 = = "__main__":
    fonk6()