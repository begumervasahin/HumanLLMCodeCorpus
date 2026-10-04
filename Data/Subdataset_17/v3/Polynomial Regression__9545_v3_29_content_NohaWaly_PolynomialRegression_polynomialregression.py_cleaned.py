import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
def load_and_preprocess_data(filepath):
    df = pd.read_csv(filepath)
    cdf = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]
    return cdf
def split_data(df, train_ratio=0.8):
    msk = np.random.rand(len(df)) < train_ratio
    train = df[msk]
    test = df[~msk]
    return train, test
def prepare_data(train, test, feature, target):
    train_x = train[[feature]].values
    train_y = train[[target]].values
    test_x = test[[feature]].values
    test_y = test[[target]].values
    return train_x, train_y, test_x, test_y
def plot_scatter(x, y, xlabel, ylabel, color='blue'):
    plt.scatter(x, y, color=color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
def polynomial_regression(degree, train_x, train_y, test_x, test_y):
    poly = PolynomialFeatures(degree=degree)
    train_x_poly = poly.fit_transform(train_x)
    model = LinearRegression()
    model.fit(train_x_poly, train_y)
    print(f'Degree {degree} Polynomial Regression:')
    print('Coefficients:', model.coef_)
    print('Intercept:', model.intercept_)
    plt.scatter(train_x, train_y, color='blue')
    XX = np.arange(0.0, 10.0, 0.1)
    yy = model.intercept_[0]
    for i in range(1, degree + 1):
        yy += model.coef_[0][i] * np.power(XX, i)
    plt.plot(XX, yy, '-r')
    plt.xlabel("Engine size")
    plt.ylabel("Emission")
    plt.show()
    test_x_poly = poly.transform(test_x)
    test_y_pred = model.predict(test_x_poly)
    print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_pred - test_y)))
    print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_pred - test_y) ** 2))
    print("R2-score: %.2f" % r2_score(test_y_pred, test_y))
def main():
    cdf = load_and_preprocess_data("FuelConsumption.csv")
    plot_scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS, "Engine size", "Emission")
    train, test = split_data(cdf)
    train_x, train_y, test_x, test_y = prepare_data(train, test, 'ENGINESIZE', 'CO2EMISSIONS')
    polynomial_regression(degree=2, train_x=train_x, train_y=train_y, test_x=test_x, test_y=test_y)
    polynomial_regression(degree=3, train_x=train_x, train_y=train_y, test_x=test_x, test_y=test_y)
if __name__ == "__main__":
    main()