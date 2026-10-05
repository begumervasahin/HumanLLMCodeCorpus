def fonk1(b3, b11, x_value):
    return b3 * x_value + b11
def fonk2(b12, b13):
    b1 = list(zip(b12, b13))
    b2 = sorted(b1, key=lambda value: value[0])
    return b2
def fonk3(b12, b13, b3 = None):
    b2 = fonk2(b12, b13)
    b4 = b2[-1]
    if b3 is None:
        b3 = fonk4(b12, b13)
    b5 = b4[1] - b3 * b4[0]
    return b5
def fonk4(b12, b13):
    b2 = fonk2(b12, b13)
    b6 = b2[0][0]
    b7 = b2[0][1]
    b8 = b2[-1][0]
    b9 = b2[-1][1]
    b3 = (b9 - b7) / (b8 - b6)
    return b3
def fonk5(b12, b13):
    b2 = fonk2(b12, b13)
    b4 = b2[-1]
    b10 = b2[0]
    b3 = fonk4(b12, b13)
    b11 = fonk3(b12, b13, b3)
    return {'b3': b3, 'b11': b11}
b12 = [1, 2, 3, 4, 5]
b13 = [2, 3, 5, 4, 6]
b14 = fonk5(b12, b13)
print("Regression line parameters:", b14)