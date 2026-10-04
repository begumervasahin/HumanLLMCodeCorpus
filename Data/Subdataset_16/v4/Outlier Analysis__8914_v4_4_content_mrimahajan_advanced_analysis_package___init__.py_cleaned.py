def fonk1(b2, b1 = 30):
    b2 = b2.sort_index()
    b2['Moving_Average'] = b2['Close'].rolling(b3 = b1).mean()
    b2['Signal'] = 0
    b2['Signal'][b1:] = \
        np.where(b2['Close'][b1:] > b2['Moving_Average'][b1:], 1, -1)
    b2['Daily_Return'] = b2['Close'].pct_change()
    b2['Strategy_Return'] = b2['Daily_Return'] * b2['Signal'].shift(1)
    return b2