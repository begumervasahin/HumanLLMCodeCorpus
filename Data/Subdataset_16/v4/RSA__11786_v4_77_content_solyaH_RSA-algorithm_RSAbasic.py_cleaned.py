import math
b1 = "abcdefghijklmnopqrstuvwxyz"
def fonk1(a, b2):
    if b2 = = 0:
        return a, 1, 0
    x2, x1, y2, b3 = 1, 0, 0, 1
    while b2 > 0:
        b4 = a
        b5 = a - b4 * b2
        x, b6 = x2 - b4 * x1, y2 - b4 * b3
        a, b2 = b2, b5
        x2, x1, y2, b3 = x1, x, b3, b6
    return a, x2, y2
def fonk2(letter_num, b10):
    return '{0:0b}'.format(letter_num).zfill(b10)
def fonk3(b18, p, b4, b19, b12):
    b7 = p * b4
    b8 = (p - 1) * (b4 - 1)
    gcd, u, b9 = fonk1(b8, b19)
    b10 = int(math.log(len(b1), 2)) + 1
    b11 = int(math.log(b7 - 1, 2))
    if b12 = = 'b19':
        b13 = ''.join(fonk2(b1.find(letter) + 1, b10) for letter in b18)
        b14 = [(int(b13[i:i + b11], 2) ** b19) % b7
                       for i in range(0, len(b13), b11)]
        return b14
    elif b12 = = 'b15':
        b15 = b9 % b8
        b16 = [(code ** b15) % b7 for code in b18]
        b13 = ''.join(fonk2(num, b11) for num in b16)
        b17 = ''.join(b1[int(b13[i:i + b10], 2) - 1]
                               for i in range(0, len(b13), b10))
        return b17
def fonk4():
    b18 = 'wonderfull'
    b12 = 'b19'
    p, b4, b19 = 17, 31, 7
    b20 = fonk3(b18, p, b4, b19, b12)
    print(b20)
if b21 = = "__main__":
    fonk4()