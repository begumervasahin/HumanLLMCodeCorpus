import random
import hashlib
import sys
def fonk1(a1, filename):
    with open(filename, 'wb') as file:
        while a1 > 0:
            b1 = a1 & 0xFF
            a1 >>= 8
            file.write(bytes([b1]))
def fonk2(filename):
    with open(filename, 'rb') as file:
        a1 = 0
        for c in reversed(file.read()):
            a1 = (a1 << 8) ^ c
    return a1
def fonk3(b27):
    a2 = 0
    for c in b27:
        if '0' <= c <= '9':
            a2 = (a2 << 4) + ord(c) - ord('0')
        elif 'b2' <= c <= 'b24':
            a2 = (a2 << 4) + ord(c) - ord('b2') + 10
        elif 'A' <= c <= 'F':
            a2 = (a2 << 4) + ord(c) - ord('A') + 10
    return a2
def fonk4(b1, m):
    b7, b6, b2 = 0, 1, m
    while b1 != 1:
        b3 = b2
        b4 = b1
        b1 = b2 % b1
        b2 = b4
        b5 = b6
        b6 = b7 - b3 * b6
        b7 = b5
    if b6 < 0:
        b6 += m
    return b6
def fonk5(b27):
    b8 = hashlib.sha256(b27.encode(encoding='UTF-8')).hexdigest()
    a2 = 0
    for cx in b8:
        a2 = (a2 << 8) ^ ord(cx)
    return a2 % n4
def fonk6(b27, b2, b1):
    while pow(b27**3 + b2*b27 + b1, (prime - 1)
        b27 += 1
    b9 = pow(b27**3 + b2*b27 + b1, (prime + 1)
    return [b27 % prime, b9 % prime]
def fonk7(b23, Q):
    b11, x2, y1, b10 = b23[0], Q[0], b23[1], Q[1]
    while b11 < x2:
        b11 += prime
    if b11 = = x2:
        b7 = ((3*(b11**2) + b2) * fonk4(2*y1, prime)) % prime
    else:
        b7 = ((y1-b10) * fonk4(b11-x2, prime)) % prime
    b12 = b7**2 - b11 - x2
    b13 = b7 * (b11-b12) - y1
    return [b12 % prime, b13 % prime]
def fonk8(b23, a1):
    b14 = True
    b15 = b23
    if a1 < 0:
        b15[1] = prime - b15[1]
        a1 = (-1)*a1
    b16 = b15
    while a1 > 0:
        if (a1 % 2 != 0):
            if b14:
                b15 = b16
                b14 = False
            else:
                b15 = fonk7(b15, b16)
        b16 = fonk7(b16, b16)
        a1 = a1
    return b15
def fonk9(G, b7, Y, b17, m):
    return b17 = = fonk5(str(fonk7(fonk8(G, b7), fonk8(Y, b17))[0]) + m)
def fonk10(G, m, S, Y):
    b18 = fonk4(S[0], n4)
    b19 = fonk5(m + str(S[1]))
    b20 = (b18 * b19) % n4
    b21 = (b18 * S[1]) % n4
    return fonk7(fonk8(G, b20), fonk8(Y, b21))[0] == S[1]
a3 = 1
while pow(a3**3 + b2*a3 + b1, (prime - 1)
    a3 += 1
b22 = pow(a3**3 + b2*a3 + b1, (prime + 1)
b23 = [a3, b22]
b24 = open(sys.argv[1], 'r')
b25 = b24.read()
b24.close()
b9 = [fonk2('y0'), fonk2('y1')]
b26 = [fonk2('s0'), fonk2('s1')]
print("Public key: X:", b9[0] % prime)
print("Public key: Y:", b9[1] % prime)
print("Signature X:", b26[0])
print("Signature Y:", b26[1])
print()
print("The verification of signature:", fonk9(b23, b26[0], b9, b26[1], b25))
b27 = random.randint(2, n4 - 1)
b28 = fonk8(b23, b27)
b26 = ecdsa(b23, b25, b27)
print("The verification of ECDSA signature:", fonk10(b23, b25, b26, b28))
b29 = fonk5('kk1_' + str(random.randint(2, n4 - 1)))
b26 = signSchnorr(b23, b25, b29)
fonk1(b26[0], 's0')
fonk1(b26[1], 's1')
b9 = fonk8(b23, b29)
fonk1(b9[0], 'y0')
fonk1(b9[1], 'y1')
a4 = 0
while 2 ** a4 < n4:
    a4 += 1
print("\nMore security checks")
print("Bit length:", a4)
print("\nCheck prime:", pow(7, prime - 1, prime) == 1)
print("Prime order:", pow(7, n4 - 1, n4) == 1)
print("Period:", b23 = = fonk8(b23, n4 + 1))