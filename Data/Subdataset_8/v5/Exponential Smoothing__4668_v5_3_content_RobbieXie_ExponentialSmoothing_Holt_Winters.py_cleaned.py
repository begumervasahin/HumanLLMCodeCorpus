import numpy as np
import matplotlib.pyplot as plt
def exponential_smoothing(alpha, s):
    smoothed_series = np.zeros(s.shape)
    smoothed_series[0] = s[0]
    for i in range(1, len(s)):
        smoothed_series[i] = alpha * s[i] + (1 - alpha) * smoothed_series[i - 1]
    return smoothed_series
def predict_double_exponential(s_single, s_double, alpha):
    a_double = 2 * s_single - s_double
    b_double = (alpha / (1 - alpha)) * (s_single - s_double)
    return a_double + b_double
def predict_triple_exponential(s_single, s_double, s_triple, alpha):
    a_triple = 3 * s_single - 3 * s_double + s_triple
    b_triple = (alpha / (2 * ((1 - alpha) ** 2))) * (
                (6 - 5 * alpha) * s_single - 2 * ((5 - 4 * alpha) * s_double) + (4 - 3 * alpha) * s_triple)
    c_triple = ((alpha ** 2) / (2 * ((1 - alpha) ** 2))) * (s_single - 2 * s_double + s_triple)
    return a_triple + b_triple + c_triple
def extend_year_array(year, pre_year):
    return np.insert(year, len(year), values=pre_year, axis=0)
def extend_predicted_array(s_pre, last_values, alpha, prediction_years):
    extension = np.array([last_values[-1] + alpha * i for i in range(1, prediction_years + 1)])
    return np.insert(s_pre, len(s_pre), values=extension, axis=0)
def load_and_preprocess_data(data_path):
    data = np.loadtxt(data_path)
    year, time_id, number = data.T
    initial_data = np.insert(data, 0, values=[0, 0, number[0]], axis=0)
    return initial_data.T
def main():
    alpha = 0.70
    pre_year = np.array([2016, 2017])
    data_path = 'data1.txt'
    initial_year, initial_time_id, initial_number = load_and_preprocess_data(data_path)
    s_single = exponential_smoothing(alpha, initial_number)
    s_double =