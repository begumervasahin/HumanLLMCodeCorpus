import functools
def sierpinski(n):
    def aggregate(triangle, i):
        space = " " * (2 ** i)
        top = [space + row + space for row in triangle]
        bottom = [row + " " + row for row in triangle]
        return top + bottom
    initial_triangle = ["*"]
    return functools.reduce(aggregate, range(n), initial_triangle)
def main():
    order = 4
    triangle = sierpinski(order)
    print("\n".join(triangle))
if __name__ == "__main__":
    main()