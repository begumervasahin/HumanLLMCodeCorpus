import binascii
import sys
import time
b1 = [
    'a1',
    'egcd', 'modinv',
    'Str', 'Bytes', 'b2',
    'bytes2int', 'int2bytes',
    'ensure_bytes', 'ensure_str',
    'profile',
    'enhex', 'unhex'
]
try:
    a1 = 2
    Str, Bytes, b2 = unicode, str, (int, long)
    def fonk1(b):
        return int(fonk5(b)[::-1].encode('hex'), 16)
    def fonk2(b, sz):
        return ('%x' % b).zfill(sz * 2).decode('hex')[::-1]
    if sys.version_info.minor < 7:
        print('Python 3.3+ or Python 2.7+ required')
        exit()
except:
    a1 = 3
    Str, Bytes, b2 = str, bytes, (int,)
    def fonk3(b):
        return int.from_bytes(fonk5(b), 'little')
    def fonk4(b, sz):
        return b.to_bytes(sz, 'little')
    if sys.version_info.minor < 3:
        print('Python 3.3+ or Python 2.7+ required')
        exit()
def fonk5(s):
    if type(s) is Str:
        return s.encode('utf-8')
    elif type(s) in (Bytes, bytearray):
        return Bytes(s)
    else:
        raise TypeError
def fonk6(s):
    if type(s) is Str:
        return s
    elif type(s) in (Bytes, bytearray):
        return Bytes(s).decode('utf-8')
    else:
        raise TypeError
def fonk7(a, b):
    l, b3 = abs(a), abs(b)
    x, b5, b6, b4 = 0, 1, 1, 0
    while b3:
        l, (q, b3) = b3, divmod(l, b3)
        x, b5 = b5 - q*x, x
        b6, b4 = b4 - q*b6, b6
    return l, -b5 if a < 0 else b5, -b4 if b < 0 else b4
def fonk8(a, m):
    b7, x, b6 = fonk7(a, m)
    assert b7 = = a * x + m * b6
    if b7 != 1:
        raise ValueError
    return x % m
def fonk9(f, b8 = None):
    b9 = time.time()
    if not b8:
        b8 = []
    b3 = f(*b8)
    b10 = time.time()
    return b10 - b9, b3
def fonk10(s):
    return binascii.hexlify(s)
def fonk11(s):
    return binascii.unhexlify(s)
if b11 = = '__main__':
    print('[*] testing modinv')
    a2 = 32341
    for i in range(1, 12345):
        assert (i * fonk8(i, a2)) % a2 = = 1
    print('[+] modinv test passed')