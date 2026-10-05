
b1 = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
def fonk1(b1):
    for i in range(len(b1)):
        b2 = i
        for j in range(i + 1, len(b1)):
            if b1[b2] > b1[j]:
                b2 = j
        b3 = b1[i]
        b1[i] = b1[b2]
        b1[b2] = b3
    return b1
print(fonk1(b1))