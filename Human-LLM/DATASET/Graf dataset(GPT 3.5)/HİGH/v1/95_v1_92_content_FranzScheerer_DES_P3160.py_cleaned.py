import random
import hashlib
def fonk1(a1, fnam):
    b1 = open(fnam, 'wb')
    while a1 > 0:
        b2 = a1 & 0xFF
        a1 >>= 8
        b1.write(bytes([b2]))
    b1.close()
def fonk2(fnam):
    b1 = open(fnam, 'rb')
    a1 = 0
    for c in reversed(b1.read()):
        a1 = (a1 << 8) ^ c
    b1.close()
    return a1
def fonk3(b8):
    a2 = 0
    for c in b8:
        if ord(c) < 58 and ord(c) >= 48:
            a2 = (a2 << 4) + ord(c) - 48
        elif ord(c) <= ord('b1') and ord(c) >= ord('b3'):
            a2 = (a2 << 4) + ord(c) - 87
        elif ord(c) <= ord('F') and ord(c) >= ord('A'):
            a2 = (a2 << 4) + ord(c) - 55
    return a2
def fonk4(b2, m):
    a3 = 0
    a4 = 1
    b3 = m
    while b2 != 1:
        b4 = b3
        b5 = b2
        b2 = b3 % b2
        b3 = b5
        b6 = a4
        a4 = a3 - b4 * a4
        a3 = b6
    if a4 < 0:
        a4 = a4 + m
    return a4
def fonk5(b8):
    b7 = hashlib.sha256(b8.encode(encoding='UTF-8', errors='strict')).hexdigest()
    a2 = 0
    for cx in b7:
        a2 = (a2 << 8) ^ ord(cx)
    return a2 % b25
def fonk6(b8, b3, b2):
    while pow(b8 ** 3 + b3 * b8 + b2, (b24 - 1)
        b8 = b8 + 1
    b9 = pow(b8 ** 3 + b3 * b8 + b2, (b24 + 1)
    return [b8 % b24, b9 % b24]
def fonk7(b27, Q):
    b10 = b27[0]
    b11 = Q[0]
    b12 = b27[1]
    b13 = Q[1]
    while b10 < b11:
        b10 = b10 + b24
    if b10 = = b11:
        a3 = ((3 * (b10 ** 2) + b3) * fonk4(2 * b12, b24)) % b24
    else:
        a3 = ((b12 - b13) * fonk4(b10 - b11, b24)) % b24
    b14 = a3 ** 2 - b10 - b11
    b15 = a3 * (b10 - b14) - b12
    return [b14 % b24, b15 % b24]
def fonk8(b27, a1):
    b16 = True
    b17 = b27
    if a1 < 0:
        b17[1] = b24 - b17[1]
        a1 = (-1) * a1
    b18 = b17
    while a1 > 0:
        if (a1 % 2 != 0):
            if b16:
                b17 = b18
                b16 = False
            else:
                b17 = fonk7(b17, b18)
        b18 = fonk7(b18, b18)
        a1 = a1
    return b17
def fonk9(G, a3, Y, b19, m):
    return b19 = = fonk5(str(fonk7(fonk8(G, a3), fonk8(Y, b19))[0]) + m)
def fonk10(G, m, S, Y):
    b20 = fonk4(S[0], b25)
    b21 = fonk5(m + str(S[1]))
    b22 = (b20 * b21) % b25
    b23 = (b20 * S[1]) % b25
    return fonk7(fonk8(G, b22), fonk8(Y, b23))[0] == S[1]
b24 = fonk3("05 177B8A2A 0FD6A4FF 55CDA06B 0924E125 F86CAD9B")
b3 = fonk3("04 3182D283 FCE38807 30C9A2FD D3F60165 29A166AF")
b2 = fonk3("02 0C61E945 9E53D887 1BCAADC2 DFC8AD52 25228035")
b25 = fonk3("05 177B8A2A 0FD6A4FF 55CCA7B8 A1E21C88 BD53B2C1")
a5 = 1
while pow(a5 ** 3 + b3 * a5 + b2, (b24 - 1)
    a5 = a5 + 1
b26 = pow(a5 ** 3 + b3 * a5 + b2, (b24 + 1)
b27 = [a5, b26]
b1 = open(sys.argv[1], 'r')
b28 = b1.read()
b1.close()
b9 = [fonk2('y0'), fonk2('b12')]
b29 = [fonk2('s0'), fonk2('s1')]
print("Public key: X:", b9[0] % b24)
print("Public key: Y:", b9[1] % b24)
print("Signature X:", b29[0])
print("Signature Y:", b29[1])
print("")
print("The verification of signature:", fonk9(b27, b29[0], b9, b29[1], b28))
b8 = random.randint(2, b25 - 1)
b30 = fonk8(b27, b8)
def fonk11(G, m, b8):
    b31 = fonk5(m + 'ecdsa')
    b32 = fonk8(G, b31)
    b21 = fonk5(m + str(b32[0]))
    a3 = (fonk4(b31, b25) * (b21 + b32[0] * b8)) % b25
    return [a3, b32[0]]
b29 = fonk11(b27, b28, b8)
print("The verification of ECDSA signature:", fonk10(b27, b28, b29, b30))
def fonk12(G, m, b8):
    b31 = fonk5(m + 'kk2')
    b32 = fonk8(G, b31)
    b19 = fonk5(str(b32[0]) + m)
    return [(b31 - b8 * b19) % b25, b19]
b33 = fonk5('kk1_' + str(random.randint(2, b25 - 1)))
b29 = fonk12(b27, b28, b33)
b9 = fonk8(b27, b33)
fonk1(b29[0], 's0')
fonk1(b29[1], 's1')
fonk1(b9[0], 'y0')
fonk1(b9[1], 'b12')
a6 = 0
while 2 ** a6 < b25:
    a6 = a6 + 1
print("\nMore security checks")
print("Bit length:", a6)
print("\nCheck b24:", pow(7, b24 - 1, b24) == 1)
print("Prime order:", pow(7, b25 - 1, b25) == 1)
print("Period:", b27 = = fonk8(b27, b25 + 1))