def zigzag(n):
    index_order = sorted(((x, y) for x in range(n) for y in range(n)),
                         key=lambda xy: (xy[0] + xy[1], -xy[1] if (xy[0] + xy[1]) % 2 else xy[1]))
    return {index: num for num, index in enumerate(index_order)}
def print_zigzag(matrix):
    n = int(len(matrix) ** 0.5 + 0.5)
    for x in range(n):
        for y in range(n):
            print(f"{matrix[(x, y)]:2d}", end=" ")
        print()
zigzag_matrix = zigzag(6)
print_zigzag(zigzag_matrix)