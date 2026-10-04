def analyze_stock_data(stock_data, moving_average_window=30):
    stock_data = stock_data.sort_index()
    stock_data['Moving_Average'] = stock_data['Close'].rolling(window=moving_average_window).mean()
    stock_data['Signal'] = 0
    stock_data['Signal'][moving_average_window:] = \
        np.where(stock_data['Close'][moving_average_window:] > stock_data['Moving_Average'][moving_average_window:], 1, -1)
    stock_data['Daily_Return'] = stock_data['Close'].pct_change()
    stock_data['Strategy_Return'] = stock_data['Daily_Return'] * stock_data['Signal'].shift(1)
    return stock_data