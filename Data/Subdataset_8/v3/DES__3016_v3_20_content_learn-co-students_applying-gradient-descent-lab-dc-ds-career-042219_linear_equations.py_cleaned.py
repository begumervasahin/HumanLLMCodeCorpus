def expected_value_for_line(slope, intercept, x_value):
    return slope * x_value + intercept
def sort_points(x_values, y_values):
    sorted_values = sorted(zip(x_values, y_values), key=lambda point: point[0])
    return sorted_values
def calculate_y_intercept(x_values, y_values, slope=None):
    sorted_values = sort_points(x_values, y_values)
    highest_x, highest_y = sorted_values[-1]
    if slope is None:
        slope = calculate_slope(x_values, y_values)
    intercept = highest_y - slope * highest_x
    return intercept
def calculate_slope(x_values, y_values):
    sorted_values = sort_points(x_values, y_values)
    x1, y1 = sorted_values[0]
    x2, y2 = sorted_values[-1]
    slope = (y2 - y1) / (x2 - x1)
    return slope
def build_regression_line(x_values, y_values):
    slope = calculate_slope(x_values, y_values)
    intercept = calculate_y_intercept(x_values, y_values, slope)
    return {'slope': slope, 'intercept': intercept}
x_values = [1, 2, 3, 4, 5]
y_values = [2, 3, 5, 4, 6]
regression_line = build_regression_line(x_values, y_values)
print("Regression line parameters:", regression_line)