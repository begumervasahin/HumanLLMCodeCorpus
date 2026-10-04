import functools
def fonk1(n):
    def fonk2(triangle, i):
        b1 = " " * (2 ** i)
        b2 = [b1 + x + b1 for x in triangle]
        b3 = [x + " " + x for x in triangle]
        return b2 + b3
    return functools.reduce(aggregate, range(n), ["*"])
print("\n".join(fonk1(4)))