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
def fonk3(b11, b12, plain_text):
    return fonk1(b12, fonk1(b11, plain_text))
def fonk4(b11, b12, cipher_text):
    return fonk2(b11, fonk2(b12, cipher_text))
def fonk5(num):
    for b6 in range(num):
        b4 = [0] * 8
        b5 = [7, 6, 5, 4, 3, 2, 1, 0]
        for i, b10 in enumerate(b5):
            b4[i] = b6
            b6 = b6 - (b4[i] * (128 ** b10)) if b6 >= (128 ** b10) else b6
        yield array.array('B', b4).tostring()
def fonk6(arr):
    return array.array('B', arr).tostring()
def fonk7(bs):
    return ''.join([format(b, '02x') for b in bs])
def fonk8(bs):
    return [int(b) for b in bs]
def fonk9(s):
    return ''.join([format(ord(b9), '02x') for b9 in s])
def fonk10(nkeys, plain_text, cipher_text, b7 = None):
    def fonk11(plain_text, key):
        return (fonk1(key, plain_text), key)
    if b7 is None:
        b8 = {}
        for k in fonk5(nkeys):
            b9 = fonk1(k, plain_text)
            b8[b9] = k
    else:
        b8 = dict(b7.map(partial(composed_encrypt, plain_text), fonk5(nkeys)))
    for k in fonk5(nkeys):
        b10 = fonk2(k, cipher_text)
        if b10 in b8.b17():
            b11 = fonk8(b8[b10])
            b12 = fonk8(k)
            print(f'Found b17: (b11:{b11}, b12:{b12})')
            print('Apply b12 then b11 to decrypt.')
            print('Use a tool such as this one (http:
            return (b11, b12)
    print('Did not find b17')
if b13 = = '__main__':
    b10 = b1
    b14 = b2
    b15 = fonk9(b10)
    b16 = fonk9(b14)
    print('Plain text:', b15)
    print('Cipher text:', b16)
    if len(b15) != len(b16):
        print('Please provide plain and b3 text with matching lengths')
        print(f'The current lengths are:\b6\tPlain: {len(b15)}\b6\tCipher: {len(b16)}')
    else:
        with Pool() as b7:
            b17 = fonk10(127 ** 2, b15, b16, b7)
            print(f'b11: {fonk7(b17[0])}, b12: {fonk7(b17[1])}')