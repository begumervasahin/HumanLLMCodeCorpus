def fonk1(b3, intercept, x_value):
    return b3 * x_value + intercept
def fonk2(x_values, y_values):
    b1 = list(zip(x_values, y_values))
    b2 = sorted(b1, key=lambda point: point[0])
    return b2
def fonk3(x_values, y_values, b3 = None):
    b4 = fonk2(x_values, y_values)
    highest_x, b5 = b4[-1]
    if b3 is None:
        b3 = calculate_slope(x_values, y_values)
    b6 = b5 - b3 * highest_x
    return b6
def fonk4(x_values, y_values):
    b4 = fonk2(x_values, y_values)
    x1, b7 = b4[0]
    x2, b8 = b4[-1]
    b3 = (b8 - b7) / (x2 - x1)
    return b3
def fonk5(x_values, y_values):
    b4 = fonk2(x_values, y_values)
    highest_x, b5 = b4[-1]
    lowest_x, b9 = b4[0]
    b10 = fonk4(x_values, y_values)
    b11 = fonk3(x_values, y_values, b10)
    return {'b3': b10, 'intercept': b11}