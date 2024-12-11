def fonk1(b2):
    for i in range(len(b2)):
        b1 = i
        for j in range(i, len(b2)):
            if b2[j] < b2[b1]:
                b1 = j
        b2[i], b2[b1] = b2[b1], b2[i]
        print(b2)
b2 = [5, 3, 7, 2, 4, 1, 11, 8, 10, 9, 6]
fonk1(b2)
print(b2)