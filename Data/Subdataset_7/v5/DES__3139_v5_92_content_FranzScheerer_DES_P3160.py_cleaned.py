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
    b12, b4, b2 = 0, 1, m
    while b3 != 1:
        q, b2, b3 = b2
        b12, b4 = b4, b12 - q * b4
    if b4 < 0:
        b4 += m
    return b4
def fonk5(b21):
    b5 = hashlib.sha256(b21.encode(encoding='UTF-8')).hexdigest()
    a2 = 0
    for char in b5:
        a2 = (a2 << 8) ^ ord(char)
    return a2
def fonk6(G, b12, Y, b13, b18):
    b6 = fonk4(b12[0], b15)
    b7 = fonk5(b18 + str(b12[1]))
    b8 = (b6 * b7) % b15
    b9 = (b6 * b12[1]) % b15
    return add_points(multiply_point(G, b8), multiply_point(Y, b9))[0] == b12[1]
def fonk7(G, b18, b21):
    b10 = fonk5(b18 + 'ecdsa')
    b11 = multiply_point(G, b10)
    b7 = fonk5(b18 + str(b11[0]))
    b12 = (fonk4(b10, b15) * (b7 + b11[0] * b21)) % b15
    return [b12, b11[0]]
def fonk8(G, b12, Y, b13, b18):
    return b13 = = fonk5(str(add_points(multiply_point(G, b12), multiply_point(Y, b13))[0]) + b18)
def fonk9(G, b18, b21):
    b10 = fonk5(b18 + 'kk2')
    b11 = multiply_point(G, b10)
    b13 = fonk5(str(b11[0]) + b18)
    return [(b10 - b21 * b13) % b15, b13]
b14 = fonk3("05 177B8A2A 0FD6A4FF 55CDA06B 0924E125 F86CAD9B")
b2 = fonk3("04 3182D283 FCE38807 30C9A2FD D3F60165 29A166AF")
b3 = fonk3("02 0C61E945 9E53D887 1BCAADC2 DFC8AD52 25228035")
b15 = fonk3("05 177B8A2A 0FD6A4FF 55CCA7B8 A1E21C88 BD53B2C1")
a3 = 1
while pow(a3 ** 3 + b2 * a3 + b3, (b14 - 1)
    a3 += 1
b16 = pow(a3 ** 3 + b2 * a3 + b3, (b14 + 1)
b17 = [a3, b16]
with open(sys.argv[1], 'r') as f:
    b18 = f.read()
b19 = [fonk2('y0'), fonk2('y1')]
b20 = [fonk2('s0'), fonk2('s1')]
print("Public key X:", b19[0] % b14)
print("Public key Y:", b19[1] % b14)
print("Signature X:", b20[0])
print("Signature Y:", b20[1])
print()
print("Verification of signature:", fonk8(b17, b20, b19, b20[1], b18))
b21 = random.randint(2, b15 - 1)
b22 = multiply_point(b17, b21)
b23 = fonk7(b17, b18, b21)
print("Verification of ECDSA signature:", fonk6(b17, b23, b22, b23[1], b18))
b24 = fonk5('kk1_' + str(random.randint(2, b15 - 1)))
b25 = fonk9(b17, b18, b24)
fonk1(b25[0], 's0')
fonk1(b25[1], 's1')
a4 = 0
while 2 ** a4 < b15:
    a4 += 1
print("\nMore security checks")
print("Bit length:", a4)
print("\nCheck b14:", pow(7, b14 - 1, b14) == 1)
print("Prime order:", pow(7, b15 - 1, b15) == 1)
print("Period:", b17 = = multiply_point(b17, b15 + 1))