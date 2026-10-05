import sys
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
b1 = DecisionTreeRegressor(random_state=0)
def fonk1():
    b2 = pd.read_csv('AUDJPY_2.csv')
    print "work dataset has {} b5 points with {} variables each.".format(*b2.shape)
    return b2
def fonk2(b5):
    b3 = b5.drop(['Date', 'Time', 'Close', 'High', 'Low', 'Total Ticks'], axis = 1)
    return b3
def fonk3(b5):
    b4 = b5.drop(['Date', 'Time', 'Open', 'High', 'Low', 'Total Ticks'], axis = 1)
    return b4
def fonk4(open):
    b5 = fonk1()
    b3 = fonk2(b5)
    b4 = fonk3(b5)
    print b3.head(10)
    print b4.shape
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, b6 = train_test_split(b3, b4, test_size=0.4, shuffle=True, random_state=101)
    b1.fit(X_train, y_train)
    b7 = np.array([[open]])
    b8 = b1.fonk4(b7)
    if(b8 > open):
        return "up"
    else:
        return "down"
b8 = fonk4(85.226)
print b8