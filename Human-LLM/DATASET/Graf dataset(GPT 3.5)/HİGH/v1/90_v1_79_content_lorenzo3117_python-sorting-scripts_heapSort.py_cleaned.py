a1 = 0
def fonk1(b5, b4, i):
    global a1
    a2 = 0
    b1 = i
    b2 = 2 * i + 1
    b3 = 2 * i + 2
    if b2 < b4 and b5[i] < b5[b2]:
        b1 = b2
    if b3 < b4 and b5[b1] < b5[b3]:
        b1 = b3
    if b1 != i:
        a2 += 1
        b5[i], b5[b1] = b5[b1], b5[i]
        a1 += 1
        a2 += fonk1(b5, b4, b1)
    return a2
def fonk2(b5):
    global a1
    b4 = len(b5)
    a2 = 0
    for i in range(b4, -1, -1):
        fonk1(b5, b4, i)
        a2 += fonk1(b5, i, 0)
    for i in range(b4-1, 0, -1):
        b5[i], b5[0] = b5[0], b5[i]
        a1 += 1
        a2 += fonk1(b5, i, 0)
    return "HEAP SORT:\nComparisons: " + str(a2) + "\nSwaps: " + str(a1)
b5 = [12, 11, 13, 5, 6, 7]
print("Unsorted array:", b5)
print(fonk2(b5.copy()))
print("Sorted array:", b5)