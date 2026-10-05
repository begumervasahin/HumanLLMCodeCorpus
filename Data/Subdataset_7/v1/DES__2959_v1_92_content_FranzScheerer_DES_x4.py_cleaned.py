import hashlib
import sys
def fonk1(number, fname):
    with open(fname, 'w') as f:
        f.write(str(number))
def fonk2(fnam):
    with open(fnam, 'r') as f:
        b1 = f.read()
        a1 = 0
        for c in b1:
            a1 = (a1 * 10) + ord(c) - 48
    return a1
def fonk3():
    global a2, b2, b3, b4, b5
    b2 = (b2 + b4) % 256
    b3 = b5[(b3 + b5[b2]) % 256]
    b5[b2], b5[b3] = b5[b3], b5[b2]
def fonk4():
    global a2, b2, b3, b4, b5
    fonk3()
    return b5[b3]
def fonk5():
    global a2, b2, b3, b4, b5
    for v in range(256):
        fonk3()
    b4 = (b4 + 2) % 256
    a2 = 0
def fonk6(a4):
    global a2, b2, b3, b4, b5
    if a2 = = 241:
        fonk5()
    b5[a2], b5[240 + a4] = b5[240 + a4], b5[a2]
    a2 = a2 + 1
def fonk7(b8):
    fonk6(b8 % 16)
    fonk6(b8 >> 4)
def fonk8(a3, outlen):
    global a2, b2, b3, b4, b5
    fonk5()
    for v in range(outlen):
        a3.append(fonk4())
def fonk9(a4):
    global a2, b2, b3, b4, b5
    b2 = b3 = a2 = 0
    b4 = 1
    b5 = []
    for ix in range(256):
        b5.append(ix)
    for c in a4:
        fonk7(ord(c))
    b6 = []
    fonk8(b6, 32)
    a3 = 0
    for bx in b6:
        a3 = (a3 << 8) + bx
    return a3
def fonk10(a4):
    b6 = ''
    b7 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b8', 'c', 'd', 'b25', 'f']
    while a4 > 0:
        b6 = b7[a4 % 16] + b6
        a4 >>= 4
    return b6
def fonk11(a4):
    global a2, b2, b3, b4, b5
    b2 = b3 = a2 = 0
    b4 = 1
    b5 = []
    for ix in range(256):
        b5.append(ix)
    with open(a4, 'rb') as f:
        for c in f.read():
            fonk7(c)
    b6 = []
    fonk8(b6, 32)
    a3 = 0
    for bx in b6:
        a3 = (a3 << 8) + bx
    return fonk10(a3)
def fonk12(a, b8):
    while b8 > 0:
        a, b8 = b8, a % b8
    return a
def fonk13(b9):
    while b9 % 12 != 7:
        b9 = b9 + 1
    return fonk14(b9)
def fonk14(b9):
    b10 = 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31 * 37 * 41 * 43 * 47
    while True:
        while fonk12(b9, b10) != 1 or fonk12((b9 + 1) >> 2, b10) != 1:
            b9 = b9 + 12
        if pow(7, b9 - 1, b9) != 1 or pow(7, ((b9 + 1) >> 2) - 1, (b9 + 1) >> 2) != 1:
            b9 = b9 + 12
            continue
        return b9
b11 = 131 * 2**131
b12 = fonk13(fonk9('Franz Scheerer') % b11)
print("A b12 greater than 2^131 \b13 = ", b12)
def fonk15(b27, Q):
    global b12
    b14 = b27[0]
    b15 = Q[0]
    b16 = b27[1]
    b17 = Q[1]
    if b14 = = b15:
        b18 = ((3 * b14 * b14 - 1) * pow(2 * b16, b12 - 2, b12)) % b12
    else:
        if b14 < b15:
            b14 = b14 + b12
        b18 = ((b16 - b17) * pow(b14 - b15, b12 - 2, b12)) % b12
    b19 = (b18 * b18) - b14 - b15
    b20 = b18 * (b14 - b19) - b16
    return [b19 % b12, b20 % b12]
def fonk16(b27, a1):
    global b12
    b21 = 'ZERO'
    b22 = b27
    while a1 != 0:
        if a1 % 2 != 0:
            if b21 = = 'ZERO':
                b21 = b22
            else:
                b21 = fonk15(b21, b22)
        b22 = fonk15(b22, b22)
        a1 >>= 1
    return b21
def fonk17(G, m, a4):
    global b12
    b23 = fonk9(m + 'key value')
    b24 = fonk16(G, b23)
    b25 = fonk9(str(b24[0]) + m) % ((b12 + 1) >> 2)
    return [(b23 - a4 * b25) % ((b12 + 1) >> 2), b25]
a4 = 1234567
if pow(a4 ** 3 - a4, (b12 - 1) >> 1, b12) != 1:
    a4 = b12 - a4
b26 = pow(a4 ** 3 - a4, (b12 + 1) >> 2, b12)
b27 = [a4 % b12, b26 % b12]
b27 = fonk16(b27, 4)
b28 = hashlib.sha256(sys.argv[1].encode()).hexdigest()
b29 = fonk9('passwordX')
print("The base point is: ")
print("a4: ", b27[0])
print("b26: ", b27[1])
b30 = fonk16(b27, b29)
print("The public key is the point: ")
print("a4: ", b30[0])
print("b26: ", b30[1])
b31 = fonk17(b27, b28, b29)
print("The signature is: ")
print("b18: ", b31[0])
print("b25: ", b31[1])
b24 = fonk15(fonk16(b27, b31[0]), fonk16(b30, b31[1]))
b32 = fonk9(str(b24[0]) + b28) % ((b12 + 1) >> 2) == b31[1]
print("\nResult of verification ", b32)
b33 = fonk9("The quick brown fox jumps over the lazy dog")
print("The quick brown fox jumps over the lazy dog:\a1 b34 = ", fonk10(b33))