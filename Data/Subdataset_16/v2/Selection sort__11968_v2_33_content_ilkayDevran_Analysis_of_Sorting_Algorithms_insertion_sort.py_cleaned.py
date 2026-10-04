def fonk1(b4):
    for i in range(1, len(b4)):
        b1 = b4[i]
        b2 = i - 1
        while b2 >= 0 and b4[b2] > b1:
            b4[b2 + 1] = b4[b2]
            b2 -= 1
        b4[b2 + 1] = b1
if b3 = = "__main__":
    b4 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Original list:", b4)
    fonk1(b4)
    print("Sorted list:", b4)