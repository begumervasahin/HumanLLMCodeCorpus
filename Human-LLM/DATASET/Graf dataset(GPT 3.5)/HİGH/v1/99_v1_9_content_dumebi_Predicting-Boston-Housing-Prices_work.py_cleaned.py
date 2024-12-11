import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
def fonk1(b10):
    b1 = pd.read_csv(b10)
    print("Work dataset has {} b4 points with {} variables each.".format(*b1.shape))
    return b1
def fonk2(b4):
    b2 = b4.drop(['Date', 'Time', 'Close', 'High', 'Low', 'Total Ticks'], axis=1)
    return b2
def fonk3(b4):
    b3 = b4['Close']
    return b3
def fonk4(a1, b10):
    b4 = fonk1(b10)
    b2 = fonk2(b4)
    b3 = fonk3(b4)
    X_train, X_test, y_train, b5 = train_test_split(b2, b3, test_size=0.4, shuffle=True, random_state=101)
    b6 = DecisionTreeRegressor(random_state=0)
    b6.fit(X_train, y_train)
    b7 = np.array([[a1]])
    b8 = b6.fonk4(b7)
    if b8 > a1:
        return "up"
    else:
        return "down"
if b9 = = "__main__":
    b10 = 'AUDJPY_2.csv'
    a1 = 85.226
    b8 = fonk4(a1, b10)
    print(b8)