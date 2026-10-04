def zigzag(n):
    index_order = sorted(
        ((x, y) for x in range(n) for y in range(n)),
        key=lambda xy: (xy[0] + xy[1], -xy[1] if (xy[0] + xy[1]) % 2 else xy[1])
    )
    return {index: num for num, index in enumerate(index_order)}
def print_zz(zigzag_dict):
    n = int(len(zigzag_dict) ** 0.5 + 0.5)
    for x in range(n):
        for y in range(n):
            print(f"{zigzag_dict[(x, y)]:2}", end=' ')
        print()
if __name__ == "__main__":
    print_zz(zigzag(6))