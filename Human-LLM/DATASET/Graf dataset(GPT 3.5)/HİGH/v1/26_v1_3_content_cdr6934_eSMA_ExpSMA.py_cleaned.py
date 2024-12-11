import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def fonk1(b6, window):
    return b6.ewm(b1 = window).mean()
def fonk2(filename):
    b2 = pd.read_csv(filename)
    b2['Date'] = pd.to_datetime(b2['Date'])
    return b2.sort_values(b3 = 'Date')
def fonk3(window_default):
    b4 = input(format('Enter Long Term Window or Enter to Default ({0} Weeks):'.format(window_default)))
    if b4 = = '':
        b4 = window_default
    return int(b4 * 5)
def fonk4():
    b5 = fonk2("b6/goog.csv")
    b6 = pd.Series(np.float32(b5['Close']), index=b5['Date'])
    b7 = fonk1(b6, fonk3(4))
    b8 = fonk1(b6, fonk3(2))
    b9 = b7 - b8
    b10 = fonk1(b9, 7.5)
    b11 = b10 - b9
    b11.plot(b12 = 'k', title="2nd Derivative GOOG Close Price")
    plt.show()
if b13 = = '__main__':
    fonk4()