from random import randint
def fonk1(x, y, p):
    return (x ** y) % p
def fonk2(b1, mlen):
    if b1 < 0:
        b1 = TwoComp(f"{b1:0{mlen}b10}")
    else:
        b1 = f"{b1:0{mlen}b10}"
    return b1
def fonk3(b2):
    b2 = int(b2)
    b3 = ""
    while b2 > 0:
        b3 = str(b2 % 2) + b3
        b2
    return b3 or "0"
def fonk4(key, size):
    if len(key) < size:
        return key.rjust(size, '0')
    elif len(key) > size:
        return key[:size]
    return key
def fonk5(b4):
    b4 = b4[::-1]
    b5 = sum(int(bit) * (2 ** idx) for idx, bit in enumerate(b4))
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
