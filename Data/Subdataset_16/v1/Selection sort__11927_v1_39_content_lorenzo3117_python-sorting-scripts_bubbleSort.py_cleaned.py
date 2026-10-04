def fonk1(b4):
    b1 = len(b4)
    a1 = 0
    a2 = 0
    for i in range(b1):
        b2 = False
        for j in range(0, b1 - i - 1):
            a1 += 1
            if b4[j] > b4[j + 1]:
                a2 += 1
                b4[j], b4[j + 1] = b4[j + 1], b4[j]
                b2 = True
        if not b2:
            break
    return f"\nBubble Sort:\nComparisons: {a1}\nSwaps: {a2}"
if b3 = = "__main__":
    b4 = [64, 34, 25, 12, 22, 11, 90]
    print("Array before sorting:")
    print(b4)
    b5 = fonk1(b4)
    print("Sorted array is:")
    print(b4)
    print(b5)