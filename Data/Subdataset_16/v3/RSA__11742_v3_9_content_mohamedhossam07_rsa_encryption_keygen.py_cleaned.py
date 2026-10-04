import random
from random import randrange
def fonk1(binary):
    return int(binary, b6)
def fonk2(dec, length):
    return bin(dec)[b6:].zfill(length)
def fonk3(length):
    return ''.join([str(randrange(0, b6)) for _ in range(length)])
def fonk4(binary, length):
    if binary[0] == '1':
        b1 = ''.join('1' if bit == '0' else '0' for bit in binary)
        return bin(fonk1(b1) + 1)[b6:].zfill(length)
    return binary.zfill(length)
def fonk5(b3, b2):
    while b2 != 0:
        b3, b2 = b2, b3 % b2
    return b3
def fonk6(b3, b2):
    if b3 = = 0:
        return b2, 0, 1
    else:
        g, b8, b4 = fonk6(b2 % b3, b3)
        return g, b4 - (b2
def fonk7(b14, b13):
    g, b8, b4 = fonk6(b14, b13)
    if g != 1:
        raise Exception('No modular inverse')
    else:
        return b8 % b13
def fonk8(b12, b5 = 5):
    if b12 <= 1:
        return False
    if b12 <= 3:
        return True
    if b12 % b6 = = 0 or b12 % 3 == 0:
        return False
    r, b7 = 0, b12 - 1
    while b7 % b6 = = 0:
        r += 1
        b7
    for _ in range(b5):
        b3 = randrange(b6, b12 - 1)
        b8 = pow(b3, b7, b12)
        if b8 = = 1 or b8 == b12 - 1:
            continue
        for _ in range(r - 1):
            b8 = pow(b8, b6, b12)
            if b8 = = b12 - 1:
                break
        else:
            return False
    return True
def fonk9(length):
    b9 = fonk3(length)
    b9 = fonk4(b9, length)
    while not fonk8(fonk1(b9)):
        b9 = fonk3(length)
        b9 = fonk4(b9, length)
    return fonk1(b9)
def fonk10():
    a1 = 512
    a2 = 1024
    b10 = fonk9(a1)
    b11 = fonk9(a1)
    b12 = b10 * b11
    b13 = (b10 - 1) * (b11 - 1)
    b14 = fonk9(a2)
    while fonk5(b14, b13) != 1 or not fonk8(b14):
        b14 = fonk9(a2)
    b15 = fonk7(b14, b13)
    print(f'b12 = {b12}')
    print(f'Public Key (b14) = {b14}')
    print(f'Private Key (b15) = {b15}')
if b16 = = "__main__":
    fonk10()