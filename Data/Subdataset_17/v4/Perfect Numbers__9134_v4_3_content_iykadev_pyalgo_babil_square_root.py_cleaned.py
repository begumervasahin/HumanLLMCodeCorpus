def babylonian_square_root(a, eps):
    x0 = (1 + a) / 2
    x1 = (x0 + a / x0) * 0.5
    y = abs((x1 - x0) / x0)
    while y > eps:
        x0 = x1
        x1 = (x0 + a / x0) * 0.5
        y = abs((x1 - x0) / x0)
    result = f"The square root of the number {a} is approximately {x1}"
    print(result)
def main():
    babylonian_square_root(5, 0.0001)
main()