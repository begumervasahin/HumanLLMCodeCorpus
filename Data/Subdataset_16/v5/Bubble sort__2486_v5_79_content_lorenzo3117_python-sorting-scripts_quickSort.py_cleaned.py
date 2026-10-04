import time
a1 = 0
a2 = 0
def fonk1(b8):
    global a1, a2
    a1 = 0
    a2 = 0
    b1 = time.time()
    b2 = fonk2(b8)
    b3 = time.time()
    print(f"QUICK SORT\nComparisons: {a1}\nSwaps: {a2}")
    print(f"Time elapsed: {b3 - b1:.4f} seconds\n")
    return b2
def fonk2(array):
    global a1, a2
    if len(array) <= 1:
        return array
    b4 = array[-1]
    less, equal, b5 = [], [], []
    for b6 in array:
        a1 += 1
        if b6 < b4:
            less.append(b6)
        elif b6 = = b4:
            equal.append(b6)
        else:
            b5.append(b6)
    a2 += len(less) + len(b5)
    return fonk2(less) + equal + fonk2(b5)
if b7 = = "__main__":
    b8 = [4, 10, 3, 5, 1]
    b9 = fonk1(b8)
    print(f"Sorted array: {b9}")