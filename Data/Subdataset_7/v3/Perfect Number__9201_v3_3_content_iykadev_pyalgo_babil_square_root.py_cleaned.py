def fonk1(a1, epsilon):
    b1 = (1 + a1) / 2
    b2 = (b1 + a1 / b1) * 0.5
    b3 = abs((b2 - b1) / b1)
    while b3 > epsilon:
        b1 = b2
        b2 = (b1 + a1 / b1) * 0.5
        b3 = abs((b2 - b1) / b1)
    return b2
def fonk2():
    a1 = 5
    a2 = 1e-7
    b4 = fonk1(a1, a2)
    b5 = "The square root of {} is {:.10f}".format(a1, b4)
    print(b5)
if b6 = = "__main__":
    fonk2()