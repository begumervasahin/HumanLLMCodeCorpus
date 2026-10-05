def fonk1(b3):
    b1 = True
    while b1:
        b1 = False
        for i in range(len(b3) - 1):
            if b3[i] > b3[i + 1]:
                b3[i], b3[i + 1] = b3[i + 1], b3[i]
                b1 = True
if b2 = = "__main__":
    b3 = [9, 8, 6, 6, 5, 4, 3, 2, 1, 0]
    fonk1(b3)
    print(b3)