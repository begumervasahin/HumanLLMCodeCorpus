def fonk1(b4):
    b1 = len(b4)
    for i in range(b1):
        b2 = i
        for j in range(i + 1, b1):
            if b4[b2] > b4[j]:
                b2 = j
        if i != b2:
            b3 = b4[i]
            b4[i] = b4[b2]
            b4[b2] = b3
    return b4
b4 = [6, 3, 1, 9, 2, 5, 8, 7, 4]
print(fonk1(b4))