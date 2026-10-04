def fonk1(b3):
    b1 = len(b3)
    for i in range(b1):
        b2 = False
        for j in range(0, b1 - i - 1):
            if b3[j] > b3[j + 1]:
                b3[j], b3[j + 1] = b3[j + 1], b3[j]
                b2 = True
        if not b2:
            break
def fonk2():
    b3 = [110, 34, 25, 32, 28, 10, 90]
    print("Original array:", b3)
    fonk1(b3)
    print("Sorted array:", b3)
if b4 = = "__main__":
    fonk2()