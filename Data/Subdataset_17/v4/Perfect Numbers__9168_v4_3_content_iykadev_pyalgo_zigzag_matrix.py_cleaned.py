def zigzag(n):
    index_order = sorted(
        ((x, y) for x in range(n) for y in range(n)),
        key=lambda xy: (xy[0] + xy[1], -xy[1] if (xy[0] + xy[1]) % 2 else xy[1])
    )
    return {index: num for num, index in enumerate(index_order)}
def print_zz(my_array):
    n = int(len(my_array) ** 0.5 + 0.5)
    for x in range(n):
        for y in range(n):
            print(f"{my_array[(x, y)]:2}", end=' ')
        print()
print_zz(zigzag(6))