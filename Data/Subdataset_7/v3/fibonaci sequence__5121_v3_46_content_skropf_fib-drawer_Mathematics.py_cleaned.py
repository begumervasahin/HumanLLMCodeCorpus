b1 = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
    9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G',
    17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O',
    25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W',
    33: 'X', 34: 'Y', 35: 'Z'
}
def fonk1(start, base):
    while True:
        yield fonk2(start, base)
        start *= 2
def fonk2(b3, base, b2 = ''):
    if b3:
        if 2 <= base <= 36:
            return fonk2(b3
        else:
            return fonk2(b3
    return b2
def fonk3(b3, base, b2 = 0):
    b3 = str(b3)
    if b3:
        if 2 <= base <= 36:
            return fonk3(b3[:-1], base, b2 + b1[b3[-1]] * (base ** len(b3[:-1])))
        else:
            return fonk3('.'.join(b3.split('.')[:-1]), base, b2 + int(b3.split('.')[-1]) * (base ** len(b3.split('.')[:-1])))
    return b2
def fonk4(b3, base):
    b4 = fonk3(b3, base)
    while b4 >= base:
        b4 = sum([b1[elem] for elem in str(b4)])
    return b4
if b5 = = "__main__":
    b6 = fonk1(1, 2)
    for _ in range(10):
        print(next(b6))
    print(fonk2(123, 16))
    print(fonk3('7B', 16))
    print(fonk4(789, 10))