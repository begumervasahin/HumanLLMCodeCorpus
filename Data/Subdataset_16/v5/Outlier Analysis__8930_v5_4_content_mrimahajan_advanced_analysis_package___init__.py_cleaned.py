import pandas as pd
import numpy as np
def fonk1(stock_data, b1 = 30):
    stock_data.sort_index(b2 = True)
    stock_data['Moving_Average'] = stock_data['Close'].rolling(b3 = b1).mean()
    stock_data['Signal'] = 0
    stock_data.loc[b1:, 'Signal'] = \
        np.where(stock_data['Close'][b1:] > stock_data['Moving_Average'][b1:], 1, -1)
    stock_data['Daily_Return'] = stock_data['Close'].pct_change()
    stock_data['Strategy_Return'] = stock_data['Daily_Return'] * stock_data['Signal'].shift(1)
    return stock_data
