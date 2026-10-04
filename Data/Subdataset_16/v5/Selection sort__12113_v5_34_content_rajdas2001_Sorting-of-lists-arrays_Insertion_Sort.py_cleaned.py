def fonk1(b4):
    for i in range(1, len(b4)):
        b1 = b4[i]
        b2 = i - 1
        while b2 >= 0 and b4[b2] > b1:
            b4[b2 + 1] = b4[b2]
            b2 -= 1
        b4[b2 + 1] = b1
if b3 = = "__main__":
    b4 = [32, 13, 14, 15, 98]
    print("Original array:", b4)
    fonk1(b4)
    print("Sorted array is:", b4)