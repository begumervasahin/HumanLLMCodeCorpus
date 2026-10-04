from random import randint
def fonk1(b8, b9, p):
    return (b8 ** b9) % p
def fonk2(b1, mlen):
    if b1 < 0:
        b1 = TwoComp(("{0:0%db}" % mlen).format(b1))
    else:
        b1 = ("{0:0%db}" % mlen).format(b1)
    return b1
def fonk3(decimalin):
    b2 = bin(int(decimalin))[2:]
    return b2
def fonk4(key, size):
    if len(key) < size:
        return key.rjust(size, '0')
    elif len(key) > size:
        return key[:size]
    return key
def fonk5(binaryin):
    return int(binaryin, 2)
def fonk6(length):
    b2 = ''.join(fonk4(bin(randint(0, 255))[2:], 8) for _ in range(length
    b2 = fonk4(b2, length)
    return fonk5(b2)
def fonk7(a, b7):
    b8, b3 = 0, 1
    b9, b4 = 1, 0
    b5 = b7
    while b7 != 0:
        b6 = a
        a, b7 = b7, a % b7
        b3, b8 = b8, b3 - b6 * b8
        b4, b9 = b9, b4 - b6 * b9
    if b3 < 0:
        b3 += b5
    return b3