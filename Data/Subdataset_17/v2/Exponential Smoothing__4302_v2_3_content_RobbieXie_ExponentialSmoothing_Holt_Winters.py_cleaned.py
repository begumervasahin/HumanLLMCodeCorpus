import numpy as np
from matplotlib import pyplot as plt
def exponential_smoothing(alpha, s):
    smoothed = np.zeros(s.shape)
    smoothed[0] = s[0]
    for i in range(1, len(smoothed)):
        smoothed[i] = alpha * s[i] + (1 - alpha) * smoothed[i - 1]
    return smoothed
def show_data(years, original_data, double_smoothing, triple_smoothing):
    plt.figure(figsize=(14, 6), dpi=80)
    plt.plot(years, original_data, color='blue', label="Actual Value")
    plt.plot(years[1:], double_smoothing[2:], color='red', label="Double Predicted Value")
    plt.plot(years[1:], triple_smoothing[2:], color='green', label="Triple Predicted Value")
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
    year, time_id, number = data.T
    initial_data = np.insert(data, 0, values=[0, 0, number[0]], axis=0)
    initial_year, initial_time_id, initial_number = initial_data.T
    s_single = exponential_smoothing(alpha, initial_number)
    s_double = exponential_smoothing(alpha, s_single)
    a_double = 2 * s_single - s_double
    b_double = (alpha / (1 - alpha)) * (s_single - s_double)
    s_pre_double = np.zeros(s_double.shape)
    for i in range(1, len(initial_time_id)):
        s_pre_double[i] = a_double[i - 1] + b_double[i - 1]
    s_pre_double = np.append(s_pre_double, [
        a_double[-1] + b_double[-1] * 1,
        a_double[-1] + b_double[-1] * 2
    ])
    s_triple = exponential_smoothing(alpha, s_double)
    a_triple = 3 * s_single - 3 * s_double + s_triple
    b_triple = (alpha / (2 * (1 - alpha)**2)) * ((6 - 5 * alpha) * s_single -
              2 * ((5 - 4 * alpha) * s_double) + (4 - 3 * alpha) * s_triple)
    c_triple = ((alpha**2) / (2 * (1 - alpha)**2)) * (s_single - 2 * s_double + s_triple)
    s_pre_triple = np.zeros(s_triple.shape)
    for i in range(1, len(initial_time_id)):
        s_pre_triple[i] = a_triple[i - 1] + b_triple[i - 1] + c_triple[i - 1]
    s_pre_triple = np.append(s_pre_triple, [
        a_triple[-1] + b_triple[-1] * 1 + c_triple[-1] * 1,
        a_triple[-1] + b_triple[-1] * 2 + c_triple[-1] * 4
    ])
    new_years = np.append(year, future_years)
    output = np.array([new_years, s_pre_double, s_pre_triple])
    print(output)
    show_data(new_years, number, s_pre_double, s_pre_triple)
if __name__ == '__main__':
    main()