import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
def load_data(file_path):
    data = pd.read_csv(file_path)
    print("Dataset shape: {} data points with {} variables each.".format(*data.shape))
    return data
def extract_features(data):
    features = data.drop(['Date', 'Time', 'Close', 'High', 'Low', 'Total Ticks'], axis=1)
    return features
def extract_close_prices(data):
    close_prices = data['Close']
    return close_prices
def predict_price_movement(opening_value, data):
    features = extract_features(data)
    close_prices = extract_close_prices(data)
    X_train, X_test, y_train, y_test = train_test_split(features, close_prices, test_size=0.4, shuffle=True, random_state=101)
    regressor = DecisionTreeRegressor(random_state=0)
    regressor.fit(X_train, y_train)
    prediction = regressor.predict([[opening_value]])
    if prediction > opening_value:
        return "Predicted movement: up"
    else:
        return "Predicted movement: down"
if __name__ == "__main__":
    file_path = 'AUDJPY_2.csv'
    opening_value = 85.226
    prediction = predict_price_movement(opening_value, load_data(file_path))
    print(prediction)