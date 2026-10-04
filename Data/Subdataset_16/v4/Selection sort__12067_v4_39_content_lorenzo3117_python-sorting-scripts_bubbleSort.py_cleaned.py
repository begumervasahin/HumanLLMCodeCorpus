def fonk1(b3):
    b1 = len(b3)
    a1 = 0
    a2 = 0
    for i in range(b1):
        b2 = False
        for j in range(0, b1 - i - 1):
            a1 += 1
            if b3[j] > b3[j + 1]:
                a2 += 1
                b3[j], b3[j + 1] = b3[j + 1], b3[j]
                b2 = True
        if not b2:
            break
    return f"\nBubble Sort:\nComparisons: {a1}\nSwaps: {a2}"
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