import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
def load_data(file_path):
    work_data = pd.read_csv(file_path)
    print("Work dataset has {} data points with {} variables each.".format(*work_data.shape))
    return work_data
def get_features(data):
    features = data.drop(['Date', 'Time', 'Close', 'High', 'Low', 'Total Ticks'], axis=1)
    return features
def get_close(data):
    close = data['Close']
    return close
def predict(open_value, file_path):
    data = load_data(file_path)
    features = get_features(data)
    close = get_close(data)
    X_train, X_test, y_train, y_test = train_test_split(features, close, test_size=0.4, shuffle=True, random_state=101)
    regressor = DecisionTreeRegressor(random_state=0)
    regressor.fit(X_train, y_train)
    test = np.array([[open_value]])
    pred = regressor.predict(test)
    if pred > open_value:
        return "up"
    else:
        return "down"
if __name__ == "__main__":
    file_path = 'AUDJPY_2.csv'
    open_value = 85.226
    pred = predict(open_value, file_path)
    print(pred)