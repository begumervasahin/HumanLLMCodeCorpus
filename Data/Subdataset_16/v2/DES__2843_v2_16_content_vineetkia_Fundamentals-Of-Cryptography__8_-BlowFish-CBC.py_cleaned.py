from Crypto.Cipher import Blowfish
from struct import pack
def fonk1(b6, b7):
    b1 = Blowfish.new(b6, Blowfish.MODE_CBC)
    b2 = Blowfish.b2
    b3 = b2 - len(b7) % b2
    b4 = pack('b' * b3, *([b3] * b3))
    b5 = b1.iv + b1.encrypt(b7 + b4)
    return b5
def fonk2():
    b6 = b'An arbitrarily long b6'
    b7 = b'docendo discimus '
    b5 = fonk1(b6, b7)
    print("Encrypted message:", b5)
if b8 = = "__main__":
    fonk2()