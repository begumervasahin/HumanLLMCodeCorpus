import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def generate_exponential_sma(data, window):
    return data.ewm(span=window).mean()
def import_clean_ts(filename):
    ts_data = pd.read_csv(filename)
    ts_data['Date'] = pd.to_datetime(ts_data['Date'])
    return ts_data.sort_values(by='Date')
def collect_user_input(window_default):
    user_input = input("Enter the Long Term Window or press Enter for default ({0} Weeks): ".format(window_default))
    if user_input == '':
        user_input = window_default
    return int(user_input * 5)
def main():
    stock_data = import_clean_ts("data/goog.csv")
    close_prices = pd.Series(np.float32(stock_data['Close']), index=stock_data['Date'])
    long_term_window = collect_user_input(4)
    short_term_window = collect_user_input(2)
    long_term_average = generate_exponential_sma(close_prices, long_term_window)
    short_term_average = generate_exponential_sma(close_prices, short_term_window)
    difference = long_term_average - short_term_average
    second_derivative = generate_exponential_sma(difference, 7.5)
    second_derivative_diff = second_derivative - difference
    second_derivative_diff.plot(style='k', title="2nd Derivative of GOOG Close Price")
    plt.show()
if __name__ == '__main__':
    main()