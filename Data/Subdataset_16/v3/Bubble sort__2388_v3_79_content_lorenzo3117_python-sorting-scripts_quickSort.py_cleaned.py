import time
a1 = 0
a2 = 0
def fonk1(arr):
    global a1, a2
    a1, a2 = 0, 0
    b1 = time.time()
    b2 = fonk2(arr)
    b3 = time.time()
    print("QUICK SORT")
    print(f"Comparisons: {a1}")
    print(f"Swaps: {a2}")
    print(f"Time elapsed: {b3 - b1:.4f} seconds\n")
    return b2
def fonk2(b8):
    global a1, a2
    if len(b8) <= 1:
        return b8
    b4 = b8[len(b8)
    less, equal, b5 = [], [], []
    for b6 in b8:
        a1 += 1
        if b6 < b4:
            less.append(b6)
        elif b6 = = b4:
            equal.append(b6)
        else:
            b5.append(b6)
    a2 += 1
    return fonk2(less) + equal + fonk2(b5)
if b7 = = "__main__":
    b8 = [12, 11, 13, 5, 6, 7]
    print("Original b8:", b8)
    b9 = fonk1(b8)
    print("Sorted b8:", b9)