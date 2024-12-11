def fonk1(b3):
    for i in range(1, len(b3)):
        b1 = b3[i]
        b2 = i
        while b2 > 0 and b3[b2 - 1] > b1:
            b3[b2] = b3[b2 - 1]
            b2 = b2 - 1
        b3[b2] = b1
b3 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
fonk1(b3)
print(b3)