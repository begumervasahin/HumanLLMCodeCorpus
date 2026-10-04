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
def fonk2(letter_numb, b12):
    return '{0:0b}'.format(letter_numb).zfill(b12)
def fonk3(b20, p, b5, b21, b14):
    b9 = p * b5
    b10 = (p - 1) * (b5 - 1)
    _, _, b11 = fonk1(b10, b21)
    b12 = int(math.log(len(b1), 2)) + 1
    b13 = int(math.log(b9 - 1, 2))
    if b14 = = 'b21':
        b15 = ''.join(fonk2(b1.find(letter) + 1, b12) for letter in b20)
        b16 = [
            (int(b15[i * b13: (i + 1) * b13], 2) ** b21) % b9
            for i in range((len(b15) + b13 - 1)
        ]
        return b16
    elif b14 = = 'b17':
        b17 = b11 % b10
        b18 = [(code ** b17) % b9 for code in b20]
        b15 = ''.join(
            fonk2(num, b13) if i < len(b18) - 1
            else fonk2(num, len(b18) * b12 - len(b15))
            for i, num in enumerate(b18)
        )
        b19 = ''.join(
            b1[int(b15[i * b12: (i + 1) * b12], 2) - 1]
            for i in range(len(b15)
        )
        return b19
def fonk4():
    b20 = 'wonderfull'
    b14 = 'b21'
    p, b5, b21 = 17, 31, 7
    b22 = fonk3(b20, p, b5, b21, b14)
    print(b22)
if b23 = = "__main__":
    fonk4()