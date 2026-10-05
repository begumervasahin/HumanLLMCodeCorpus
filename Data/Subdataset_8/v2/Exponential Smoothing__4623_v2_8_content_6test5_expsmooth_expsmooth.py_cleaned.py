import numpy as np
def expsmooth(data):
    optimal_alpha = calculate_optimal_alpha(data)
    smoothed_data = apply_smoothing(data, optimal_alpha)
    return smoothed_data
def calculate_optimal_alpha(data):
    alpha_range = np.arange(0.1, 2, 0.1)
    sss = []
    for alpha in alpha_range:
        squared_errors = calculate_squared_errors(data, alpha)
        mean_squared_error = np.mean(squared_errors)
        sss.append(mean_squared_error)
    min_index = np.argmin(sss)
    optimal_alpha = alpha_range[min_index]
    print("Optimal Alpha:", optimal_alpha)
    return optimal_alpha
def calculate_squared_errors(data, alpha):
    squared_errors = []
    for i, value in enumerate(data):
        b = calculate_initial_value(data, alpha, i)
        squared_error = 0
        for j in range(i, len(data)):
            squared_error += (b - data[j]) ** 2
            b = alpha * data[j] + (1 - alpha) * b
        squared_errors.append(squared_error)
    return squared_errors
def calculate_initial_value(data, alpha, index):
    initial_value = alpha * data[index] + (1 - alpha) * data[index]
    return initial_value
def apply_smoothing(data, alpha):
    smoothed_data = []
    for i, value in enumerate(data):
        if i == 0:
            smoothed_value = value
        else:
            smoothed_value = alpha * value + (1 - alpha) * smoothed_data[-1]
        smoothed_data.append(smoothed_value)
    return smoothed_data[-1]
if __name__ == '__main__':
    data = np.array([1, 2, 3, 4, 5])
    result = expsmooth(data)
    print("Result:", result)