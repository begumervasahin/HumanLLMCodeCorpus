def fonk1(b3, b5, a1):
    return b3 * a1 + b5
def fonk2(x_values, y_values):
    b1 = list(zip(x_values, y_values))
    b2 = sorted(b1, key=lambda value: value[0])
    return b2
def fonk3(x_values, y_values, b3 = None):
    b2 = fonk2(x_values, y_values)
    b4 = b2[-1]
    if b3 is None:
        b3 = fonk4(x_values, y_values)
    b5 = b4[1] - b3 * b4[0]
    return b5
def fonk4(x_values, y_values):
    b2 = fonk2(x_values, y_values)
    x1, b6 = b2[0]
    x2, b7 = b2[-1]
    b3 = (b7 - b6) / (x2 - x1)
    return b3
def fonk5(x_values, y_values):
    b3 = fonk4(x_values, y_values)
    b5 = fonk3(x_values, y_values, b3)
    return {'b3': b3, 'b5': b5}
if b8 = = "__main__":
    b9 = [1, 2, 3, 4, 5]
    b10 = [2, 4, 5, 4, 5]
    b11 = fonk5(b9, b10)
    print(f"Slope (b3): {b11['b3']}")
    print(f"Y-intercept (b5): {b11['b5']}")
    a1 = 6
    b12 = fonk1(b11['b3'], b11['b5'], a1)
    print(f"Expected y-value for b13 = {a1}: {b12}")