import sys
import hashlib
b1 = b3 = b6 = a1 = 0
b2 = []
def fonk1(a3):
    global b1, b3, b6, a1, b2
    b3 = b6 = b1 = 0
    a1 = 1
    b2 = [ix for ix in range(256)]
    for c in a3:
        fonk7(ord(c))
    b4 = []
    fonk8(b4, 32)
    a2 = 0
    for bx in b4:
        a2 = (a2 << 8) + bx
    return a2
def fonk2(a3):
    b4 = ''
    b5 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b18', 'c', 'd', 'b17', 'f']
    while a3 > 0:
        b4 = b5[a3 % 16] + b4
        a3 >>= 4
    return b4
def fonk3():
    global b1, b3, b6, a1, b2
    b3 = (b3 + a1) % 256
    b6 = b2[(b6 + b2[b3]) % 256]
    b2[b3], b2[b6] = b2[b6], b2[b3]
def fonk4():
    global b1, b3, b6, a1, b2
    fonk3()
    return b2[b6]
def fonk5():
    global b1, b3, b6, a1, b2
    for _ in range(256):
        fonk3()
    a1 = (a1 + 2) % 256
    b1 = 0
def fonk6(a3):
    global b1, b3, b6, a1, b2
    if b1 = = 241:
        fonk5()
    b2[b1], b2[240 + a3] = b2[240 + a3], b2[b1]
    b1 += 1
def fonk7(b18):
    fonk6(b18 % 16)
    fonk6(b18 >> 4)
def fonk8(a2, outlen):
    global b1, b3, b6, a1, b2
    fonk5()
    for _ in range(outlen):
        a2.append(fonk4())
def fonk9(b24, Q):
    global b21
    b9, b7 = b24[0], Q[0]
    y1, b8 = b24[1], Q[1]
    if b9 = = b7:
        b10 = ((3 * b9 * b9 - 1) * pow(2 * y1, b21 - 2, b21)) % b21
    else:
        if b9 < b7:
            b9 += b21
        b10 = ((y1 - b8) * pow(b9 - b7, b21 - 2, b21)) % b21
    b11 = (b10 * b10) - b9 - b7
    b12 = b10 * (b9 - b11) - y1
    return [b11 % b21, b12 % b21]
def fonk10(b24, n):
    global b21
    b13 = 'ZERO'
    b14 = b24
    while n != 0:
        if n % 2 != 0:
            if b13 = = 'ZERO':
                b13 = b14
            else:
                b13 = fonk9(b13, b14)
        b14 = fonk9(b14, b14)
        n >>= 1
    return b13
def fonk11(G, m, a3):
    global b21
    b15 = fonk1(m + 'key value')
    b16 = fonk10(G, b15)
    b17 = fonk1(str(b16[0]) + m) % ((b21 + 1) >> 2)
    return [(b15 - a3 * b17) % ((b21 + 1) >> 2), b17]
def fonk12(a, b18):
    while b18 > 0:
        a, b18 = b18, a % b18
    return a
def fonk13(p):
    while p % 12 != 7:
        p += 1
    return fonk14(p)
def fonk14(p):
    b19 = 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31 * 37 * 41 * 43 * 47
    while True:
        while fonk12(p, b19) != 1 or fonk12((p + 1) >> 2, b19) != 1:
            p += 12
        if pow(7, p - 1, p) != 1 or pow(7, ((p + 1) >> 2) - 1, (p + 1) >> 2) != 1:
            p += 12
            continue
        return p
b20 = 131 * 2 ** 131
b21 = fonk13(fonk1('Franz Scheerer') % b20)
print("A b21 greater than 2^131 \b22 = ", b21)
a3 = 1234567
if pow(a3 ** 3 - a3, (b21 - 1) >> 1, b21) != 1:
    a3 = b21 - a3
b23 = pow(a3 ** 3 - a3, (b21 + 1) >> 2, b21)
b24 = [a3 % b21, b23 % b21]
b24 = fonk10(b24, 4)
b25 = hashlib.sha256(sys.argv[1].encode()).hexdigest()
b26 = fonk1('passwordX')
print("The base point is:")
print("a3:", b24[0])
print("b23:", b24[1])
b27 = fonk10(b24, b26)
print("The public key is the point:")
print("a3:", b27[0])
print("b23:", b27[1])
b28 = fonk11(b24, b25, b26)
print("The signature is:")
print("b10:", b28[0])
print("b17:", b28[1])
b16 = fonk9(fonk10(b24, b28[0]), fonk10(b27, b28[1]))
b29 = fonk1(str(b16[0]) + b25) % ((b21 + 1) >> 2) == b28[1]
print("\nResult of verification", b29)
b30 = fonk1("The quick brown fox jumps over the lazy dog")
print("The quick brown fox jumps over the lazy dog:\n b31 = ", fonk2(b30))