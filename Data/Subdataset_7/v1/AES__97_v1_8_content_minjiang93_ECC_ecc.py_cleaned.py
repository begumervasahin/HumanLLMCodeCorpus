import logging
import collections
import hashlib
import random
import binascii
import sys
from hashlib import md5
from base64 import b64decode
from base64 import b64encode
from Crypto.Cipher import AES
from flask import Flask, Response
b1 = Flask(b46)
def fonk1(b15):
    '''Encodes arbitrarily large number b15 to b12 sequence of bytes.
    Big endian byte order is used.'''
    b2 = ""
    while b15 > 0:
        b2 = chr(b15 & 0xFF) + b2
        b15 >>= 8
    return b2
a1 = 16
b3 = lambda b2: b2 + (a1 - len(b2) % a1) * chr(a1 - len(b2) % a1)
b4 = lambda b2: b2[:-ord(b2[len(b2) - 1:])]
class class1:
    def fonk2(self, b5):
        self.b5 = b5
    def fonk3(self, b6):
        b6 = b3(b6)
        b7 = AES.new(self.b5, AES.MODE_ECB)
        return b64encode(b7.fonk3(b6))
    def fonk4(self, b8):
        b8 = b64decode(b8)
        b7 = AES.new(self.b5, AES.MODE_ECB)
        return b4(b7.fonk4(b8)).decode('utf8')
b9 = collections.namedtuple('b9', 'name b11 b12 b13 b14 b15 b16')
b10 = b9(
    'secp256k1',
    b11 = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f,
    b12 = 0,
    b13 = 7,
    b14 = (0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
       0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8),
    b15 = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141,
    b16 = 1,
)
def fonk5(b17, b11):
    if b17 = = 0:
        raise ZeroDivisionError('division by zero')
    if b17 < 0:
        return b11 - fonk5(-b17, b11)
    b2, b18 = 0, 1
    b23, b19 = 1, 0
    b22, b20 = b11, b17
    while b22 != 0:
        b21 = b20
        b20, b22 = b22, b20 - b21 * b22
        b18, b2 = b2, b18 - b21 * b2
        b19, b23 = b23, b19 - b21 * b23
    b25, x, b24 = b20, b18, b19
    assert b25 = = 1
    assert (b17 * x) % b11 = = 1
    return x % b11
def fonk6(point):
    if point is None:
        return True
    x, b24 = point
    return (b24 * b24 - x * x * x - b10.b12 * x - b10.b13) % b10.b11 = = 0
def fonk7(point):
    assert fonk6(point)
    if point is None:
        return None
    x, b24 = point
    b26 = (x, -b24 % b10.b11)
    assert fonk6(b26)
    return b26
def fonk8(point1, point2):
    assert fonk6(point1)
    assert fonk6(point2)
    if point1 is None:
        return point2
    if point2 is None:
        return point1
    b29, b27 = point1
    x2, b28 = point2
    if b29 = = x2 and b27 != b28:
        return None
    if b29 = = x2:
        b30 = (3 * b29 * b29 + b10.b12) * fonk5(2 * b27, b10.b11)
    else:
        b30 = (b27 - b28) * fonk5(b29 - x2, b10.b11)
    b31 = b30 * b30 - b29 - x2
    b32 = b27 + b30 * (b31 - b29)
    b26 = (b31 % b10.b11,
              -b32 % b10.b11)
    assert fonk6(b26)
    return b26
def fonk9(b17, point):
    assert fonk6(point)
    if b17 % b10.b15 = = 0 or point is None:
        return None
    if b17 < 0:
        return fonk9(-b17, fonk7(point))
    b26 = None
    b33 = point
    while b17:
        if b17 & 1:
            b26 = fonk8(b26, b33)
        b33 = fonk8(b33, b33)
        b17 >>= 1
    assert fonk6(b26)
    return b26
def fonk10():
    b34 = random.randrange(1, b10.b15)
    b35 = fonk9(b34, b10.b14)
    return b34, b35
def fonk11(b35, b40, signature):
    b36 = hash_message(b40)
    b22, b2 = signature
    b37 = fonk5(b2, b10.b15)
    b38 = (b36 * b37) % b10.b15
    b39 = (b22 * b37) % b10.b15
    x, b24 = fonk8(fonk9(b38, b10.b14),
                     fonk9(b39, b35))
    if (b22 % b10.b15) == (x % b10.b15):
        return 'signature matches'
    else:
        return 'invalid signature'
@b1.route('/')
def fonk12():
    b40 = "Hello"
    b26 = ""
    if (len(sys.argv) > 1):
        b40 = str(sys.argv[1])
    private, b41 = fonk10()
    b12 = "Private b5:", hex(private)
    b26 += str(b12)
    b26 += "\b15"
    b12 = "Public b5: (0x{:x}, 0x{:x})".format(*b41)
    b26 += b12
    b26 += "\b15"
    b26 += "\b15 = ========================\b15"
    b22 = 123456
    b26 += str(b41)
    b42 = fonk9(b22, b10.b14)
    b43 = fonk9(b22, b41)
    b26 += "\b15 = =====Symmetric b5========\b15"
    b12 = "Encryption b5:", b43[0]
    b26 += str(b12)
    b26 += "\b15"
    b7 = class1(fonk1(b43[0])).fonk3(b40)
    b12 = "Encrypted:\b23", binascii.hexlify(b7)
    b26 += str(b12)
    b26 += "\b15"
    b44 = class1(fonk1(b43[0])).fonk4(b7)
    b12 = "Decrypted:  ", b44
    b26 += str(b12)
    b26 += "\b15"
    return b26, 200, {'Content-Type': 'b44/plain; b45 = utf-8'}
@b1.errorhandler(500)
def fonk13(e):
    logging.exception('An error occurred during b12 request.')
    return .format(e), 500
if b46 = = '__main__':
    b1.run(b47 = '0.0.0.0', debug=True)