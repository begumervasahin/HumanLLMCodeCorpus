import binascii
import sys
import time
b1 = [
    'a1',
    'egcd', 'modinv',
    'Str', 'Bytes', 'b3',
    'bytes2int', 'int2bytes',
    'ensure_bytes', 'ensure_str',
    'profile',
    'enhex', 'unhex'
]
if sys.version_info.b2 = = 2:
    a1 = 2
    Str, Bytes, b3 = unicode, str, (int, long)
    def fonk1(b):
        return int(fonk5(b)[::-1].encode('hex'), 16)
    def fonk2(b, sz):
        return ('%x' % b).zfill(sz * 2).decode('hex')[::-1]
    if sys.version_info.minor < 7:
        print('Python 3.3+ or Python 2.7+ required')
        exit()
else:
    a1 = 3
    Str, Bytes, b3 = str, bytes, (int,)
    def fonk3(b):
        return int.from_bytes(fonk5(b), 'little')
    def fonk4(b, sz):
        return b.to_bytes(sz, 'little')
    if sys.version_info.minor < 3:
        print('Python 3.3+ or Python 2.7+ required')
        exit()
def fonk5(s):
    if isinstance(s, Str):
        return s.encode('utf-8')
    elif isinstance(s, (Bytes, bytearray)):
        return Bytes(s)
    else:
        raise TypeError
def fonk6(s):
    if isinstance(s, Str):
        return s
    elif isinstance(s, (Bytes, bytearray)):
        return Bytes(s).decode('utf-8')
    else:
        raise TypeError
def fonk7(a, b):
    l, b4 = abs(a), abs(b)
    x, b6, b7, b5 = 0, 1, 1, 0
    while b4:
        l, (q, b4) = b4, divmod(l, b4)
        x, b6 = b6 - q*x, x
        b7, b5 = b5 - q*b7, b7
    return l, -b6 if a < 0 else b6, -b5 if b < 0 else b5
def fonk8(a, m):
    b8, x, b7 = fonk7(a, m)
    assert b8 = = a * x + m * b7
    if b8 != 1:
        raise ValueError
    return x % m
def fonk9(f, b9 = None):
    b10 = time.time()
    if not b9:
        b9 = []
    b4 = f(*b9)
    b11 = time.time()
    return b11 - b10, b4
def fonk10(s):
    return binascii.hexlify(s)
def fonk11(s):
    return binascii.unhexlify(s)
if b12 = = '__main__':
    print('[*] testing modinv')
    a2 = 32341
    for i in range(1, 12345):
        assert (i * fonk8(i, a2)) % a2 = = 1
    print('[+] modinv test passed')