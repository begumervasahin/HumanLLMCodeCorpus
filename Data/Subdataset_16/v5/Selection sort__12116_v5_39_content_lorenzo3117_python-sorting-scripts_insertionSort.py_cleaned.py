def fonk1(b3):
    a1 = 0
    a2 = 0
    for i in range(1, len(b3)):
        b1 = b3[i]
        b2 = i - 1
        a1 += 1
        while b2 >= 0 and b1 < b3[b2]:
            b3[b2 + 1] = b3[b2]
            b2 -= 1
            a1 += 1
            a2 += 1
        b3[b2 + 1] = b1
    return f"INSERTION SORT:\nComparisons: {a1}\nSwaps: {a2}"
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