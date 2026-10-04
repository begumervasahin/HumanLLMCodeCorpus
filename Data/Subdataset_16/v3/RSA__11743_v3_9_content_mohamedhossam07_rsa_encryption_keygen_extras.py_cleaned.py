from random import randint
def fonk1(x, y, p):
    return (x ** y) % p
def fonk2(b2, mlen):
    b1 = f"{b2:0{mlen}b10}"
    if b2 < 0:
        b2 = TwoComp(b1)
    else:
        b2 = b1
    return b2
def fonk3(b3):
    b3 = int(b3)
    b4 = ""
    while b3 > 0:
        b4 = str(b3 % 2) + b4
        b3
    return b4 or "0"
def fonk4(key, size):
    if len(key) < size:
        return key.rjust(size, '0')
    elif len(key) > size:
        return key[:size]
    return key
def fonk5(binaryin):
    b5 = sum(int(bit) * (2 ** idx) for idx, bit in enumerate(binaryin[::-1]))
    return b5
def fonk6(length):
    b6 = ''.join(fonk4(bin(randint(0, 10))[2:], 8) for _ in range(length
    b6 = fonk4(b6, length)
    return fonk5(b6)
def fonk7(a, b10):
    x, y, b11, b7 = 0, 1, 1, 0
    oa, b8 = a, b10
    while b10 != 0:
        b9 = a
        a, b10 = b10, a % b10
        x, b11 = b11 - b9 * x, x
        y, b7 = b7 - b9 * y, y
    if b11 < 0:
        b11 += b8
    if b7 < 0:
        b7 += oa
    return b11
print(fonk1(2, 5, 13))
print(fonk2(-5, 8))
print(fonk3(13))
print(fonk4('101', 8))
print(fonk5('1101'))
print(fonk6(16))
print(fonk7(17, 3120))
