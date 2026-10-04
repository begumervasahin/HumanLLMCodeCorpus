def fonk1(b3):
    b1 = True
    b2 = len(b3) - 1
    while b2 > 0 and b1:
        b1 = False
        for i in range(b2):
            if b3[i] > b3[i + 1]:
                b3[i], b3[i + 1] = b3[i + 1], b3[i]
                b1 = True
        b2 -= 1
b3 = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
fonk1(b3)
print(b3)