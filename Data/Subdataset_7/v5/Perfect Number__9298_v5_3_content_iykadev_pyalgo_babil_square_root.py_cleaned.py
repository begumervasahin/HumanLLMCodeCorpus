def fonk1(number, epsilon):
    b1 = (1 + number) / 2
    b2 = (b1 + number / b1) * 0.5
    while abs(b2 - b1) / b1 > epsilon:
        b1 = b2
        b2 = (b1 + number / b1) * 0.5
    b3 = "The square root of {} is approximately {:.5f}".format(number, b2)
    print(b3)
def fonk2():
    fonk1(5, 0.00001)
fonk2()