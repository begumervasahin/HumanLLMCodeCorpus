def fonk1(b3, l, r):
    if l < r:
        b1 = b3[l]
        b2 = l
        for i in range(l + 1, r):
            if b3[i] < b1:
                b2 = b2 + 1
                b3[b2], b3[i] = b3[i], b3[b2]
        b3[l], b3[b2] = b3[b2], b3[l]
        fonk1(b3, l, b2 - 1)
        fonk1(b3, b2 + 1, r)
def fonk2():
    b3 = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    print("Original array:", b3)
    fonk1(b3, 0, len(b3))
    print("Sorted array:", b3)
if b4 = = "__main__":
    fonk2()