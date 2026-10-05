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
    stock = import_clean_ts("data/goog.csv")
    data = pd.Series(np.float32(stock['Close']), index=stock['Date'])
    lt_av = generate_exponential_sma(data, collect_user_input(4))
    st_av = generate_exponential_sma(data, collect_user_input(2))
    diff_ltst = lt_av - st_av
    diff_ltst_av = generate_exponential_sma(diff_ltst, 7.5)
    diff_av_diff = diff_ltst_av - diff_ltst
    diff_av_diff.plot(style='k', title="2nd Derivative of GOOG Close Price")
    plt.show()
if __name__ == '__main__':
    main()