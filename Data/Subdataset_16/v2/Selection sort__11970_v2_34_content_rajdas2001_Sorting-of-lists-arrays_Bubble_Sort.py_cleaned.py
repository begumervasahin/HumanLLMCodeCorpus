def fonk1(b2):
    b1 = len(b2)
    for i in range(b1):
        for j in range(0, b1 - i - 1):
            if b2[j] > b2[j + 1]:
                b2[j], b2[j + 1] = b2[j + 1], b2[j]
def fonk2():
    b2 = [110, 34, 25, 32, 28, 10, 90]
    print("Original array:", b2)
    fonk1(b2)
    print("Sorted array:", b2)
if b3 = = "__main__":
    fonk2()