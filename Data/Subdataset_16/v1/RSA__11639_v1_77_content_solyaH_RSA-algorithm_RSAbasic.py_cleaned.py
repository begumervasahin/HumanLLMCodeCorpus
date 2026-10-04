import math
b1 = "abcdefghijklmnopqrstuvwxyz"
def fonk1(a, b3):
    b20, b7, b2 = 0, 1, 0
    if b3 = = 0:
        return b20, b7, b2
    x2, b8, y2, b4 = 1, 0, 0, 1
    while b3 > 0:
        b5 = a
        b6 = a - b5 * b3
        b7 = x2 - b5 * b8
        b2 = y2 - b5 * b4
        a, b3 = b3, b6
        x2, b8 = b8, b7
        y2, b4 = b4, b2
    b20, b7, b2 = a, x2, y2
    return b20, b7, b2
def fonk2(b16, b12):
    return '{0:0b}'.format(b16).zfill(b12)
def fonk3(b24, a1, b5, a2, b14):
    b9 = a1 * b5
    b10 = (a1 - 1) * (b5 - 1)
    smt, u, b11 = fonk1(b10, a2)
    b12 = int(math.log(len(b1), 2)) + 1
    b13 = int(math.log(b9 - 1, 2))
    if b14 = = 'a2':
        b15 = ''
        for letter in b24:
            b16 = b1.find(letter) + 1
            b15 += fonk2(b16, b12)
        b17 = []
        b18 = len(b15)
        for b21 in range(b18):
            b19 = int(b15[b13 * b21 : b13 * (b21 + 1)], 2)
            b17.append((b19 ** a2) % b9)
        return b17
    elif b14 = = 'b20':
        b20 = b11 % b10
        b19 = [(code ** b20) % b9 for code in b24]
        b15 = ''
        for b21 in range(len(b19)):
            if b21 = = len(b19) - 1:
                b22 = int(b13 * (len(b19) - 1) / b12) + 1
                b15 += fonk2(b19[b21], b22 * b12 - len(b15))
            else:
                b15 += fonk2(b19[b21], b13)
        b23 = ''
        b18 = len(b15)
        for b21 in range(b18):
            b16 = int(b15[b12 * b21 : b12 * (b21 + 1)], 2)
            b23 += b1[b16 - 1]
        return b23
def fonk4():
    b24 = 'wonderfull'
    b14 = 'a2'
    a1 = 17
    b5 = 31
    a2 = 7
    b25 = fonk3(b24, a1, b5, a2, b14)
    print(b25)
if b26 = = "__main__":
    fonk4()