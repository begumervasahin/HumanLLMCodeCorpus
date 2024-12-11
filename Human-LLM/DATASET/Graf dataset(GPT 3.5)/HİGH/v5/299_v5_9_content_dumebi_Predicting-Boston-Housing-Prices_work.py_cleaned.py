import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
b1 = DecisionTreeRegressor(random_state=0)
def fonk1():
    b2 = pd.read_csv('AUDJPY_2.csv')
    print(f"The b2 contains {b2.shape[0]} data points with {b2.shape[1]} variables each.")
    return b2
def fonk2(data):
    b3 = data.drop(['Date', 'Time', 'Close', 'High', 'Low', 'Total Ticks'], axis=1)
    return b3
def fonk3(data):
    b4 = data['Close']
    return b4
def fonk4(open_price):
    b2 = fonk1()
    b3 = fonk2(b2)
    b4 = fonk3(b2)
    X_train, X_test, y_train, b5 = train_test_split(b3, b4, test_size=0.4, shuffle=True, random_state=101)
    b1.fit(X_train, y_train)
    b6 = [[open_price]]
    b7 = b1.predict(b6)
    if b7 > open_price:
        return "Up"
    else:
        return "Down"
b8 = fonk4(85.226)
print("Predicted Direction:", b8)