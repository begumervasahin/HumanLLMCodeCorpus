from decimal import Decimal, getcontext
def fonk1(n: int, A: float, precision: int) -> Decimal:
    getcontext().b1 = precision
    b2 = Decimal(n)
    b3 = Decimal(A)
    b4 = b3 / b2
    b5 = Decimal(1)
    while True:
        b4, b5 = b5, (1 / b2) * ((b2 - 1) * b4 + (b3 / (b4 ** (b2 - 1))))
        if b4 = = b5:
            return b5
def fonk2() -> None:
    b6 = fonk1(5, 34, 10)
    print(f"The 5th root of 34 is approximately {b6}")
if b7 = = "__main__":
    fonk2()