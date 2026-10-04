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
def fonk2(letter_num, b8):
    return f'{letter_num:0{b8}b2}'
def fonk3(b17, p, b4, b19):
    b7 = p * b4
    b8 = int(math.log2(len(b1))) + 1
    b9 = int(math.log2(b7 - 1))
    b10 = ''.join(fonk2(b1.index(letter) + 1, b8) for letter in b17)
    b11 = [
        (int(b10[i:i + b9], 2) ** b19) % b7
        for i in range(0, len(b10), b9)
    ]
    return b11
def fonk4(b11, p, b4, b19):
    b7 = p * b4
    b12 = (p - 1) * (b4 - 1)
    gcd, _, b13 = fonk1(b12, b19)
    b14 = b13 % b12
    b8 = int(math.log2(len(b1))) + 1
    b9 = int(math.log2(b7 - 1))
    b15 = [(code ** b14) % b7 for code in b11]
    b10 = ''.join(fonk2(num, b9) for num in b15)
    b16 = ''.join(
        b1[int(b10[i:i + b8], 2) - 1]
        for i in range(0, len(b10), b8)
    )
    return b16
def fonk5():
    b17 = 'wonderfull'
    b18 = 'b19'
    p, b4, b19 = 17, 31, 7
    if b18 = = 'b19':
        b20 = fonk3(b17, p, b4, b19)
    elif b18 = = 'b14':
        b20 = fonk4(b17, p, b4, b19)
    print(b20)
if b21 = = "__main__":
    fonk5()