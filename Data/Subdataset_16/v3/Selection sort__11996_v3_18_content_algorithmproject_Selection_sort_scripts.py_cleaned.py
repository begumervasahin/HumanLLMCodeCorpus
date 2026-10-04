def fonk1(b4):
    b1 = len(b4)
    for i in range(b1):
        b2 = i
        for j in range(i + 1, b1):
            if b4[b2] > b4[j]:
                b2 = j
        if i != b2:
            b4[i], b4[b2] = b4[b2], b4[i]
    return b4
def fonk2(b4):
    print(b4)
if b3 = = "__main__":
    b4 = [6, 3, 1, 9, 2, 5, 8, 7, 4]
    print("Original array:")
    fonk2(b4)
    b5 = fonk1(b4)
    print("Sorted array:")
    fonk2(b5)