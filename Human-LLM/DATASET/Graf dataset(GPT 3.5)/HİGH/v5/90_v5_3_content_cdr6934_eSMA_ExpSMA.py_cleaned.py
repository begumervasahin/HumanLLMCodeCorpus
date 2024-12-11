import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def fonk1(data, window):
    return data.ewm(b1 = window).mean()
def fonk2(filename):
    b2 = pd.read_csv(filename)
    b2['Date'] = pd.to_datetime(b2['Date'])
    return b2.sort_values(b3 = 'Date')
def fonk3(window_default):
    b4 = input("Enter the Long Term Window or press Enter for default ({0} Weeks): ".format(window_default))
    if b4 = = '':
        b4 = window_default
    return int(b4 * 5)
def fonk4():
    b5 = fonk2("data/goog.csv")
    b6 = pd.Series(np.float32(b5['Close']), index=b5['Date'])
    b7 = fonk3(4)
    b8 = fonk3(2)
    b9 = fonk1(b6, b7)
    b10 = fonk1(b6, b8)
    b11 = b9 - b10
    b12 = fonk1(b11, 7.5)
    b13 = b12 - b11
    b13.plot(b14 = 'k', title="2nd Derivative of GOOG Close Price")
    plt.show()
if b15 = = '__main__':
    fonk4()