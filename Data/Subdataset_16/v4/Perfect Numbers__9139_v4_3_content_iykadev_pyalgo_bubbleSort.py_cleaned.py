def fonk1(b1):
    for passnum in range(len(b1) - 1, 0, -1):
        for i in range(passnum):
            if b1[i] > b1[i + 1]:
                b1[i, b1[i + 1] = b1[i + 1], b1[i]
b1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
fonk1(b1)
print(b1)
