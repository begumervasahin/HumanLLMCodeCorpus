from random import randint
a1 = 2
b1 = 8 * a1
a2 = 87177
b2 = [1, 4, 6, 12, 25, 50, 103, 205, 409, 820, 1639, 3276, 6554, 13106, 26212, 52425]
b3 = [89, 356, 534, 1068, 2225, 4450, 9167, 18245, 36401, 72980, 41023, 81868, 59066, 13106, 26212, 52513]
def fonk1(a, b4):
    while b4 != 0:
        a, b4 = b4, a % b4
    return a
def fonk2(a, b4):
    return fonk1(a, b4) == 1
def fonk3():
    b5 = sum(b2)
    b6 = randint(41, 100)
    a3 = 0
    while a3 < b5:
        if fonk2(b6, b5 + 1):
            a3 = b5 + 1
    return b6, a3
def fonk4(b6, a3, sik):
    b7 = []
    for ai in sik:
        b7.append((ai * b6) % a3)
    return b7
def fonk5(A, M):
    gcd, x, b8 = fonk6(A, M)
    if x < 0:
        x += M
    return x
def fonk6(a, b4):
    b9 = 0; old_s = 1
    b10 = 1; old_t = 0
    b11 = b4; old_r = a
    while b11 != 0:
        b12 = old_r / b11
        old_r, b11 = b11, old_r - b12 * b11
        old_s, b9 = b9, old_s - b12 * b9
        old_t, b10 = b10, old_t - b12 * b10
    return [old_r, old_s, old_t]
def fonk7(character):
    b13 = ord(character)
    b14 = "{0:b4}".format(b13)
    if len(b14) <= 7:
        b14 = '0' * (8 - len(b14)) + b14
    return b14
def fonk8(character):
    b14 = ""
    for i in range(len(character)):
        b14 = fonk7(character[i])[::-1] + b14
    return sum([int(x) * b8 for x, b8 in zip(list(b14), b3)])
def fonk9(number):
    b15 = ""
    b16 = (number * a2) % b1
    for sik_i in b2[::-1]:
        if b16 >= sik_i:
            b15 = "1" + b15
            b16 -= sik_i
        else:
            b15 = "0" + b15
    b15 = b15[::-1]
    char1, b17 = chr(fonk10(b15[:8])), chr(fonk10(b15[8:]))
    return char1 + b17
def fonk10(binary_string):
    a4 = 0
    for bit in list(binary_string):
        a4 = (a4 << 1) | int(bit)
    return a4
def fonk11(message):
    b18 = []
    b19 = []
    if len(message) % a1 != 0:
        message += " " * (a1 - len(message) % a1)
    for i in range(0, len(message), a1):
        b18.append(message[i:i + a1])
    for block in b18:
        b19.append(fonk8(block))
    return b19
def fonk12(crypto_list):
    b20 = ""
    for num in crypto_list:
        b20 += fonk9(num)
    return b20
print(fonk12(fonk11("ciao, io mi chiamo francesco ")))
with open("b19", "b11") as fin:
    b21 = ""
    for line in fin:
        b21 += fonk12([int(line, 16)])
    print(b21)