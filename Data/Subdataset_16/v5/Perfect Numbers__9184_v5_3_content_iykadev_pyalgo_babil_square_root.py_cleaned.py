def fonk1(a, eps):
    b1 = (1 + a) / 2
    b2 = (b1 + a / b1) * 0.5
    b3 = abs((b2 - b1) / b1)
    while b3 > eps:
        b1 = b2
        b2 = (b1 + a / b1) * 0.5
        b3 = abs((b2 - b1) / b1)
    return b2
def fonk2():
    a1 = 5
    a2 = 0.0001
    b4 = fonk1(a1, a2)
    print(f"The square root of the a1 {a1} is approximately {b4}")
if b5 = = "__main__":
    fonk2()