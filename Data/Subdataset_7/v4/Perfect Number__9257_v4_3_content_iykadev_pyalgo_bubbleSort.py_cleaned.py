def fonk1(b3):
    b1 = len(b3)
    for passnum in range(b1 - 1, 0, -1):
        for i in range(passnum):
            if b3[i] > b3[i + 1]:
                b2 = b3[i]
                b3[i] = b3[i + 1]
                b3[i + 1] = b2
b3 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
fonk1(b3)
print(b3)