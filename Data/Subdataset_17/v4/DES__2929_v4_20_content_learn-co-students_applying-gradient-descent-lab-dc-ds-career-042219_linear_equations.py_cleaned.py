def expected_value_for_line(m, b, x_value):
    return m * x_value + b
def sorted_points(x_values, y_values):
    points = list(zip(x_values, y_values))
    return sorted(points, key=lambda point: point[0])
def y_intercept(x_values, y_values, m=None):
    sorted_values = sorted_points(x_values, y_values)
    highest = sorted_values[-1]
    if m is None:
        m = slope(x_values, y_values)
    return highest[1] - m * highest[0]
def slope(x_values, y_values):
    sorted_values = sorted_points(x_values, y_values)
    x1, y1 = sorted_values[0]
    x2, y2 = sorted_values[-1]
    return (y2 - y1) / (x2 - x1)
def build_regression_line(x_values, y_values):
    m = slope(x_values, y_values)
    b = y_intercept(x_values, y_values, m)
    return {'m': m, 'b': b}
if __name__ == "__main__":
    x_vals = [1, 2, 3, 4, 5]
    y_vals = [2, 4, 5, 4, 5]
    regression_line = build_regression_line(x_vals, y_vals)
    print(f"Slope (m): {regression_line['m']}")
    print(f"Y-intercept (b): {regression_line['b']}")
    x_value = 6
    expected_y = expected_value_for_line(regression_line['m'], regression_line['b'], x_value)
    print(f"Expected y-value for x={x_value}: {expected_y}")