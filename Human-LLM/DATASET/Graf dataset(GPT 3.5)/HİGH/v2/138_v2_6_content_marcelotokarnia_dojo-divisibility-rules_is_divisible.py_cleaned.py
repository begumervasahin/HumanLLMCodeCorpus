
def fonk1(b4):
    a1 = 0
    while True:
        yield (-1) ** a1
        a1 += 1
def fonk2(b2, b4):
    b1 = fonk1(b4)
    a2 = 0
    b2 = str(b2)[::-1]
    for digit in b2:
        b3 = next(b1)
        a2 += int(digit) * b3
        if abs(a2) > 3 * b4:
            a2 %= 3 * b4
    return a2 % b4 = = 0
a3 = 123456
a4 = 7
b5 = fonk2(a3, a4)
print(b5)
