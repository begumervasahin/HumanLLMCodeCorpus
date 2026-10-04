import itertools
import random
from functools import reduce
a1 = 2
b1 = 8 * a1
def fonk1():
    b2 = [0] * b1
    for it_i in range(b1):
        b3 = sum(b2[:it_i])
        b2[it_i] = b3 + random.randint(1, 5)
    a2 = 0
    for i in range(len(b2) - 1):
        a2 += b2[i]
        if a2 > b2[i + 1]:
            print("NON b2")
    return b2
b2 = [1, 4, 6, 12, 25, 50, 103, 205, 409, 820, 1639, 3276, 6554, 13106, 26212, 52425]
b8, b4 = 89, 104848
a3 = 87177
b5 = [89, 356, 534, 1068, 2225, 4450, 9167, 18245, 36401, 72980, 41023, 81868, 59066, 13106, 26212, 52513]
def fonk2(a, b6):
    while b6 != 0:
        a, b6 = b6, a % b6
    return a
def fonk3(a, b6):
    return fonk2(a, b6) == 1
def fonk4():
    b7 = sum(b2)
    b8 = random.randint(41, 100)
    b4 = 0
    while b4 < b7:
        if fonk3(b8, b7 + 1):
            b4 = b7 + 1
    return b8, b4
def fonk5(b8, b4, b2):
    return [(ai * b8) % b4 for ai in b2]
def fonk6(a, b6):
    b14, b9 = 0, 1
    b15, b10 = 1, 0
    b13, b11 = b6, a
    while b13 != 0:
        b12 = b11
        b11, b13 = b13, b11 - b12 * b13
        b9, b14 = b14, b9 - b12 * b14
        b10, b15 = b15, b10 - b12 * b15
    return b11, b9, b10
def fonk7(A, M):
    gcd, b17, b16 = fonk6(A, M)
    if b17 < 0:
        b17 += M
    return b17
def fonk8(b17):
    b17 = ord(b17)
    b18 = "{0:b6}".format(b17)
    return b18.zfill(8)
def fonk9(chars):
    b19 = ''.join(fonk8(c)[::-1] for c in chars)
    return sum(int(bit) * weight for bit, weight in zip(b19, b5))
def fonk10(number):
    b20 = (number * a3) % b4
    b21 = ""
    for sik_i in b2[::-1]:
        if b20 >= sik_i:
            b21 = "1" + b21
            b20 -= sik_i
        else:
            b21 = "0" + b21
    b21 = b21.zfill(8 * a1)
    b22 = chr(fonk11(b21[:8]))
    b23 = chr(fonk11(b21[8:]))
    return b22 + b23
def fonk11(bitstring):
    return int(bitstring, 2)
def fonk12(message):
    if len(message) % a1 != 0:
        message += " " * (a1 - len(message) % a1)
    b24 = [fonk9(message[i:i + a1]) for i in range(0, len(message), a1)]
    return b24
def fonk13(crypto_list):
    b25 = ''.join(fonk10(num) for num in crypto_list)
    return b25
if b26 = = "__main__":
    b27 = fonk12("ciao, io mi chiamo francesco ")
    print("Encrypted:", b27)
    b28 = fonk13(b27)
    print("Decrypted:", b28)
    with open("b24", "b13") as file:
        b29 = [int(line.strip(), 16) for line in file]
        b30 = fonk13(b29)
        print("Decrypted from file:", b30)