import logging
import collections
import random
import binascii
import sys
from hashlib import md5
from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from flask import Flask
b1 = Flask(b47)
def fonk1(b15):
    b2 = ""
    while b15 > 0:
        b2 = chr(b15 & 0xFF) + b2
        b15 >>= 8
    return b2
a1 = 16
b3 = lambda b23: b23 + (a1 - len(b23) % a1) * chr(a1 - len(b23) % a1)
b4 = lambda b23: b23[:-ord(b23[len(b23) - 1:])]
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
    b23, b18 = 0, 1
    b24, b19 = 1, 0
    b22, b20 = b11, b17
    while b22 != 0:
        b21 = b20
        b20, b22 = b22, b20 - b21 * b22
        b18, b23 = b23, b18 - b21 * b23
        b19, b24 = b24, b19 - b21 * b24
    b26, x, b25 = b20, b18, b19
    assert b26 = = 1
    assert (b17 * x) % b11 = = 1
    return x % b11
def fonk6(point):
    if point is None:
        return True
    x, b25 = point
    return (b25 * b25 - x * x * x - b10.b12 * x - b10.b13) % b10.b11 = = 0
def fonk7(point):
    assert fonk6(point)
    if point is None:
        return None
    x, b25 = point
    b27 = (x, -b25 % b10.b11)
    assert fonk6(b27)
    return b27
def fonk8(point1, point2):
    assert fonk6(point1)
    assert fonk6(point2)
    if point1 is None:
        return point2
    if point2 is None:
        return point1
    b30, b28 = point1
    x2, b29 = point2
    if b30 = = x2 and b28 != b29:
        return None
    if b30 = = x2:
        b31 = (3 * b30 * b30 + b10.b12) * fonk5(2 * b28, b10.b11)
    else:
        b31 = (b28 - b29) * fonk5(b30 - x2, b10.b11)
    b32 = b31 * b31 - b30 - x2
    b33 = b28 + b31 * (b32 - b30)
    b27 = (b32 % b10.b11, -b33 % b10.b11)
    assert fonk6(b27)
    return b27
def fonk9(b17, point):
    assert fonk6(point)
    if b17 % b10.b15 = = 0 or point is None:
        return None
    if b17 < 0:
        return fonk9(-b17, fonk7(point))
    b27 = None
    b34 = point
    while b17:
        if b17 & 1:
            b27 = fonk8(b27, b34)
        b34 = fonk8(b34, b34)
        b17 >>= 1
    assert fonk6(b27)
    return b27
def fonk10():
    b35 = random.randrange(1, b10.b15)
    b36 = fonk9(b35, b10.b14)
    return b35, b36
def fonk11(b36, b41, signature):
    b37 = hash_message(b41)
    b22, b23 = signature
    b38 = fonk5(b23, b10.b15)
    b39 = (b37 * b38) % b10.b15
    b40 = (b22 * b38) % b10.b15
    x, b25 = fonk8(fonk9(b39, b10.b14),
                     fonk9(b40, b36))
    if (b22 % b10.b15) == (x % b10.b15):
        return 'signature matches'
    else:
        return 'invalid signature'
@b1.route('/')
def fonk12():
    b41 = "Hello"
    b27 = ""
    if len(sys.argv) > 1:
        b41 = str(sys.argv[1])
    private, b42 = fonk10()
    b27 += f"Private b5: {hex(private)}\b15"
    b27 += f"Public b5: (0x{b42[0]:x}, 0x{b42[1]:x})\b15\b15"
    b27 += "=========================\b15"
    b27 += str(b42) + "\b15"
    b22 = 123456
    b43 = fonk9(b22, b10.b14)
    b44 = fonk9(b22, b42)
    b27 += "======Symmetric b5 = =======\b15"
    b27 += f"Encryption b5: {b44[0]}\b15"
    b7 = class1(fonk1(b44[0])).fonk3(b41)
    b27 += f"Encrypted: {binascii.hexlify(b7)}\b15"
    b45 = class1(fonk1(b44[0])).fonk4(b7)
    b27 += f"Decrypted: {b45}\b15"
    return b27, 200, {'Content-Type': 'b45/plain; b46 = utf-8'}
@b1.errorhandler(500)
def fonk13(e):
    logging.exception('An error occurred during b12 request.')
    return .format(e), 500
if b47 = = '__main__':
    b1.run(b48 = '0.0.0.0', debug=True)