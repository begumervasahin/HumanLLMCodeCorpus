def fonk1(b2):
    a1 = 0
    a2 = 0
    for i in range(len(b2) - 1):
        b1 = i
        for j in range(i + 1, len(b2)):
            a1 += 1
            if b2[j] < b2[b1]:
                b1 = j
        if b1 != i:
            b2[i], b2[b1] = b2[b1], b2[i]
            a2 += 1
    return f"SELECTION SORT:\nComparisons: {a1}\nSwaps: {a2}"
def fonk2():
    b2 = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted array:")
    print(b2)
    b3 = fonk1(b2)
    print("Sorted array:")
    print(b2)
    print(b3)
if b4 = = "__main__":
    fonk2()