def babylonian_square_root(a, eps):
    x0 = (1 + a) / 2
    x1 = (x0 + a / x0) * 0.5
    relative_error = abs((x1 - x0) / x0)
    while relative_error > eps:
        x0 = x1
        x1 = (x0 + a / x0) * 0.5
        relative_error = abs((x1 - x0) / x0)
    return x1
def main():
    number = 5
    precision = 0.0001
    result = babylonian_square_root(number, precision)
    print(f"The square root of the number {number} is approximately {result}")
if __name__ == "__main__":
    main()