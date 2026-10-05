def fonk1(b3):
    a1 = 0
    b1 = len(b3)
    for i in range(b1):
        b2 = False
        for j in range(0, b1 - i - 1):
            a1 += 1
            if b3[j] > b3[j + 1]:
                b3[j], b3[j + 1] = b3[j + 1], b3[j]
                b2 = True
        if not b2:
            break
    return a1
b3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original List:", b3)
a1 = fonk1(b3)
print("Sorted List:", b3)
print("Number of comparisons:", a1)