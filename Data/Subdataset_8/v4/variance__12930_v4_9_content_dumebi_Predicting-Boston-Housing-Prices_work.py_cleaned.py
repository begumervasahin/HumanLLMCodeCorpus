import sys
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
regressor = DecisionTreeRegressor(random_state=0)
def load_data():
    work_data = pd.read_csv('AUDJPY_2.csv')
    print("The work dataset has {} data points with {} variables each.".format(*work_data.shape))
    return work_data
def get_features(data):
    features = data.drop(['Date', 'Time', 'Close', 'High', 'Low', 'Total Ticks'], axis=1)
    return features
def get_close(data):
    close = data.drop(['Date', 'Time', 'Open', 'High', 'Low', 'Total Ticks'], axis=1)
    return close
def predict(open_value):
    data = load_data()
    features = get_features(data)
    close = get_close(data)
    X_train, X_test, y_train, y_test = train_test_split(features, close, test_size=0.4, shuffle=True, random_state=101)
    regressor.fit(X_train, y_train)
    test = np.array([[open_value]])
    pred = regressor.predict(test)
    if pred > open_value:
        return "Up"
    else:
        return "Down"
pred = predict(85.226)
print("Prediction:", pred)