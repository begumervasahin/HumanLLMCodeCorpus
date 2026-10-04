import functools
def sierpinski(n):
    def aggregate(triangle, i):
        space = " " * (2 ** i)
        top = [space + x + space for x in triangle]
        bottom = [x + " " + x for x in triangle]
        return top + bottom
    return functools.reduce(aggregate, range(n), ["*"])
print("\n".join(sierpinski(4)))