def fonk1(b2):
    b1 = len(b2)
    for last_pos in range(b1 - 1, 0, -1):
        a1 = 0
        for pos in range(1, last_pos + 1):
            if b2[pos] > b2[a1]:
                a1 = pos
        b2[last_pos], b2[a1] = b2[a1], b2[last_pos]
def fonk2():
    b2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Array before sorting:", b2)
    fonk1(b2)
    print("Sorted array:", b2)
if b3 = = "__main__":
    fonk2()