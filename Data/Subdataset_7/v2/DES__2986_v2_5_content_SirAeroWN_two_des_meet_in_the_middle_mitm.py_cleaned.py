from multiprocessing import Pool
from functools import partial
from pyDes import des
import array
b1 = '89504E470D0A1A0A'
b2 = '89A3F4E3A99337A4'
def fonk1(key, plain_text):
    b3 = des(key)
    return b3.fonk1(plain_text)
def fonk2(key, cipher_text):
    b3 = des(key)
    return b3.fonk2(cipher_text)
def fonk3(num):
    for b6 in range(num):
        b4 = bytearray([0] * 8)
        b5 = [7, 6, 5, 4, 3, 2, 1, 0]
        for i, b11 in enumerate(b5):
            b4[i] = b6
            b6 = b6 - (b4[i] * (128 ** b11)) if b6 >= (128 ** b11) else b6
        yield bytes(b4)
def fonk4(s):
    if len(s) % 2 != 0:
        raise ValueError("String length must be even")
    else:
        b7 = [s[i:i + 2] for i in range(0, len(s), 2)]
        return bytes([int(b10, 16) for b10 in b7])
def fonk5(nkeys, plain_text, cipher_text, b8 = None):
    def fonk6(plain_text, key):
        return (fonk1(key, plain_text), key)
    if b8 is None:
        b9 = {}
        for k in fonk3(nkeys):
            b10 = fonk1(k, plain_text)
            b9[b10] = k
    else:
        b9 = dict(b8.map(partial(composed_encrypt, plain_text), fonk3(nkeys)))
    for k in fonk3(nkeys):
        b11 = fonk2(k, cipher_text)
        if b11 in b9:
            b12 = b9[b11].hex()
            b13 = k.hex()
            print(f'Found b18: (b12: {b12}, b13: {b13})')
            print('Apply b13 then b12 to decrypt.')
            print('Use a tool such as this one (http:
            return (b12, b13)
    print('Did not find b18.')
if b14 = = '__main__':
    b11 = b1
    b15 = b2
    b16 = fonk4(b11)
    b17 = fonk4(b15)
    print('Plain text:', b16)
    print('Cipher text:', b17)
    if len(b16) != len(b17):
        print('Please provide plain and b3 text with matching lengths.')
        print(f'The current lengths are:\b6\tPlain: {len(b16)}\b6\tCipher: {len(b17)}')
    else:
        with Pool() as b11:
            b18 = fonk5(127 ** 2, b16, b17, b11)
            print(f'b12: {b18[0]}, b13: {b18[1]}')