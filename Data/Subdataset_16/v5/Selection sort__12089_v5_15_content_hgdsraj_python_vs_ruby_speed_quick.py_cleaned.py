def fonk1(b2):
    b1 = len(b2)
    for i in range(b1 - 1):
        for j in range(i + 1, b1):
            if b2[j] < b2[i]:
                b2[i], b2[j] = b2[j], b2[i]
    return b2
def fonk2():
    b2 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    b3 = fonk1(b2)
    print("Sorted array:")
    print(b3)
if b4 = = "__main__":
    fonk2()