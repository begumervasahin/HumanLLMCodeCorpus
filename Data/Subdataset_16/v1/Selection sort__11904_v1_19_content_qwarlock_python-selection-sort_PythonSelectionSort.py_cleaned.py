def fonk1(b3):
    b1 = len(b3)
    for i in range(b1):
        b2 = i
        for j in range(i + 1, b1):
            if b3[j] < b3[b2]:
                b2 = j
        b3[i], b3[b2] = b3[b2], b3[i]
b3 = [6, 5, 8, 4, 3, 2, 8, 9, 10, 15, 0]
print("Original list:", b3)
fonk1(b3)
print("Sorted list:", b3)