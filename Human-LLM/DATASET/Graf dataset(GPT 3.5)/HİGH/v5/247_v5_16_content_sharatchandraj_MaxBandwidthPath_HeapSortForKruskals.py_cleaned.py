def fonk1(b5, b4, i):
    b1 = i
    b2 = 2 * i + 1
    b3 = 2 * i + 2
    if b2 < b4 and b5[i] < b5[b2]:
        b1 = b2
    if b3 < b4 and b5[b1] < b5[b3]:
        b1 = b3
    if b1 != i:
        b5[i], b5[b1] = b5[b1], b5[i]
        fonk1(b5, b4, b1)
def fonk2(b5):
    b4 = len(b5)
    for i in range(b4
        fonk1(b5, b4, i)
    for i in range(b4 - 1, 0, -1):
        b5[i], b5[0] = b5[0], b5[i]
        fonk1(b5, i, 0)
b5 = [12, 11, 13, 5, 6, 7]
fonk2(b5)
print("Sorted array is:", b5)