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
    print("Comparisons: " + str(a1))
    print("Swaps: " + str(a2))
    print("Time elapsed: " + str(b3 - b1) + " seconds\n")
    return b2
def fonk2(b8):
    global a1, a2
    less, equal, b4 = [], [], []
    if len(b8) > 1:
        b5 = b8[len(b8) - 1]
        for b6 in b8:
            if b6 < b5:
                a1 += 1
                less.append(b6)
            elif b6 = = b5:
                a1 += 1
                equal.append(b6)
            else:
                a1 += 1
                b4.append(b6)
        a2 += 1
        return fonk2(less) + equal + fonk2(b4)
    else:
        return b8
if b7 = = "__main__":
    b8 = [12, 11, 13, 5, 6, 7]
    print("Original b8:", b8)
    b9 = fonk1(b8)
    print("Sorted b8:", b9)