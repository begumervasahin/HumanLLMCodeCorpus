import functools
def fonk1(a1: int) -> list:
    def fonk2(b4: list, iteration: int) -> list:
        b1 = " " * (2 ** iteration)
        b2 = [b1 + row + b1 for row in b4]
        b3 = [row + " " + row for row in b4]
        return b2 + b3
    return functools.reduce(aggregate, range(a1), ["*"])
def fonk3() -> None:
    a1 = 4
    b4 = fonk1(a1)
    print("\n".join(b4))
if b5 = = "__main__":
    fonk3()