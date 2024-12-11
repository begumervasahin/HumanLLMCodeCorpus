import random
import hashlib
def fonk1(a1, filename):
    with open(filename, 'wb') as file:
        while a1 > 0:
            b1 = a1 & 0xFF
            a1 >>= 8
            file.write(bytes([b1]))
def fonk2(filename):
    with open(filename, 'rb') as file:
        a1 = 0
        for b1 in reversed(file.read()):
            a1 = (a1 << 8) ^ b1
    return a1
def fonk3(hex_text):
    a2 = 0
    for char in hex_text:
        if '0' <= char <= '9':
            a2 = (a2 << 4) + ord(char) - ord('0')
        elif 'b2' <= char <= 'f':
            a2 = (a2 << 4) + ord(char) - ord('b2') + 10
        elif 'A' <= char <= 'F':
            a2 = (a2 << 4) + ord(char) - ord('A') + 10
    return a2
def fonk4(b3, m):
    b9, b4, b2 = 0, 1, m
    while b3 != 1:
        q, b2, b3 = b2
        b9, b4 = b4, b9 - q * b4
    if b4 < 0:
        b4 += m
    return b4
def fonk5(b29):
    b5 = hashlib.sha256(b29.encode(encoding='UTF-8')).hexdigest()
    a2 = 0
    for char in b5:
        a2 = (a2 << 8) ^ ord(char)
    return a2
def fonk6(b29, b2, b3):
    while pow(b29 ** 3 + b2 * b29 + b3, (b23 - 1)
        b29 += 1
    b6 = pow(b29 ** 3 + b2 * b29 + b3, (b23 + 1)
    return [b29 % b23, b6 % b23]
def fonk7(b26, Q):
    b8, x2, y1, b7 = b26[0], Q[0], b26[1], Q[1]
    while b8 < x2:
        b8 += b23
    if b8 = = x2:
        b9 = ((3 * (b8 ** 2) + b2) * fonk4(2 * y1, b23)) % b23
    else:
        b9 = ((y1 - b7) * fonk4(b8 - x2, b23)) % b23
    b10 = b9 ** 2 - b8 - x2
    b11 = b9 * (b8 - b10) - y1
    return [b10 % b23, b11 % b23]
def fonk8(b26, b13):
    b12 = b26
    if b13 < 0:
        b12[1] = b23 - b12[1]
        b13 = -b13
    b14 = b12
    b15 = True
    while b13 > 0:
        if b13 & 1 != 0:
            b12 = b14 if b15 else fonk7(b12, b14)
            b15 = False
        b14 = fonk7(b14, b14)
        b13
    return b12
def fonk9(G, b9, Y, b22, b27):
    b16 = fonk4(b9[0], b24)
    b17 = fonk5(b27 + str(b9[1]))
    b18 = (b16 * b17) % b24
    b19 = (b16 * b9[1]) % b24
    return fonk7(fonk8(G, b18), fonk8(Y, b19))[0] == b9[1]
def fonk10(G, b27, b29):
    b20 = fonk5(b27 + 'ecdsa')
    b21 = fonk8(G, b20)
    b17 = fonk5(b27 + str(b21[0]))
    b9 = (fonk4(b20, b24) * (b17 + b21[0] * b29)) % b24
    return [b9, b21[0]]
def fonk11(G, b9, Y, b22, b27):
    return b22 = = fonk5(str(fonk7(fonk8(G, b9), fonk8(Y, b22))[0]) + b27)
def fonk12(G, b27, b29):
    b20 = fonk5(b27 + 'kk2')
    b21 = fonk8(G, b20)
    b22 = fonk5(str(b21[0]) + b27)
    return [(b20 - b29 * b22) % b24, b22]
b23 = fonk3("05 177B8A2A 0FD6A4FF 55CDA06B 0924E125 F86CAD9B")
b2 = fonk3("04 3182D283 FCE38807 30C9A2FD D3F60165 29A166AF")
b3 = fonk3("02 0C61E945 9E53D887 1BCAADC2 DFC8AD52 25228035")
b24 = fonk3("05 177B8A2A 0FD6A4FF 55CCA7B8 A1E21C88 BD53B2C1")
a3 = 1
while pow(a3 ** 3 + b2 * a3 + b3, (b23 - 1)
    a3 += 1
b25 = pow(a3 ** 3 + b2 * a3 + b3, (b23 + 1)
b26 = [a3, b25]
with open(sys.argv[1], 'r') as f:
    b27 = f.read()
b6 = [fonk2('y0'), fonk2('y1')]
b28 = [fonk2('s0'), fonk2('s1')]
print("Public key X:", b6[0] % b23)
print("Public key Y:", b6[1] % b23)
print("Signature X:", b28[0])
print("Signature Y:", b28[1])
print()
print("Verification of signature:", fonk11(b26, b28, b6, b28[1], b27))
b29 = random.randint(2, b24 - 1)
b30 = fonk8(b26, b29)
b31 = fonk10(b26, b27, b29)
print("Verification of ECDSA signature:", fonk9(b26, b31, b30, b31[1], b27))
b32 = fonk5('kk1_' + str(random.randint(2, b24 - 1)))
b33 = fonk12(b26, b27, b32)
fonk1(b33[0], 's0')
fonk1(b33[1], 's1')
a4 = 0
while 2 ** a4 < b24:
    a4 += 1
print("\nMore security checks")
print("Bit length:", a4)
print("\nCheck b23:", pow(7, b23 - 1, b23) == 1)
print("Prime order:", pow(7, b24 - 1, b24) == 1)
print("Period:", b26 = = fonk8(b26, b24 + 1))