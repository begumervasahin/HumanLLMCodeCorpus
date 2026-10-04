def fonk1(b3):
    a1 = 0
    a2 = 0
    b1 = len(b3)
    for i in range(b1 - 1):
        b2 = i
        for j in range(i + 1, b1):
            a1 += 1
            if b3[j] < b3[b2]:
                b2 = j
        if b2 != i:
            b3[i], b3[b2] = b3[b2], b3[i]
            a2 += 1
    return a1, a2
def fonk2():
    b3 = [64, 25, 12, 22, 11]
    print("Array before sorting:")
    print(b3)
    a1, a2 = fonk1(b3)
    print("Sorted array is:")
    print(b3)
    print(f"\nSELECTION SORT:\nComparisons: {a1}\nSwaps: {a2}")
if b4 = = "__main__":
    fonk2()