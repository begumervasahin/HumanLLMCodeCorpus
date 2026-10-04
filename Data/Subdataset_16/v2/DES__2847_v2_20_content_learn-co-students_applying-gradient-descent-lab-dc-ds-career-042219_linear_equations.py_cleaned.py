def fonk1(b3, b6, a1):
    return b3 * a1 + b6
def fonk2(x_values, y_values):
    b1 = list(zip(x_values, y_values))
    b2 = sorted(b1, key=lambda point: point[0])
    return b2
def fonk3(x_values, y_values, b3 = None):
    b4 = fonk2(x_values, y_values)
    b5 = b4[-1]
    if b3 is None:
        b3 = fonk4(x_values, y_values)
    b6 = b5[1] - b3 * b5[0]
    return b6
def fonk4(x_values, y_values):
    b4 = fonk2(x_values, y_values)
    x1, b7 = b4[0]
    x2, b8 = b4[-1]
    b3 = (b8 - b7) / (x2 - x1)
    return b3
def fonk5(x_values, y_values):
    b3 = fonk4(x_values, y_values)
    b6 = fonk3(x_values, y_values, b3)
    return {'b3': b3, 'b6': b6}
if b9 = = "__main__":
    b10 = [1, 2, 3, 4, 5]
    b11 = [2, 4, 5, 4, 5]
    b12 = fonk5(b10, b11)
    print(f"Slope (b3): {b12['b3']}")
    print(f"Y-intercept (b6): {b12['b6']}")
    a1 = 6
    b13 = fonk1(b12['b3'], b12['b6'], a1)
    print(f"Expected y-value for b14 = {a1}: {b13}")