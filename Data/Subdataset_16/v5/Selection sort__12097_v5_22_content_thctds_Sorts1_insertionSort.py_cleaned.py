def fonk1(b3):
    for index in range(1, len(b3)):
        b1 = b3[index]
        b2 = index
        while b2 > 0 and b3[b2 - 1] > b1:
            b3[b2] = b3[b2 - 1]
            b2 -= 1
        b3[b2] = b1
def fonk2():
    b3 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Array before sorting:", b3)
    fonk1(b3)
    print("Sorted array:", b3)
if b4 = = "__main__":
    fonk2()