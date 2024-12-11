b1 = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
    9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G',
    17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O',
    25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W',
    33: 'X', 34: 'Y', 35: 'Z'
}
def fonk1(b2, base):
    while True:
        yield fonk2(b2, base)
        b2 = b2 * 2
def fonk2(b4, base, b3 = ''):
    if b4:
        if 2 <= base <= 36:
            return fonk2(int(b4 / base), base, b1[b4 % base] + b3)
        else:
            return fonk2(int(b4 / base), base, str(b4 % base) + '.' + b3 if b3 else str(b4 % base))
    return b3
def fonk3(b4, base, b3 = 0, power=0):
    b4 = str(b4)
    if b4:
        if 2 <= base <= 36:
            return fonk3(b4[:-1], base, b3 + list(b1.values()).index(b4[-1]) * (base ** power), power + 1)
        else:
            return fonk3('.'.join(b4.split('.')[:-1]), base, b3 + int(b4.split('.')[-1]) * (base ** power), power + 1)
    return b3
def fonk4(b4, base):
    if fonk3(b4, base) >= base:
        if 2 <= base <= 36:
            return fonk4(fonk2(sum([list(b1.values()).index(elem) for elem in list(str(b4))]), base), base)
        else:
            return fonk4(fonk2(sum([int(elem) for elem in str(b4).split('.')]), base), base)
    return b4
if b5 = = "__main__":
    b6 = fonk1(1, 2)
    for i in range(10):
        print(next(b6))
    print(fonk2(123, 16))
    print(fonk3('7B', 16))
    print(fonk4(789, 10))