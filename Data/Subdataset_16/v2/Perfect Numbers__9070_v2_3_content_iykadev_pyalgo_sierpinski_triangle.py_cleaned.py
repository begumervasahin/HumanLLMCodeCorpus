import functools
def fonk1(a1: int) -> list:
    def fonk2(b2: list, iteration: int) -> list:
        b1 = " " * (2 ** iteration)
        return [b1 + row + b1 for row in b2] + [row + " " + row for row in b2]
    return functools.reduce(aggregate, range(a1), ["*"])
def fonk3() -> None:
    a1 = 4
    b2 = fonk1(a1)
    print("\n".join(b2))
if b3 = = "__main__":
    fonk3()