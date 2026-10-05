from __future__ import print_function
import numpy as np
from byte_utils import bytes_from_hex
from keys500 import b8
from softAESr import AESr
from AESUtils import Gmul, getGmulInv, SBOX, mix_col
from collections import defaultdict
import pickle
import matplotlib.pyplot as plt
b1 = False
b2 = True
a1 = 6
def fonk1(a, b):
    b3 = [[]]*256
    for k in range(256):
        b4 = SBOX[a^k] ^ SBOX[b^k]
        b3[b4] = b3[b4] + [k]
    return b3
def fonk2(a, b5):
    if b5 = = 0:
        return np.array([a[0],  a[5], a[10], a[15]], b6 = np.uint8)
    raise Exception("Unsupported b42 b5")
def fonk3(b56, k, b42):
    b7 = fonk2(b56,b42)
    b8 = fonk2(k, b42)
    return mix_col(b7, b8)
def fonk4(b68, b69, b31, b10):
    global b59
    b9 = SBOX[b68^b31] ^ SBOX[b69^b31]
    if b10 = = 0:
        a2 = 2
        a3 = 3
    if b10 = = 1:
        a2 = 1
        a3 = 2
    if b10 = = 2:
        a2 = 1
        a3 = 1
    if b10 = = 3:
        a2 = 3
        a3 = 1
    b11 = getGmulInv(a3)
    b12 = Gmul(b11, Gmul(a2, b9))
    return b59[b12]
def fonk5(b68, b69, b10):
    b13 = {}
    for b31 in range(256):
        b14 = fonk4(b68, b69, b31, b10)
        if len(b14) == 2 or len(b14) == 4:
            b13[b31] = b14
        elif len(b14) != 0:
            print (b14)
            raise Exception('get_key_pairs - len of b14 is bad')
    return b13
def fonk6(b8, b58, b10 = 0):
    b15 = []
    for j in range(len(b8)):
        for b40 in range(len(b58)):
            b16 = bytes_from_hex(b8[j])
            b17 = fonk3(b58[b40][0], b16, 0)
            b18 = fonk3(b58[b40][1], b16, 0)
            b4 = b17 ^ b18
            if b4[b10] == 0:
                b15.append([j, b40])
    return b15
def fonk7(x,y):
    b19 = x[:]
    b20 = y[:]
    b19[0] = y[0]
    b19[7] = y[7]
    b19[10] = y[10]
    b19[13] = y[13]
    b20[0] = x[0]
    b20[7] = x[7]
    b20[10] = x[10]
    b20[13] = x[13]
    return np.array(b19, b6 = np.uint8), np.array(b20, b6=np.uint8)
def fonk8(p2, ptag2, b13, b21 = 3, b10 = 0, b42=0):
    b22 = fonk2(p2, b42)
    b23 = fonk2(ptag2, b42)
    b24 = defaultdict(list)
    b25 = defaultdict(list)
    for b31 in b13.keys():
        for b14 in b13[b31]:
            b4 = mix_col(np.concatenate([b22[0:2],[0,0]]), [b31, b14, 0, 0])[b10]
            b26 = mix_col(np.concatenate([b23[0:2],[0,0]]), [b31, b14, 0, 0])[b10]
            b24[b4^b26].append([b31, b14])
    b7 = [0] * 4
    b27 = [0] * 4
    b7[b21] = b22[b21]
    b27[b21] = b23[b21]
    b28 = [0] * 4
    for key_byte in range(256):
        b28[b21] = key_byte
        b4 = mix_col(b7, b28)[b10]
        b26 = mix_col(b27, b28)[b10]
        b25[b4 ^ b26].append(key_byte)
    b29 = defaultdict(list)
    for b4 in b24.keys():
        if b4 in b25.keys():
            for b31, b14 in b24[b4]:
                b30 = b25[b4]
                b29[b31+b14*256] = b29[b31+b14*256] + b30
                if b31 = = b62 and False:
                    print ('This is the real deal', b31, b14, b29[b31+b14*256])
    return b29
def fonk9(b43, b44):
    b32 = b61.encrypt(b43)
    b33 = b61.encrypt(b44)
    c2i, b34 = fonk7(b32, b33)
    b35 = b61.decrypt(c2i)
    b36 = b61.decrypt(b34)
    return b35, b36
def fonk10(b43, b44, b45, b51, b46, b53, b52, b54, b10, b42):
    b37 = fonk8(b45, b51, b65[b10], 3, b10)
    b38 = fonk8(b46, b53, b65[b10], 2, b10)
    b39 = []
    for b40 in range(256):
        if b40 = = b52 or b40 == b54:
            continue
        b43[1] = b40
        b44[1] = b40
        b35, b36 = fonk9(b43, b44)
        b39.append([fonk2(b35,b42), fonk2(b36, b42)])
        if len(b39) >= a1:
            break
    b41 = []
    a4 = 0
    for k0k5 in b37.keys():
        if k0k5 in b38.keys():
            b31 = k0k5 % 256
            b14 = k0k5
            if True:
                for b64 in b38[k0k5]:
                    for b63 in b37[k0k5]:
                        if b31 = = b62 and False:
                            print ([b31, b14, b64, b63])
                            print ([b31 ^ a5 ^ a6, b14, b64, b63])
                        a4 += 1
                        for b40 in range(a1):
                            b22, b23 = b39[b40]
                            b4 = mix_col(b22, [b31, b14, b64, b63])[b10]
                            b26 = mix_col(b23, [b31, b14, b64, b63])[b10]
                            if b4 != b26:
                                break
                        if b4 = = b26:
                            print ('Recovered b8 is', [b31, b14, b64, b63])
                            b41.append([b31, b14, b64, b63])
    return b41
def fonk11(b67, b42 = 0):
    b43 = b67[0][:]
    b44 = b67[1][:]
    b45 = None
    b46 = None
    for b40 in range(256):
        b43[1] = b40
        b44[1] = b40
        b35, b36 = fonk9(b43, b44)
        if b36[10] ^ b35[10] == 0 and b45 is None:
            if b1:
                b47 = fonk3(b35, b16,0)
                b48 = fonk3(b36, b16, 0)
                b49 = fonk3(b43, b16, 0)
                b50 = fonk3(b44, b16, 0)
                print ('one round b4 10', b47^b48, b49^b50)
                print ('b7 ', fonk2(b35, b42), fonk2(b36, b42))
            b45 = b35
            b51 = b36
            b52 = b40
        if b36[15] ^ b35[15] == 0 and b46 is None:
            if b1:
                b47 = fonk3(b35, b16,0)
                b48 = fonk3(b36, b16, 0)
                b49 = fonk3(b43, b16, 0)
                b50 = fonk3(b44, b16, 0)
                print ('one round b4 15', b47^b48, b49^b50)
                print ('b7 ', fonk2(b35, b42), fonk2(b36, b42))
            b46 = b35
            b53 = b36
            b54 = b40
        if (b45 is not None) and (b46 is not None):
            for index in range(4):
                b41 = fonk10(b43, b44, b45, b51, b46, b53, b52, b54, index, b42)
                if len(b41) > 0:
                    return b41
            return None
b55 = [0] * 16
a5 = 0
a6 = 1
b56 = b55[:]
b56[5] = a5
b57 = b55[:]
b57[5] = a6
if b2:
    b58 = []
    for b40 in range(16):
        for j in range(16, 16+8):
            b58.append([[b40] + b56[1:], [j] + b57[1:]])
else:
    b58 = [[b56, [val] + b57[1:]] for val in range(1,129)]
b59 = fonk1(a5,a6)
a7 = 0
a8 = 0
a9 = 0
b60 = []
for b21 in range(len(b8)):
    b16 = bytes_from_hex(b8[b21])
    b61 = AESr(b16, 5)
    b14 = b16[5]
    b62 = b16[0]
    b63 = b16[15]
    b64 = b16[10]
    b65 = [[]]*4
    print ('starting attack on b8 number', b21, ' with pair', b66 = ' ')
    print ('len b58 ', len(b58))
    for pair_index in range(len(b58)):
        print (pair_index, b66 = ' ')
        b67 = b58[pair_index]
        b68 = b67[0][0]
        b69 = b67[1][0]
        for b40 in range(4):
            b65[b40] = fonk5(b68, b69, b40)
        b70 = fonk11(b58[pair_index])
        if b70 is not None:
            break
    print ('\nreal b8 number', b21, [b62, b14, b64, b63])
    print ('calc b8', b70, ' from pair index ', pair_index)
    a7 += 1
    if b70 is not None:
        a8 += 1
        b71 = b70[0] == [b62, b14, b64, b63]
        print ('good b8? ', b71)
        if b71:
            a9 += 1
            b60.append(pair_index)
    print ('found good', a9, ' out of found ', a8, ' out of', a7)
b60.sort()
b60 = np.array(b60)
b72 = np.zeros(len(b58))
for b40 in range(len(b58)):
    b72[b40] = sum(b60 <= b40)
b72 = b72  * 1.0 / a7
if b2:
    b73 = 'RB%dStruct.pickle' % len(b8)
else:
    b73 = 'RB%d.pickle' % len(b8)
print('Filename is ', b73)
with open(b73, 'wb') as handle:
    pickle.dump([b58, b60, a9], handle)
plt.plot(range(len(b58)), b72)
plt.show()