import functools
def sierpinski(n):
    def aggregate(TRIANGLE, I):
        SPACE = " " * (2 ** I)
        return [SPACE + X + SPACE for X in TRIANGLE] + [X + " " + X for X in TRIANGLE]
    return functools.reduce(aggregate, range(n), ["*"])
def main():
    triangle = sierpinski(4)
    print("\n".join(triangle))
if __name__ == "__main__":
    main()