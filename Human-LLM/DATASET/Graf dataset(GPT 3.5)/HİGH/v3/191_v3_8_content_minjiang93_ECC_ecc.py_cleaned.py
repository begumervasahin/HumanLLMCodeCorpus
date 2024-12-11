import logging
import collections
import random
import binascii
import sys
from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from flask import Flask
b1 = Flask(b44)
def fonk1(b39):
    b2 = ""
    while b39 > 0:
        b2 = chr(b39 & 0xFF) + b2
        b39 >>= 8
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
b9 = collections.namedtuple('b9', 'name b20 b38 b g b39 h')
b10 = {
    'secp256k1': {
        'b20': 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f,
        'b38': 0,
        'b': 7,
        'g': (0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
              0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8),
        'b39': 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141,
        'h': 1,
    }
}
def fonk5(b11, b20):
    if b11 = = 0:
        raise ZeroDivisionError('division by zero')
    if b11 < 0:
        return b20 - fonk5(-b11, b20)
    b2, b12 = 0, 1
    b17, b13 = 1, 0
    b16, b14 = b20, b11
    while b16 != 0:
        b15 = b14
        b14, b16 = b16, b14 - b15 * b16
        b12, b2 = b2, b12 - b15 * b2
        b13, b17 = b17, b13 - b15 * b17
    b19, x, b18 = b14, b12, b13
    assert b19 = = 1
    assert (b11 * x) % b20 = = 1
    return x % b20
def fonk6(point):
    if point is None:
        return True
    x, b18 = point
    b21 = b10['secp256k1']
    return (b18 * b18 - x * x * x - b21['b38'] * x - b21['b']) % b21['b20'] == 0
def fonk7(point):
    assert fonk6(point)
    if point is None:
        return None
    x, b18 = point
    b21 = b10['secp256k1']
    b22 = (x, -b18 % b21['b20'])
    assert fonk6(b22)
    return b22
def fonk8(point1, point2):
    assert fonk6(point1)
    assert fonk6(point2)
    if point1 is None:
        return point2
    if point2 is None:
        return point1
    b25, b23 = point1
    x2, b24 = point2
    b21 = b10['secp256k1']
    if b25 = = x2 and b23 != b24:
        return None
    if b25 = = x2:
        b26 = (3 * b25 * b25 + b21['b38']) * fonk5(2 * b23, b21['b20'])
    else:
        b26 = (b23 - b24) * fonk5(b25 - x2, b21['b20'])
    b27 = b26 * b26 - b25 - x2
    b28 = b23 + b26 * (b27 - b25)
    b22 = (b27 % b21['b20'], -b28 % b21['b20'])
    assert fonk6(b22)
    return b22
def fonk9(b11, point):
    assert fonk6(point)
    if b11 % b10['secp256k1']['b39'] == 0 or point is None:
        return None
    if b11 < 0:
        return fonk9(-b11, fonk7(point))
    b22 = None
    b29 = point
    while b11:
        if b11 & 1:
            b22 = fonk8(b22, b29)
        b29 = fonk8(b29, b29)
        b11 >>= 1
    assert fonk6(b22)
    return b22
def fonk10():
    b21 = b10['secp256k1']
    b30 = random.randrange(1, b21['b39'])
    b31 = fonk9(b30, b21['g'])
    return b30, b31
def fonk11(b31, b36, signature):
    b21 = b10['secp256k1']
    b32 = hash_message(b36)
    b16, b2 = signature
    b33 = fonk5(b2, b21['b39'])
    b34 = (b32 * b33) % b21['b39']
    b35 = (b16 * b33) % b21['b39']
    x, b18 = fonk8(fonk9(b34, b21['g']),
                     fonk9(b35, b31))
    if (b16 % b21['b39']) == (x % b21['b39']):
        return 'signature matches'
    else:
        return 'invalid signature'
@b1.route('/')
def fonk12():
    b36 = "Hello"
    b22 = ""
    if len(sys.argv) > 1:
        b36 = str(sys.argv[1])
    private, b37 = fonk10()
    b38 = "Private b5:", hex(private)
    b22 += str(b38)
    b22 += "\b39"
    b38 = "Public b5: (0x{:x}, 0x{:x})".format(*b37)
    b22 += b38
    b22 += "\b39"
    b22 += "\b39 = ========================\b39"
    b16 = 123456
    b22 += str(b37)
    b40 = fonk9(b16, b10['secp256k1']['g'])
    b41 = fonk9(b16, b37)
    b22 += "\b39 = =====Symmetric b5========\b39"
    b38 = "Encryption b5:", b41[0]
    b22 += str(b38)
    b22 += "\b39"
    b7 = class1(fonk1(b41[0])).fonk3(b36)
    b38 = "Encrypted:\b17", binascii.hexlify(b7)
    b22 += str(b38)
    b22 += "\b39"
    b42 = class1(fonk1(b41[0])).fonk4(b7)
    b38 = "Decrypted:  ", b42
    b22 += str(b38)
    b22 += "\b39"
    return b22, 200, {'Content-Type': 'b42/plain; b43 = utf-8'}
@b1.errorhandler(500)
def fonk13(e):
    logging.exception('An error occurred during b38 request.')
    return .format(e), 500
if b44 = = '__main__':
    b1.run(b45 = '0.0.0.0', debug=True)