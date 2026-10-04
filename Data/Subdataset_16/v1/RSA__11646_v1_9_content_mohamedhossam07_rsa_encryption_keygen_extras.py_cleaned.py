from random import randint
def fonk1(x, y, p):
    return (x ** y) % p
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
    b5 = b5[::-1]
    b6 = sum(int(bit) * (2 ** idx) for idx, bit in enumerate(b5))
    return b6
def fonk6(leng):
    b7 = ''
    for _ in range(int(leng / 8)):
        b8 = str(bin(randint(0, 10)))[2:]
        b8 = fonk4(b8, 8)
        b7 += b8
    b7 = fonk4(b7, leng)
    return fonk5(b7)
def fonk7(a, b12):
    x, y, b13, b9 = 0, 1, 1, 0
    oa, b10 = a, b12
    while b12 != 0:
        b11 = a
        a, b12 = b12, a % b12
        x, b13 = b13 - b11 * x, x
        y, b9 = b9 - b11 * y, y
    if b13 < 0:
        b13 += b10
    if b9 < 0:
        b9 += oa
    return b13
print(fonk1(2, 5, 13))
print(fonk2(-5, 8))
print(fonk3(13))
print(fonk4('101', 8))
print(fonk5('1101'))
print(fonk6(16))
print(fonk7(17, 3120))
