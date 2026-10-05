import numpy as np
import matplotlib.pyplot as plt
def exponential_smoothing(alpha, series):
    smoothed_series = np.zeros(series.shape)
    smoothed_series[0] = series[0]
    for i in range(1, len(series)):
        smoothed_series[i] = alpha * series[i] + (1 - alpha) * smoothed_series[i - 1]
    return smoothed_series
def plot_project_data(year, actual_data, double_pred, triple_pred):
    plt.figure(figsize=(14, 6), dpi=80)
    plt.plot(year, actual_data, color='blue', label="Actual Value")
    plt.plot(year[2:], double_pred[2:], color='red', label="Double Predicted Value")
    plt.plot(year[2:], triple_pred[2:], color='green', label="Triple Predicted Value")
    plt.legend(loc='lower right')
    plt.title('Projects')
    plt.xlabel('Year')
    plt.ylabel('Number')
    plt.xticks(year)
    plt.show()
def main():
    alpha = 0.70
    prediction_years = np.array([2016, 2017])
    data_path = 'data1.txt'
    data = np.loadtxt(data_path)
    year, time_id, number = data.T
    initial_data = np.insert(data, 0, values=[0, 0, number[0]], axis=0)
    initial_year, initial_time_id, initial_number = initial_data.T
    s_single = exponential_smoothing(alpha, initial_number)
    s_double = exponential_smoothing(alpha, s_single)
    s_triple = exponential_smoothing(alpha, s_double)
    a_double = 2 * s_single - s_double
    b_double = (alpha / (1 - alpha)) * (s_single - s_double)
    double_pred = a_double + b_double
    a_triple = 3 * s_single - 3 * s_double + s_triple
    b_triple = (alpha / (2 * ((1 - alpha) ** 2))) * (
                (6 - 5 * alpha) * s_single - 2 * ((5 - 4 * alpha) * s_double) + (4 - 3 * alpha) * s_triple)
    c_triple = ((alpha ** 2) / (2 * ((1 - alpha) ** 2))) * (s_single - 2 * s_double + s_triple)
    triple_pred = a_triple + b_triple + c_triple
    year_with_pred = np.insert(year, len(year), values=prediction_years, axis=0)
    double_pred = np.insert(double_pred, len(double_pred), values=np.array(
        [a_double[-1] + b_double[-1] * i for i in range(1, 3)]), axis=0)
    triple_pred = np.insert(triple_pred, len(triple_pred), values=np.array(
        [a_triple[-1] + b_triple[-1] * i + c_triple[-1] * (i ** 2) for i in range(1, 3)]), axis=0)
    plot_project_data(year_with_pred, initial_number, double_pred, triple_pred)
if __name__ == '__main__':
    main()