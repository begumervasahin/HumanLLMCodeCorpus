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
def fonk4(b6, a3, b2):
    b3 = []
    for ai in b2:
        b3.append((ai * b6) % a3)
    return b3
def fonk5(A, M):
    gcd, b12, b7 = fonk6(A, M)
    if b12 < 0:
        b12 += M
    return b12
def fonk6(a, b4):
    b8 = 0; old_s = 1
    b9 = 1; old_t = 0
    b10 = b4; old_r = a
    while b10 != 0:
        b11 = old_r / b10
        old_r, b10 = b10, old_r - b11 * b10
        old_s, b8 = b8, old_s - b11 * b8
        old_t, b9 = b9, old_t - b11 * b9
    return [old_r, old_s, old_t]
def fonk7(b12):
    b12 = ord(b12)
    b13 = "{0:b4}".format(b12)
    if len(b13) <= 7:
        b13 = '0' * (8 - len(b13)) + b13
    return b13
def fonk8(chars):
    b14 = ""
    for i in range(len(chars)):
        b14 = fonk7(chars[i])[::-1] + b14
    return sum([int(b12) * b7 for b12, b7 in zip(list(b14), b3)])
def fonk9(number):
    b15 = ""
    b16 = (number * a2) % a3
    for sik_i in b2[::-1]:
        if b16 >= sik_i:
            b15 = "1" + b15
            b16 -= sik_i
        else:
            b15 = "0" + b15
    b15 = b15[::-1]
    char1, b17 = chr(fonk10(b15[:8])), chr(fonk10(b15[8:]))
    return char1 + b17
def fonk10(bitstring):
    a4 = 0
    for bit in list(bitstring):
        a4 = (a4 << 1) | int(bit)
    return a4
def fonk11(message):
    b18 = []
    b19 = []
    if len(message) % a1 != 0:
        message += " " * (a1 - len(message) % a1)
    for i in range(0, len(message), a1):
        b18.append(message[i:i + a1])
    for chars in b18:
        b19.append(fonk8(chars))
    return b19
def fonk12(crypto_list):
    b20 = ""
    for num in crypto_list:
        b20 += fonk9(num)
    return b20
print(fonk12(fonk11("ciao, io mi chiamo francesco ")))
b21 = open("b19", "b10").readlines()
b22 = ""
for i in b21:
    b22 += fonk12([int(i, 16)])
print(b22)