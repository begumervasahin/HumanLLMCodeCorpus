b1 = [100, 48, 70, 29, 2, 17]
def fonk1(b1):
    for i in range(len(b1)):
        b2 = i
        for j in range(i + 1, len(b1)):
            if b1[b2] > b1[j]:
                b2 = j
        b1[i], b1[b2] = b1[b2], b1[i]
        print(b1)
fonk1(b1)