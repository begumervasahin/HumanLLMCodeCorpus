def fonk1(b2):
    b1 = len(b2)
    for i in range(b1 - 1, 0, -1):
        a1 = 0
        for j in range(1, i + 1):
            if b2[j] > b2[a1]:
                a1 = j
        b2[i], b2[a1] = b2[a1], b2[i]
b2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
fonk1(b2)
print(b2)