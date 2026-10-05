import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
regressor = DecisionTreeRegressor(random_state=0)
def load_dataset():
    dataset = pd.read_csv('AUDJPY_2.csv')
    print(f"The dataset contains {dataset.shape[0]} data points with {dataset.shape[1]} variables each.")
    return dataset
def extract_features(data):
    features = data.drop(['Date', 'Time', 'Close', 'High', 'Low', 'Total Ticks'], axis=1)
    return features
def extract_close_prices(data):
    close_prices = data['Close']
    return close_prices
def predict_price(open_price):
    dataset = load_dataset()
    features = extract_features(dataset)
    close_prices = extract_close_prices(dataset)
    X_train, X_test, y_train, y_test = train_test_split(features, close_prices, test_size=0.4, shuffle=True, random_state=101)
    regressor.fit(X_train, y_train)
    open_price_array = [[open_price]]
    predicted_price = regressor.predict(open_price_array)
    if predicted_price > open_price:
        return "Up"
    else:
        return "Down"
predicted_direction = predict_price(85.226)
print("Predicted Direction:", predicted_direction)