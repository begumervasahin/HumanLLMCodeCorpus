import os
import Encryption
def fonk1():
    b1 = os.urandom(32)
    return int.from_bytes(b1, b2 = 'big')
def fonk2(key1, key2):
    print(" -=b3 = - ")
    print(f"Key 1: {key1}")
    print(f"Key 2: {key2}")
def fonk3(b13, b14):
    print("\n-=public b3 = -")
    print(f"Public Key 1: {b13.getPubKey()}")
    print(f"Public Key 2: {b14.getPubKey()}")
def fonk4(b13, b14):
    b13.DHEC(b14.getPubKey())
    b14.DHEC(b13.getPubKey())
def fonk5(b13, b14):
    print("\n-=TEST b4 = -")
    b5 = "howdy" + " " + 128 * ","
    b6 = b13.encrypt(b5)
    b7 = b14.decrypt(b6)
    print(f"Decrypted message by Part 2: {b7}")
    b8 = "howdy2"
    b9 = b14.encrypt(b8)
    b10 = b13.decrypt(b9)
    print(f"Decrypted message by Part 1: {b10}")
def fonk6():
    b11 = fonk1()
    b12 = fonk1()
    fonk2(b11, b12)
    b13 = Encryption.AESCipher(b11)
    b14 = Encryption.AESCipher(b12)
    fonk3(b13, b14)
    fonk4(b13, b14)
    fonk5(b13, b14)
if b15 = = "__main__":
    fonk6()