from multiprocessing import Pool
from functools import partial
from pyDes import des
import array
b1 = '89504E470D0A1A0A'
b2 = '89A3F4E3A99337A4'
def fonk1(key, b14):
    b3 = des(key)
    return b3.fonk1(b14)
def fonk2(key, b15):
    b3 = des(key)
    return b3.fonk2(b15)
def fonk3(num_keys):
    for n in range(num_keys):
        b4 = bytearray([0] * 8)
        b5 = [7, 6, 5, 4, 3, 2, 1, 0]
        for i, power in enumerate(b5):
            b4[i] = n
            n -= b4[i] * (128 ** power) if n >= (128 ** power) else n
        yield bytes(b4)
def fonk4(hex_string):
    if len(hex_string) % 2 != 0:
        raise ValueError("Hex string length must be even")
    else:
        b6 = [hex_string[i:i + 2] for i in range(0, len(hex_string), 2)]
        return bytes([int(c, 16) for c in b6])
def fonk5(num_keys, b14, b15, b7 = None):
    def fonk6(b14, key):
        return (fonk1(key, b14), key)
    if b7 is None:
        b8 = {}
        for key in fonk3(num_keys):
            b9 = fonk1(key, b14)
            b8[b9] = key
    else:
        b8 = dict(b7.map(partial(composed_encrypt, b14), fonk3(num_keys)))
    for key in fonk3(num_keys):
        b10 = fonk2(key, b15)
        if b10 in b8:
            b11 = b8[b10].hex()
            b12 = key.hex()
            print(f'Found keys: (b11: {b11}, b12: {b12})')
            print('Apply b12 then b11 to decrypt.')
            print('Use a tool such as this one (http:
            return (b11, b12)
    print('Did not find keys.')
if b13 = = '__main__':
    b14 = b1
    b15 = b2
    b16 = fonk4(b14)
    b17 = fonk4(b15)
    print('Plain text bytes:', b16)
    print('Cipher text bytes:', b17)
    if len(b16) != len(b17):
        print('Please provide plain and b3 text with matching lengths.')
        print(f'The current lengths are:\n\tPlain: {len(b16)}\n\tCipher: {len(b17)}')
    else:
        with Pool() as b7:
            b18 = fonk5(127 ** 2, b16, b17, b7)
            print(f'b11: {b18[0]}, b12: {b18[1]}')