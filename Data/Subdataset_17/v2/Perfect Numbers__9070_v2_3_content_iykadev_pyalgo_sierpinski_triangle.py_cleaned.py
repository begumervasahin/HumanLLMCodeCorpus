import functools
def sierpinski(order: int) -> list:
    def aggregate(triangle: list, iteration: int) -> list:
        space = " " * (2 ** iteration)
        return [space + row + space for row in triangle] + [row + " " + row for row in triangle]
    return functools.reduce(aggregate, range(order), ["*"])
def main() -> None:
    order = 4
    triangle = sierpinski(order)
    print("\n".join(triangle))
if __name__ == "__main__":
    main()