def fonk1(b3):
    a1 = 0
    b1 = max(b3)
    b2 = b1 - a1 + 1
    print(a1, b1, b2)
    a2 = 0
    while b2 != 0:
        if a1 + a2 in b3:
            a2 += 1
            b2 -= 1
        else:
            return a1 + a2
    return a1 + a2
b3 = [0]
print(fonk1(b3))
b3 = [3, 0, 1]
print(fonk1(b3))
b3 = [0, 1]
print(fonk1(b3))
b3 = [9,6,4,2,3,5,7,0,1]
print(fonk1(b3))
