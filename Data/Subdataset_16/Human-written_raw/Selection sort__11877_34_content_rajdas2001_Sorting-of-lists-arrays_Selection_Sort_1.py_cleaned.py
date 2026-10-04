def fonk1(b3):
    a1 = 0
    while a1 < len(b3):
        b1 = min(b3[a1:])
        b2 = b3.index(b1)
        b3[a1], b3[b2] = b3[b2], b3[a1]
        a1 = a1 + 1
    for elements in b3:
        print(elements)
b3 = [49, 25, 26, 2, 99]
print("Sorted array is:")
fonk1(b3)