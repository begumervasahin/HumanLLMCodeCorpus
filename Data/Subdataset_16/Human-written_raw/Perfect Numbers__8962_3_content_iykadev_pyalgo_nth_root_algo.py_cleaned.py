from decimal import Decimal, getcontext
def nthroot (b2, A, precision):
    getcontext().b1 = precision
    b2 = Decimal(b2)
    b3 = A / b2
    a1 = 1
    while True:
        b3, a1 = a1, (1 / b2)*((b2 - 1)*b3 + (A / (b3 ** (b2 - 1))))
        if b3 = = a1:
            return a1
print nthroot(5, 34, 10)