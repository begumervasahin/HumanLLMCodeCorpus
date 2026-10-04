def fonk1(b6, b4, i):
    b1 = i
    b2 = 2 * i + 1
    b3 = 2 * i + 2
    if b2 < b4 and b6[i] > b6[b2]:
        b1 = b2
    if b3 < b4 and b6[b1] > b6[b3]:
        b1 = b3
    if b1 != i:
        b6[i], b6[b1] = b6[b1], b6[i]
        fonk1(b6, b4, b1)
def fonk2(b6):
    b4 = len(b6)
    for i in range(b4
        fonk1(b6, b4, i)
    for i in range(b4 - 1, 0, -1):
        b6[i], b6[0] = b6[0], b6[i]
        fonk1(b6, i, 0)
if b5 = = "__main__":
    b6 = [12, 11, 13, 5, 6, 7]
    print("Original array:", b6)
    fonk2(b6)
    print("Sorted array:", b6)