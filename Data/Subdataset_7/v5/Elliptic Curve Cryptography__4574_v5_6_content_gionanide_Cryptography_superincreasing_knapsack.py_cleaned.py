from random import randint
a1 = 2
a2 = 8
b1 = a1 * a2
def fonk1():
    b2 = [0] * b1
    for i in range(b1):
        b2[i] = sum(b2[:i]) + randint(1, 5)
    return b2
b3 = [1, 4, 6, 12, 25, 50, 103, 205, 409, 820, 1639, 3276, 6554, 13106, 26212, 52425]
MODULUS_M, b4 = 89, 104848
a3 = 87177
def fonk2(a, b5):
    while b5 != 0:
        a, b5 = b5, a % b5
    return a
def fonk3(a, b5):
    return fonk2(a, b5) == 1
def fonk4():
    b6 = sum(b3)
    b7 = randint(41, 100)
    a4 = 0
    while a4 < b6:
        if fonk3(b7, b6 + 1):
            a4 = b6 + 1
    return b7, a4
def fonk5(b7, a4, b2):
    b8 = []
    for ai in b2:
        b8.append((ai * b7) % a4)
    return b8
def fonk6(A, M):
    gcd, x, b9 = fonk7(A, M)
    if x < 0:
        x += M
    return x
def fonk7(a, b5):
    b15, b10 = 0, 1
    b16, b11 = 1, 0
    b14, b12 = b5, a
    while b14 != 0:
        b13 = b12
        b12, b14 = b14, b12 - b13 * b14
        b10, b15 = b15, b10 - b13 * b15
        b11, b16 = b16, b11 - b13 * b16
    return b12, b10, b11
def fonk8(character):
    b17 = ord(character)
    b18 = "{0:b5}".format(b17)
    if len(b18) <= a2 - 1:
        b18 = '0' * (a2 - len(b18)) + b18
    return b18
def fonk9(character):
    b19 = ""
    for char in character:
        b19 = fonk8(char)[::-1] + b19
    return sum([int(x) * b9 for x, b9 in zip(list(b19), GENERAL_KNAPSACK)])
def fonk10(number):
    b20 = ""
    b21 = (number * a3) % b4
    for value in b3[::-1]:
        if b21 >= value:
            b20 = "1" + b20
            b21 -= value
        else:
            b20 = "0" + b20
    b20 = b20[::-1]
    b22 = chr(fonk11(b20[:a2]))
    b23 = chr(fonk11(b20[a2:]))
    return b22 + b23
def fonk11(bitstring):
    a5 = 0
    for bit in list(bitstring):
        a5 = (a5 << 1) | int(bit)
    return a5
def fonk12(message):
    b24 = []
    if len(message) % a1 != 0:
        message += " " * (a1 - len(message) % a1)
    for i in range(0, len(message), a1):
        b24.append(fonk9(message[i:i + a1]))
    return b24
def fonk13(crypto_list):
    b25 = ""
    for num in crypto_list:
        b25 += fonk10(num)
    return b25
print(fonk13(fonk12("ciao, io mi chiamo francesco ")))
with open("encrypted", "b14") as encrypted_file:
    b26 = encrypted_file.readlines()
    b27 = ""
    for line in b26:
        b27 += fonk13([int(line, 16)])
    print(b27)