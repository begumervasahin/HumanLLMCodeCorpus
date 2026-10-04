import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def generate_exponential_sma(data, window):
    return data.ewm(span=window).mean()
def import_clean_ts(filename):
    ts_data = pd.read_csv(filename)
    ts_data['Date'] = pd.to_datetime(ts_data['Date'])
    ts_data.sort_values(by='Date', inplace=True)
    return ts_data
def collect_user_input(window_default):
    user_input = input(f'Enter Long Term Window or press Enter to use default ({window_default} Weeks): ')
    if not user_input:
        return window_default * 5
    return int(user_input) * 5
def main():
    stock_data = import_clean_ts("data/goog.csv")
    stock_close_prices = pd.Series(np.float32(stock_data['Close']), index=stock_data['Date'])
    long_term_window = collect_user_input(4)
    short_term_window = collect_user_input(2)
    long_term_sma = generate_exponential_sma(stock_close_prices, long_term_window)
    short_term_sma = generate_exponential_sma(stock_close_prices, short_term_window)
    diff_long_short = long_term_sma - short_term_sma
    smoothed_diff = generate_exponential_sma(diff_long_short, 7.5)
    second_derivative = smoothed_diff - diff_long_short
    plt.figure(figsize=(10, 6))
    second_derivative.plot(style='k', title="2nd Derivative of GOOG Close Price")
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.show()
if __name__ == '__main__':
    main()