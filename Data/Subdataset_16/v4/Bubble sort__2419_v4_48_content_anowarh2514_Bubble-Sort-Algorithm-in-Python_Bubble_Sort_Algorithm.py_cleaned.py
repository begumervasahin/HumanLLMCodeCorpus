def fonk1(b3):
    b1 = len(b3)
    for i in range(b1-1, 0, -1):
        for j in range(i):
            if b3[j] > b3[j+1]:
                b3[j], b3[j+1] = b3[j+1], b3[j]
        print(b3)
if b2 = = "__main__":
    b3 = [5, 3, 8, 6, 7, 2]
    print("Unsorted b4 = ", b3)
    fonk1(b3)
    print("Sorted b4 = ", b3)