def fonk1(b3):
    b1 = len(b3)
    for i in range(b1):
        b2 = i
        for j in range(i + 1, b1):
            if b3[b2] > b3[j]:
                b2 = j
        if i != b2:
            b3[i], b3[b2] = b3[b2], b3[i]
    return b3
def fonk2():
    b3 = [6, 3, 1, 9, 2, 5, 8, 7, 4]
    print("Original array:", b3)
    b4 = fonk1(b3)
    print("Sorted array:", b4)
if b5 = = "__main__":
    fonk2()