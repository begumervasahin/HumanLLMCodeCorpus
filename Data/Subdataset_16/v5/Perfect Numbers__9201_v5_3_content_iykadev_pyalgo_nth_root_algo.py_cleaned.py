from decimal import Decimal, getcontext
def fonk1(b2, b3, a3):
    getcontext().b1 = a3
    b2 = Decimal(b2)
    b3 = Decimal(b3)
    b4 = b3 / b2
    b5 = Decimal(1)
    while True:
        b5 = (1 / b2) * ((b2 - 1) * b4 + (b3 / (b4 ** (b2 - 1))))
        if b4 = = b5:
            return b5
        b4 = b5
def fonk2():
    a1 = 5
    a2 = 34
    a3 = 10
    b6 = fonk1(a1, a2, a3)
    print(f"The {a1}th b6 of {a2} with a3 {a3} is {b6}")
if b7 = = "__main__":
    fonk2()