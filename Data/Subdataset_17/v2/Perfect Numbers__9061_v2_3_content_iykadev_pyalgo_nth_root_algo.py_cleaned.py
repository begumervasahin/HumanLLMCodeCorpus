from decimal import Decimal, getcontext
def nth_root(n: int, A: float, precision: int) -> Decimal:
    getcontext().prec = precision
    n_decimal = Decimal(n)
    A_decimal = Decimal(A)
    x_0 = A_decimal / n_decimal
    x_1 = Decimal(1)
    while True:
        x_0, x_1 = x_1, (1 / n_decimal) * ((n_decimal - 1) * x_0 + (A_decimal / (x_0 ** (n_decimal - 1))))
        if x_0 == x_1:
            return x_1
def main() -> None:
    result = nth_root(5, 34, 10)
    print(f"The 5th root of 34 is approximately {result}")
if __name__ == "__main__":
    main()