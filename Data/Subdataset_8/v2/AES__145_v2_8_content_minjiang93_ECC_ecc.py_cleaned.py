import logging
import collections
import hashlib
import random
import binascii
import sys
from hashlib import md5
from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from flask import Flask
app = Flask(__name__)
def enc_long(n):
    s = ""
    while n > 0:
        s = chr(n & 0xFF) + s
        n >>= 8
    return s
BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
class AESCipher:
    def __init__(self, key):
        self.key = key
    def encrypt(self, raw):
        raw = pad(raw)
        cipher = AES.new(self.key, AES.MODE_ECB)
        return b64encode(cipher.encrypt(raw))
    def decrypt(self, enc):
        enc = b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_ECB)
        return unpad(cipher.decrypt(enc)).decode('utf8')
EllipticCurve = collections.namedtuple('EllipticCurve', 'name p a b g n h')
curve = EllipticCurve(
    'secp256k1',
    p=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f,
    a=0,
    b=7,
    g=(0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
       0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8),
    n=0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141,
    h=1,
)
def inverse_mod(k, p):
    if k == 0:
        raise ZeroDivisionError('division by zero')
    if k < 0:
        return p - inverse_mod(-k, p)
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = p, k
    while r != 0:
        quotient = old_r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    gcd, x, y = old_r, old_s, old_t
    assert gcd == 1
    assert (k * x) % p == 1
    return x % p
def is_on_curve(point):
    if point is None:
        return True
    x, y = point
    return (y * y - x * x * x - curve.a * x - curve.b) % curve.p == 0
def point_neg(point):
    assert is_on_curve(point)
    if point is None:
        return None
    x, y = point
    result = (x, -y % curve.p)
    assert is_on_curve(result)
    return result
def point_add(point1, point2):
    assert is_on_curve(point1)
    assert is_on_curve(point2)
    if point1 is None:
        return point2
    if point2 is None:
        return point1
    x1, y1 = point1
    x2, y2 = point2
    if x1 == x2 and y1 != y2:
        return None
    if x1 == x2:
        m = (3 * x1 * x1 + curve.a) * inverse_mod(2 * y1, curve.p)
    else:
        m = (y1 - y2) * inverse_mod(x1 - x2, curve.p)
    x3 = m * m - x1 - x2
    y3 = y1 + m * (x3 - x1)
    result = (x3 % curve.p,
              -y3 % curve.p)
    assert is_on_curve(result)
    return result
def scalar_mult(k, point):
    assert is_on_curve(point)
    if k % curve.n == 0 or point is None:
        return None
    if k < 0:
        return scalar_mult(-k, point_neg(point))
    result = None
    addend = point
    while k:
        if k & 1:
            result = point_add(result, addend)
        addend = point_add(addend, addend)
        k >>= 1
    assert is_on_curve(result)
    return result
def make_keypair():
    private_key = random.randrange(1, curve.n)
    public_key = scalar_mult(private_key, curve.g)
    return private_key, public_key
def verify_signature(public_key, message, signature):
    z = hash_message(message)
    r, s = signature
    w = inverse_mod(s, curve.n)
    u1 = (z * w) % curve.n
    u2 = (r * w) % curve.n
    x, y = point_add(scalar_mult(u1, curve.g),
                     scalar_mult(u2, public_key))
    if (r % curve.n) == (x % curve.n):
        return 'signature matches'
    else:
        return 'invalid signature'
@app.route('/')
def hello():
    message = "Hello"
    result = ""
    if len(sys.argv) > 1:
        message = str(sys.argv[1])
    private, public = make_keypair()
    a = "Private key:", hex(private)
    result += str(a)
    result += "\n"
    a = "Public key: (0x{:x}, 0x{:x})".format(*public)
    result += a
    result += "\n"
    result += "\n=========================\n"
    r = 123456
    result += str(public)
    R = scalar_mult(r, curve.g)
    S = scalar_mult(r, public)
    result += "\n======Symmetric key========\n"
    a = "Encryption key:", S[0]
    result += str(a)
    result += "\n"
    cipher = AESCipher(enc_long(S[0])).encrypt(message)
    a = "Encrypted:\t", binascii.hexlify(cipher)
    result += str(a)
    result += "\n"
    text = AESCipher(enc_long(S[0])).decrypt(cipher)
    a = "Decrypted:  ", text
    result += str(a)
    result += "\n"
    return result, 200, {'Content-Type': 'text/plain; charset=utf-8'}
@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return .format(e), 500
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)