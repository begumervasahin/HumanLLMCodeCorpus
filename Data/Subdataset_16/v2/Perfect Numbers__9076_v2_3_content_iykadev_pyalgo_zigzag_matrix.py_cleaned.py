def fonk1(b3):
    b1 = sorted(((x, y) for x in range(b3) for y in range(b3)),
                         b2 = lambda xy: (xy[0] + xy[1], -xy[1] if (xy[0] + xy[1]) % 2 else xy[1]))
    return {index: num for num, index in enumerate(b1)}
def fonk2(matrix):
    b3 = int(len(matrix) ** 0.5 + 0.5)
    for x in range(b3):
        for y in range(b3):
            print(f"{matrix[(x, y)]:2d}", b4 = " ")
        print()
b5 = fonk1(6)
fonk2(b5)