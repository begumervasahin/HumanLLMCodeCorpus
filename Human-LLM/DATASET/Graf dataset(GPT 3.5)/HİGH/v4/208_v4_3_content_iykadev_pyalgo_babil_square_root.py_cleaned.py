def fonk1(number, epsilon):
    b1 = (1 + number) / 2
    b2 = (b1 + number / b1) * 0.5
    b3 = (b2 - b1) / b1
    if b3 < 0:
        b3 = -b3
    while b3 > epsilon:
        b1 = b2
        b2 = (b1 + number / b1) * 0.5
        b3 = (b2 - b1) / b1
        if b3 < 0:
            b3 = -b3
    b4 = "The square root of %s is approximately %s" % (number, b2)
    print(b4)
def fonk2():
    fonk1(5, 0.00001)
fonk2()