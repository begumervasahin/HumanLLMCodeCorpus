import numpy as np
import matplotlib.pyplot as plt
def exponential_smoothing(alpha, data):
    smoothed_data = np.zeros(data.shape)
    smoothed_data[0] = data[0]
    for i in range(1, len(data)):
        smoothed_data[i] = alpha * data[i] + (1 - alpha) * smoothed_data[i - 1]
    return smoothed_data
def plot_data(years, actual_data, double_smoothed, triple_smoothed):
    plt.figure(figsize=(14, 6), dpi=80)
    plt.plot(years, actual_data, color='blue', label="Actual Value")
    plt.plot(years[1:], double_smoothed[2:], color='red', label="Double Predicted Value")
    plt.plot(years[1:], triple_smoothed[2:], color='green', label="Triple Predicted Value")
    plt.legend(loc='lower right')
    plt.title('Projects')
    plt.xlabel('Year')
    plt.ylabel('Number')
    plt.xticks(years)
    plt.show()
def main():
    alpha = 0.70
    pre_years = np.array([2016, 2017])
    data_path = 'data1.txt'
    data = np.loadtxt(data_path)
    years, time_ids, actual_data = data.T
    initial_line = np.array([0, 0, actual_data[0]])
    initial_data = np.insert(data, 0, values=initial_line, axis=0)
    initial_years, initial_time_ids, initial_data = initial_data.T
    single_smoothed = exponential_smoothing(alpha, initial_data)
    double_smoothed = exponential_smoothing(alpha, single_smoothed)
    triple_smoothed = exponential_smoothing(alpha, double_smoothed)
    a_double = 2 * single_smoothed - double_smoothed
    b_double = (alpha / (1 - alpha)) * (single_smoothed - double_smoothed)
    double_predicted = np.zeros(double_smoothed.shape)
    for i in range(1, len(initial_time_ids)):
        double_predicted[i] = a_double[i - 1] + b_double[i - 1]
    double_predicted[-2:] = a_double[-1] + b_double[-1] * np.array([1, 2])
    a_triple = 3 * single_smoothed - 3 * double_smoothed + triple_smoothed
    b_triple = (alpha / (2 * ((1 - alpha) ** 2))) * ((6 - 5 * alpha) * single_smoothed - 2 * ((5 - 4 * alpha) * double_smoothed) + (4 - 3 * alpha) * triple_smoothed)
    c_triple = ((alpha ** 2) / (2 * ((1 - alpha) ** 2))) * (single_smoothed - 2 * double_smoothed + triple_smoothed)
    triple_predicted = np.zeros(triple_smoothed.shape)
    for i in range(1, len(initial_time_ids)):
        triple_predicted[i] = a_triple[i - 1] + b_triple[i - 1] * 1 + c_triple[i - 1] * (1 ** 2)
    triple_predicted[-2:] = a_triple[-1] + b_triple[-1] * np.array([1, 2]) + c_triple[-1] * np.array([1 ** 2, 2 ** 2])
    new_years = np.insert(years, len(years), values=pre_years, axis=0)
    output = np.array([new_years, double_predicted, triple_predicted])
    print(output)
    plot_data(new_years, actual_data, double_predicted, triple_predicted)
if __name__ == '__main__':
    main()