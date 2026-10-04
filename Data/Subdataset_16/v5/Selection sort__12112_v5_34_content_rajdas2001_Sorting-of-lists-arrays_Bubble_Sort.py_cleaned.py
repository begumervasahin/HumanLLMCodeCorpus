def fonk1(b4):
    b1 = len(b4)
    for i in range(b1):
        b2 = False
        for j in range(0, b1 - i - 1):
            if b4[j] > b4[j + 1]:
                b4[j], b4[j + 1] = b4[j + 1], b4[j]
                b2 = True
        if not b2:
            break
if b3 = = "__main__":
    b4 = [110, 34, 25, 32, 28, 10, 90]
    print("Original array:", b4)
    fonk1(b4)
    print("Sorted array:", b4)