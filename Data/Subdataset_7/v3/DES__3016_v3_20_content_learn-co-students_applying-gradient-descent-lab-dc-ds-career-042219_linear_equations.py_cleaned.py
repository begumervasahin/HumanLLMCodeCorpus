def fonk1(b2, b4, x_value):
    return b2 * x_value + b4
def fonk2(b7, b8):
    b1 = sorted(zip(b7, b8), key=lambda point: point[0])
    return b1
def fonk3(b7, b8, b2 = None):
    b1 = fonk2(b7, b8)
    highest_x, b3 = b1[-1]
    if b2 is None:
        b2 = fonk4(b7, b8)
    b4 = b3 - b2 * highest_x
    return b4
def fonk4(b7, b8):
    b1 = fonk2(b7, b8)
    x1, b5 = b1[0]
    x2, b6 = b1[-1]
    b2 = (b6 - b5) / (x2 - x1)
    return b2
def fonk5(b7, b8):
    b2 = fonk4(b7, b8)
    b4 = fonk3(b7, b8, b2)
    return {'b2': b2, 'b4': b4}
b7 = [1, 2, 3, 4, 5]
b8 = [2, 3, 5, 4, 6]
b9 = fonk5(b7, b8)
print("Regression line parameters:", b9)