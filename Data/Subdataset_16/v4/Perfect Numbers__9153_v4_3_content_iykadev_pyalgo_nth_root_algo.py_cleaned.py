from decimal import Decimal, getcontext
def fonk1(b2, b3, precision):
    getcontext().b1 = precision
    b2 = Decimal(b2)
    b3 = Decimal(b3)
    b4 = b3 / b2
    b5 = Decimal(1)
    while True:
        b4, b5 = b5, (1 / b2) * ((b2 - 1) * b4 + (b3 / (b4 ** (b2 - 1))))
        if b4 = = b5:
            return b5
print(fonk1(5, 34, 10))