import random
a1 = 2
b1 = 8 * a1
def fonk1():
    b2 = [0] * b1
    for i in range(b1):
        b3 = sum(b2[:i])
        b2[i] = b3 + random.randint(1, 5)
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
    gcd, x, b16 = fonk6(A, M)
    if x < 0:
        x += M
    return x
def fonk8(char):
    b17 = "{0:b6}".format(ord(char))
    return b17.zfill(8)
def fonk9(chars):
    b18 = ''.join(fonk8(c)[::-1] for c in chars)
    return sum(int(bit) * weight for bit, weight in zip(b18, b5))
def fonk10(number):
    b19 = (number * a3) % b4
    b20 = ""
    for sik_i in b2[::-1]:
        if b19 >= sik_i:
            b20 = "1" + b20
            b19 -= sik_i
        else:
            b20 = "0" + b20
    b20 = b20.zfill(8 * a1)
    b21 = chr(fonk11(b20[:8]))
    b22 = chr(fonk11(b20[8:]))
    return b21 + b22
def fonk11(bitstring):
    return int(bitstring, 2)
def fonk12(message):
    if len(message) % a1 != 0:
        message += " " * (a1 - len(message) % a1)
    b23 = [fonk9(message[i:i + a1]) for i in range(0, len(message), a1)]
    return b23
def fonk13(crypto_list):
    b24 = ''.join(fonk10(num) for num in crypto_list)
    return b24
if b25 = = "__main__":
    b26 = fonk12("ciao, io mi chiamo francesco ")
    print("Encrypted:", b26)
    b27 = fonk13(b26)
    print("Decrypted:", b27)
    try:
        with open("b23", "b13") as file:
            b28 = [int(line.strip(), 16) for line in file]
            b29 = fonk13(b28)
            print("Decrypted from file:", b29)
    except FileNotFoundError:
        print("The file 'b23' was not found.")