def fonk1(b3):
    b1 = len(b3)
    for i in range(b1):
        b2 = i
        for j in range(i + 1, b1):
            if b3[j] < b3[b2]:
                b2 = j
        b3[i], b3[b2] = b3[b2], b3[i]
def fonk2():
    b3 = [49, 25, 26, 2, 99]
    print("Original array:", b3)
    fonk1(b3)
    print("Sorted array:", b3)
if b4 = = "__main__":
    fonk2()