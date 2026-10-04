def fonk1(b3):
    b1 = len(b3)
    for step in range(b1):
        b2 = step
        for i in range(step + 1, b1):
            if b3[i] < b3[b2]:
                b2 = i
        b3[step], b3[b2] = b3[b2], b3[step]
    print("Sorted b3:", b3)
    print("Total number of b3:", b1)
b3 = [64, 25, 12, 22, 11]
fonk1(b3)