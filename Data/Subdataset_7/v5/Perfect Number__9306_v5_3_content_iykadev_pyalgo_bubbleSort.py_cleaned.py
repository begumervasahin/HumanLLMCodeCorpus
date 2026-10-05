def fonk1(b2):
    b1 = len(b2)
    for i in range(b1 - 1, 0, -1):
        for j in range(i):
            if b2[j] > b2[j + 1]:
                b2[j], b2[j + 1] = b2[j + 1], b2[j]
b2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
fonk1(b2)
print(b2)