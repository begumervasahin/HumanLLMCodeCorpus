
a1 = 0
def fonk1(b6, b4, i):
    global a1
    a2 = 0
    b1 = i
    b2 = 2 * i + 1
    b3 = 2 * i + 2
    if b2 < b4 and b6[i] < b6[b2]:
        b1 = b2
        a2 += 1
    if b3 < b4 and b6[b1] < b6[b3]:
        b1 = b3
        a2 += 1
    if b1 != i:
        b6[i], b6[b1] = b6[b1], b6[i]
        a1 += 1
        a2 += fonk1(b6, b4, b1)
    return a2
def fonk2(b6):
    global a1
    a1 = 0
    b4 = len(b6)
    a3 = 0
    for i in range(b4
        a3 += fonk1(b6, b4, i)
    for i in range(b4 - 1, 0, -1):
        b6[i], b6[0] = b6[0], b6[i]
        a1 += 1
        a3 += fonk1(b6, i, 0)
    return f"HEAP SORT:\nComparisons: {a3}\nSwaps: {a1}"
if b5 = = "__main__":
    b6 = [4, 10, 3, 5, 1]
    b7 = fonk2(b6)
    print(b7)
    print(f"Sorted array: {b6}")