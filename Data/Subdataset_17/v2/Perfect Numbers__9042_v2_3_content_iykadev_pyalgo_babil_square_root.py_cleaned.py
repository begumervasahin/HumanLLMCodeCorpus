def babylonian_square_root(a: float, eps: float) -> float:
    x0 = (1 + a) / 2
    x1 = (x0 + a / x0) * 0.5
    y = abs((x1 - x0) / x0)
    while y > eps:
        x0 = x1
        x1 = (x0 + a / x0) * 0.5
        y = abs((x1 - x0) / x0)
    return x1
def main() -> None:
    number = 5
    tolerance = 0.0001
    result = babylonian_square_root(number, tolerance)
    print(f"The square root of {number} is approximately {result:.6f}")
if __name__ == "__main__":
    main()