def fonk1(b4):
    b1 = sorted(((x, y) for x in range(b4) for y in range(b4)),
                         b2 = lambda xy: (xy[0] + xy[1], -xy[1] if (xy[0] + xy[1]) % 2 else xy[1]))
    b3 = {index: num for num, index in enumerate(b1)}
    return b3
def fonk2(matrix):
    b4 = int(len(matrix) ** 0.5 + 0.5)
    for x in range(b4):
        for y in range(b4):
            print(f"{matrix[(x, y)]:2d}", b5 = " ")
        print()
b3 = fonk1(6)
fonk2(b3)