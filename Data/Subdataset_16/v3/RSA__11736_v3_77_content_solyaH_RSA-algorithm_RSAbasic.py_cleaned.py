import math
b1 = "abcdefghijklmnopqrstuvwxyz"
def fonk1(a, b2):
    if b2 = = 0:
        return a, 1, 0
    x2, b3 = 1, 0
    y2, b4 = 0, 1
    while b2 > 0:
        b5 = a
        b6 = a - b5 * b2
        b7 = x2 - b5 * b3
        b8 = y2 - b5 * b4
        a, b2 = b2, b6
        x2, b3 = b3, b7
        y2, b4 = b4, b8
    return a, x2, y2
def fonk2(number, length):
    return format(number, '0{}b2'.format(length))
def fonk3(b19, p, b5, b21):
    b9 = p * b5
    b10 = (p - 1) * (b5 - 1)
    _, _, b11 = fonk1(b10, b21)
    b12 = int(math.log2(len(b1))) + 1
    b13 = int(math.log2(b9 - 1))
    b14 = ''.join(fonk2(b1.index(char) + 1, b12) for char in b19)
    b15 = [
        (int(b14[i * b13: (i + 1) * b13], 2) ** b21) % b9
        for i in range((len(b14) + b13 - 1)
    ]
    return b15
def fonk4(b23, p, b5, b21):
    b9 = p * b5
    b10 = (p - 1) * (b5 - 1)
    _, _, b11 = fonk1(b10, b21)
    b16 = b11 % b10
    b13 = int(math.log2(b9 - 1))
    b12 = int(math.log2(len(b1))) + 1
    b17 = [(code ** b16) % b9 for code in b23]
    b14 = ''.join(
        fonk2(num, b13) if i < len(b17) - 1
        else fonk2(num, len(b17) * b12 - len(b14))
        for i, num in enumerate(b17)
    )
    b18 = ''.join(
        b1[int(b14[i * b12: (i + 1) * b12], 2) - 1]
        for i in range(len(b14)
    )
    return b18
def fonk5():
    b19 = 'wonderfull'
    b20 = 'b21'
    p, b5, b21 = 17, 31, 7
    if b20 = = 'b21':
        b22 = fonk3(b19, p, b5, b21)
    elif b20 = = 'b16':
        b23 = fonk3(b19, p, b5, b21)
        b22 = fonk4(b23, p, b5, b21)
    print(b22)
if b24 = = "__main__":
    fonk5()