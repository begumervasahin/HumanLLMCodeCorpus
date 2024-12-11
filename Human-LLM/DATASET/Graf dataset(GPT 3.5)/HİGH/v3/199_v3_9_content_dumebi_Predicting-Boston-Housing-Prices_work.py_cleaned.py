import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
def fonk1(b8):
    b1 = pd.read_csv(b8)
    print("Dataset shape: {} b1 points with {} variables each.".format(*b1.shape))
    return b1
def fonk2(b1):
    b2 = b1.drop(['Date', 'Time', 'Close', 'High', 'Low', 'Total Ticks'], axis=1)
    return b2
def fonk3(b1):
    b3 = b1['Close']
    return b3
def fonk4(a1, b1):
    b2 = fonk2(b1)
    b3 = fonk3(b1)
    X_train, X_test, y_train, b4 = train_test_split(b2, b3, test_size=0.4, shuffle=True, random_state=101)
    b5 = DecisionTreeRegressor(random_state=0)
    b5.fit(X_train, y_train)
    b6 = b5.predict([[a1]])
    if b6 > a1:
        return "Predicted movement: up"
    else:
        return "Predicted movement: down"
if b7 = = "__main__":
    b8 = 'AUDJPY_2.csv'
    a1 = 85.226
    b6 = fonk4(a1, fonk1(b8))
    print(b6)