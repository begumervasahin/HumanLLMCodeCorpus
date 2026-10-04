def fonk1(b2):
    b1 = True
    while b1:
        b1 = False
        for i in range(len(b2) - 1):
            if b2[i] > b2[i + 1]:
                b2[i], b2[i + 1] = b2[i + 1], b2[i]
                b1 = True
b2 = [9, 8, 6, 6, 5, 4, 3, 2, 1, 0]
fonk1(b2)
print(b2)