def fonk1(b3):
    b1 = len(b3)
    for i in range(b1):
        b2 = i
        for j in range(i + 1, b1):
            if b3[j] < b3[b2]:
                b2 = j
        b3[i], b3[b2] = b3[b2], b3[i]
    return b3
def fonk2():
    b3 = [5, 3, 2, 10, 45, 3, 1]
    b4 = fonk1(b3)
    print("Sorted array:", b4)
if b5 = = "__main__":
    fonk2()