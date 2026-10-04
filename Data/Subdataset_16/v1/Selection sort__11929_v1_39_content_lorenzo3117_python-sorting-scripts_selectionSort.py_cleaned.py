def fonk1(b3):
    a1 = 0
    a2 = 0
    for i in range(len(b3) - 1):
        b1 = i
        for j in range(i + 1, len(b3)):
            a1 += 1
            if b3[j] < b3[b1]:
                b1 = j
        if b1 != i:
            b3[i], b3[b1] = b3[b1], b3[i]
            a2 += 1
    return f"SELECTION SORT:\nComparisons: {a1}\nSwaps: {a2}"
if b2 = = "__main__":
    b3 = [64, 25, 12, 22, 11]
    print("Array before sorting:")
    print(b3)
    b4 = fonk1(b3)
    print("Sorted array is:")
    print(b3)
    print(b4)