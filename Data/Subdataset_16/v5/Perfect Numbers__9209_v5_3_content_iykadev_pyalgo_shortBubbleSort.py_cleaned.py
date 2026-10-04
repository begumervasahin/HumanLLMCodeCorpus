def fonk1(b3):
    b1 = len(b3) - 1
    b2 = True
    while b1 > 0 and b2:
        b2 = False
        for i in range(b1):
            if b3[i] > b3[i + 1]:
                b3[i], b3[i + 1] = b3[i + 1], b3[i]
                b2 = True
        b1 -= 1
b3 = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
fonk1(b3)
print(b3)