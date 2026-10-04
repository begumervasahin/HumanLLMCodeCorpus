import numpy as np
from matplotlib import pyplot as plt
def exponential_smoothing(alpha, data):
    smoothed_data = np.zeros(data.shape)
    smoothed_data[0] = data[0]
    for i in range(1, len(smoothed_data)):
        smoothed_data[i] = alpha * data[i] + (1 - alpha) * smoothed_data[i - 1]
    return smoothed_data
def show_data(years, original_data, double_smoothed, triple_smoothed):
    plt.figure(figsize=(14, 6), dpi=80)
    plt.plot(years, original_data, color='blue', label="Actual Value")
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
    future_years = np.array([2016, 2017])
    data_path = 'data1.txt'
    data = np.loadtxt(data_path)
    years, time_id, values = data.T
    initial_data = np.insert(data, 0, values=[0, 0, values[0]], axis=0)
    initial_years, initial_time_id, initial_values = initial_data.T
    single_smoothed = exponential_smoothing(alpha, initial_values)
    double_smoothed = exponential_smoothing(alpha, single_smoothed)
    a_double = 2 * single_smoothed - double_smoothed
    b_double = (alpha / (1 - alpha)) * (single_smoothed - double_smoothed)
    double_predictions = np.zeros(double_smoothed.shape)
    for i in range(1, len(initial_time_id)):
        double_predictions[i] = a_double[i - 1] + b_double[i - 1]
    double_predictions = np.append(double_predictions, [
        a_double[-1] + b_double[-1] * 1,
        a_double[-1] + b_double[-1] * 2
    ])
    triple_smoothed = exponential_smoothing(alpha, double_smoothed)
    a_triple = 3 * single_smoothed - 3 * double_smoothed + triple_smoothed
    b_triple = (alpha / (2 * (1 - alpha)**2)) * ((6 - 5 * alpha) * single_smoothed -
              2 * ((5 - 4 * alpha) * double_smoothed) + (4 - 3 * alpha) * triple_smoothed)
    c_triple = ((alpha**2) / (2 * (1 - alpha)**2)) * (single_smoothed - 2 * double_smoothed + triple_smoothed)
    triple_predictions = np.zeros(triple_smoothed.shape)
    for i in range(1, len(initial_time_id)):
        triple_predictions[i] = a_triple[i - 1] + b_triple[i - 1] + c_triple[i - 1]
    triple_predictions = np.append(triple_predictions, [
        a_triple[-1] + b_triple[-1] * 1 + c_triple[-1] * 1,
        a_triple[-1] + b_triple[-1] * 2 + c_triple[-1] * 4
    ])
    all_years = np.append(years, future_years)
    output = np.array([all_years, double_predictions, triple_predictions])
    print(output)
    show_data(all_years, values, double_predictions, triple_predictions)
if __name__ == '__main__':
    main()