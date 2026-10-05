import sys
sys.setrecursionlimit(3000)
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))
def main():
    m = 3
    n = 4
    result = ackermann(m, n)
    print(f"Ackermann({m}, {n}) = {result}")
if __name__ == "__main__":
    main()