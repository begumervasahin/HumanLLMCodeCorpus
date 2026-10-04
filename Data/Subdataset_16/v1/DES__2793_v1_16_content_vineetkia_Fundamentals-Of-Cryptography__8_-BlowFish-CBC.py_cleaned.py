from Crypto.Cipher import Blowfish
from struct import pack
def fonk1(b7, b8):
    b1 = Blowfish.new(b7, Blowfish.MODE_CBC)
    b2 = Blowfish.block_size
    b3 = b2 - len(b8) % b2
    b4 = [b3] * b3
    b4 = pack('b' * b3, *b4)
    b5 = b1.iv + b1.encrypt(b8 + b4)
    return b5
if b6 = = "__main__":
    b7 = b'An arbitrarily long b7'
    b8 = b'docendo discimus '
    b5 = fonk1(b7, b8)
    print("Encrypted message:", b5)