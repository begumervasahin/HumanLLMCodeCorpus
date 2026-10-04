import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
def load_data(filepath):
    dataset = pd.read_csv(filepath)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, 1].values
    return X, y
def split_data(X, y, test_size=1/3, random_state=0):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
def train_model(X_train, y_train):
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    return regressor
def visualize_results(X, y, model, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, color='red', label='Actual Data')
    plt.plot(X, model.predict(X), color='blue', label='Regression Line')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()
def main():
    X, y = load_data('Data.csv')
    X_train, X_test, y_train, y_test = split_data(X, y)
    model = train_model(X_train, y_train)
    visualize_results(X_train, y_train, model, 'Salary vs Experience (Training Set)', 'Years of Experience', 'Salary')
    visualize_results(X_test, y_test, model, 'Salary vs Experience (Test Set)', 'Years of Experience', 'Salary')
if __name__ == "__main__":
    main()