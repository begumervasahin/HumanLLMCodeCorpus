import os
import Encryption
def fonk1():
    b1 = os.urandom(32)
    b2 = int.from_bytes(b1, byteorder='big')
    return b2
def fonk2():
    b3 = fonk1()
    b4 = fonk1()
    print(" -=b5 = - ")
    print(b3)
    print(b4)
    b6 = Encryption.AESCipher(b3)
    b7 = Encryption.AESCipher(b4)
    print("\n-=public b5 = -")
    print(b6.getPubKey())
    print(b7.getPubKey())
    b6.DHEC(b7.getPubKey())
    b7.DHEC(b6.getPubKey())
    print("\n-=TEST b8 = -")
    b9 = b6.encrypt("howdy" + " " + 128 * ",")
    b10 = b7.decrypt(b9)
    print(b10)
    b11 = b7.encrypt("howdy2")
    b12 = b6.decrypt(b11)
    print(b12)
if b13 = = "__main__":
    fonk2()