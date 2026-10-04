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
    return f"SELECTION SORT:\nComparisons: {a1}\nSwaps: {a2}"
def fonk2():
    b3 = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted array:")
    print(b3)
    b4 = fonk1(b3)
    print("Sorted array:")
    print(b3)
    print(b4)
if b5 = = "__main__":
    fonk2()