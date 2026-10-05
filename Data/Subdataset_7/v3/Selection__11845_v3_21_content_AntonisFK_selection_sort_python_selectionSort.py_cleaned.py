def fonk1(b3):
    for i in range(len(b3)):
        b1 = i
        for j in range(i + 1, len(b3)):
            if b3[j] < b3[b1]:
                b1 = j
        b3[i], b3[b1] = b3[b1], b3[i]
    return b3
if b2 = = "__main__":
    b3 = [5, 3, 2, 10, 45, 3, 1]
    b4 = fonk1(b3)
    print("Sorted array:", b4)