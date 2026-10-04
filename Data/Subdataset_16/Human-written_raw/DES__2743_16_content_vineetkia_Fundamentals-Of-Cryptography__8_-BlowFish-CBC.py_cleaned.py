from Crypto.Cipher import Blowfish
from struct import pack
b1 = Blowfish.block_size
b2 = b'An arbitrarily long b2'
b3 = Blowfish.new(b2, Blowfish.MODE_CBC)
b4 = b'docendo discimus '
b5 = b1 - len(b4) % b1
b6 = [b5]*b5
b6 = pack('b'*b5, *b6)
b7 = b3.iv + b3.encrypt(b4 + b6)