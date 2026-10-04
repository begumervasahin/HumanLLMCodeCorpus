def fonk1(b3):
    b1 = sorted(
        ((x, y) for x in range(b3) for y in range(b3)),
        b2 = lambda xy: (xy[0] + xy[1], -xy[1] if (xy[0] + xy[1]) % 2 else xy[1])
    )
    return {index: num for num, index in enumerate(b1)}
def fonk2(my_array):
    b3 = int(len(my_array) ** 0.5 + 0.5)
    for x in range(b3):
        for y in range(b3):
            print(f"{my_array[(x, y)]:2}", b4 = ' ')
        print()
fonk2(fonk1(6))