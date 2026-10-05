def fonk1(number, epsilon):
    b1 = (1 + number) / 2
    b2 = (b1 + number / b1) * 0.5
    b3 = abs((b2 - b1) / b1)
    while b3 > epsilon:
        b1 = b2
        b2 = (b1 + number / b1) * 0.5
        b3 = abs((b2 - b1) / b1)
    b4 = "The square root of {} is {}".format(number, b2)
    print(b4)
def fonk2():
    fonk1(5, 1e-7)
fonk2()