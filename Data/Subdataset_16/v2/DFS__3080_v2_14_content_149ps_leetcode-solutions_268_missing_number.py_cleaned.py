def fonk1(b4):
    a1 = 0
    b1 = max(b4)
    b2 = b1 - a1 + 1
    print(a1, b1, b2)
    a2 = 0
    while b2 != 0:
        b3 = a1 + a2
        if b3 in b4:
            a2 += 1
            b2 -= 1
        else:
            return b3
    return a1 + a2
b4 = [0]
print(fonk1(b4))
b4 = [3, 0, 1]
print(fonk1(b4))
b4 = [0, 1]
print(fonk1(b4))
b4 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(fonk1(b4))
