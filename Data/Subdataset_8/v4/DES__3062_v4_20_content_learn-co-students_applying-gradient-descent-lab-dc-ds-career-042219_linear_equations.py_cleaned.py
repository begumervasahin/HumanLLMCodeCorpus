def expected_value_for_line(slope, intercept, x_value):
    return slope * x_value + intercept
def sorted_points(x_values, y_values):
    points = list(zip(x_values, y_values))
    sorted_points = sorted(points, key=lambda point: point[0])
    return sorted_points
def y_intercept(x_values, y_values, slope=None):
    sorted_values = sorted_points(x_values, y_values)
    highest_x, highest_y = sorted_values[-1]
    if slope is None:
        slope = calculate_slope(x_values, y_values)
    offset = highest_y - slope * highest_x
    return offset
def slope(x_values, y_values):
    sorted_values = sorted_points(x_values, y_values)
    x1, y1 = sorted_values[0]
    x2, y2 = sorted_values[-1]
    slope = (y2 - y1) / (x2 - x1)
    return slope
def build_regression_line(x_values, y_values):
    sorted_values = sorted_points(x_values, y_values)
    highest_x, highest_y = sorted_values[-1]
    lowest_x, lowest_y = sorted_values[0]
    slope_value = slope(x_values, y_values)
    intercept_value = y_intercept(x_values, y_values, slope_value)
    return {'slope': slope_value, 'intercept': intercept_value}