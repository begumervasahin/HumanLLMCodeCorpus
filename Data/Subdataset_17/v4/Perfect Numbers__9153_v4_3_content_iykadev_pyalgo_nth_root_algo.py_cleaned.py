from decimal import Decimal, getcontext
def nth_root(n, A, precision):
    getcontext().prec = precision
    n = Decimal(n)
    A = Decimal(A)
    x_0 = A / n
    x_1 = Decimal(1)
    while True:
        x_0, x_1 = x_1, (1 / n) * ((n - 1) * x_0 + (A / (x_0 ** (n - 1))))
        if x_0 == x_1:
            return x_1
print(nth_root(5, 34, 10))