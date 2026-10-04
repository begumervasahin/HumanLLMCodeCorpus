def fonk1(b3):
    b1 = len(b3)
    for i in range(b1 - 1):
        b2 = i
        for j in range(i + 1, b1):
            if b3[j] < b3[b2]:
                b2 = j
        b3[i], b3[b2] = b3[b2], b3[i]
        print(b3)
b3 = [5, 3, 7, 2, 4, 1, 11, 8, 10, 9, 6]
fonk1(b3)
print("Sorted list:", b3)