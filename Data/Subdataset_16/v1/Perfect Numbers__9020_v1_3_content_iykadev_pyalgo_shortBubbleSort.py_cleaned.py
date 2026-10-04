def fonk1(b4):
    b1 = True
    b2 = len(b4) - 1
    while b2 > 0 and b1:
        b1 = False
        for i in range(b2):
            if b4[i] > b4[i + 1]:
                b1 = True
                b3 = b4[i]
                b4[i] = b4[i + 1]
                b4[i + 1] = b3
        b2 = b2 - 1
b4 = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
fonk1(b4)
print(b4)
