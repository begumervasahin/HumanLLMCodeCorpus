import functools
def fonk1(n):
    def fonk2(TRIANGLE, I):
        b1 = " " * (2 ** I)
        return [b1 + X + b1 for X in TRIANGLE] + [X + " " + X for X in TRIANGLE]
    return functools.reduce(aggregate, range(n), ["*"])
def fonk3():
    b2 = fonk1(4)
    print("\n".join(b2))
if b3 = = "__main__":
    fonk3()