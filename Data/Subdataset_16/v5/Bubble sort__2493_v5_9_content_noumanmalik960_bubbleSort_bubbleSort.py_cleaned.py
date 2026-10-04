def fonk1(b2):
    b1 = True
    while b1:
        b1 = False
        for i in range(len(b2) - 1):
            if b2[i] > b2[i + 1]:
                b2[i], b2[i + 1] = b2[i + 1], b2[i]
                b1 = True
def fonk2():
    b2 = [9, 8, 6, 6, 5, 4, 3, 2, 1, 0]
    print("Original array:", b2)
    fonk1(b2)
    print("Sorted array:", b2)
if b3 = = "__main__":
    fonk2()