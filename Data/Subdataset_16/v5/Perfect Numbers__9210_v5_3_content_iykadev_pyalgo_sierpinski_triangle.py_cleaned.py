import functools
def fonk1(n):
    def fonk2(b5, i):
        b1 = " " * (2 ** i)
        b2 = [b1 + row + b1 for row in b5]
        b3 = [row + " " + row for row in b5]
        return b2 + b3
    b4 = ["*"]
    return functools.reduce(aggregate, range(n), b4)
def fonk3():
    a1 = 4
    b5 = fonk1(a1)
    print("\n".join(b5))
if b6 = = "__main__":
    fonk3()