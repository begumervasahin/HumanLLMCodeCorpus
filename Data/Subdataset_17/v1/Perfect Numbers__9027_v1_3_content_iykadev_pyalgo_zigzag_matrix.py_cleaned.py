def zigzag(n):
    indexorder = sorted(((x, y) for x in range(n) for y in range(n)),
                        key=lambda xy: (xy[0] + xy[1], -xy[1] if (xy[0] + xy[1]) % 2 else xy[1]))
    return {index: num for num, index in enumerate(indexorder)}
def printzz(myarray):
    n = int(len(myarray) ** 0.5 + 0.5)
    for x in range(n):
        for y in range(n):
            print("%2i" % myarray[(x, y)], end=" ")
        print()
printzz(zigzag(6))