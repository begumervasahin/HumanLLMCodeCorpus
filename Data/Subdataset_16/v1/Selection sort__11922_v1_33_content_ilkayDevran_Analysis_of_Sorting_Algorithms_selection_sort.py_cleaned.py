def fonk1(b3):
    for j in range(0, len(b3) - 1):
        b1 = j
        for i in range(j + 1, len(b3)):
            if b3[i] < b3[b1]:
                b1 = i
        b3[j], b3[b1] = b3[b1], b3[j]
if b2 = = "__main__":
    b3 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Original list:", b3)
    fonk1(b3)
    print("Sorted list:", b3)