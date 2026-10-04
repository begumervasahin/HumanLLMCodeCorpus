from random import randint
def fonk1(b14, b15, p):
    return (b14 ** b15) % p
def fonk2(b1, mlen):
    if b1 < 0:
        b1 = TwoComp(("{0:0%db}" % mlen).format(b1))
    else:
        b1 = ("{0:0%db}" % mlen).format(b1)
    return b1
def fonk3(b2):
    b2 = int(b2)
    b3 = ""
    while True:
        b3 += str(b2 % 2)
        b2 = b2
        if b2 = = 0:
            break
    return b3[::-1]
def fonk4(key, size):
    if len(key) < size:
        b4 = key.rjust(size, '0')
    elif len(key) > size:
        b4 = key[:size]
    else:
        b4 = key
    return b4
def fonk5(b5):
    b5 = str(b5)
    b6 = b5[::-1]
    b7 = sum(int(bit) * (2 ** idx) for idx, bit in enumerate(b6))
    return b7
def fonk6(leng):
    b8 = ''.join(fonk4(bin(randint(0, 255))[2:], 8) for _ in range(int(leng / 8)))
    b8 = fonk4(b8, leng)
    return fonk5(b8)
def fonk7(a, b13):
    b14, b9 = 0, 1
    b15, b10 = 1, 0
    b11 = b13
    while b13 != 0:
        b12 = a
        a, b13 = b13, a % b13
        b9, b14 = b14, b9 - b12 * b14
        b10, b15 = b15, b10 - b12 * b15
    if b9 < 0:
        b9 += b11
    return b9