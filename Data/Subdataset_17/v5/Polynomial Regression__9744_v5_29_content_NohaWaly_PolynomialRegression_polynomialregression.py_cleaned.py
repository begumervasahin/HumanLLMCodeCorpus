
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
def load_and_preview_data(file_path):
    df = pd.read_csv(file_path)
    print(df.head())
    return df
def select_features(df):
    selected_df = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]
    print(selected_df.head(9))
    return selected_df
def plot_engine_size_vs_emissions(data):
    plt.scatter(data.ENGINESIZE, data.CO2EMISSIONS, color='blue')
    plt.xlabel("Engine size")
    plt.ylabel("Emission")
    plt.show()
def split_data(data, split_ratio=0.8):
    mask = np.random.rand(len(data)) < split_ratio
    train = data[mask]
    test = data[~mask]
    return train, test
def prepare_polynomial_regression(train_x, degree=2):
    poly = PolynomialFeatures(degree=degree)
    train_x_poly = poly.fit_transform(train_x)
    model = LinearRegression()
    model.fit(train_x_poly, train_y)
    return model, poly
def plot_regression_line(model, poly, train, degree=2):
    plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color='blue')
    XX = np.arange(0.0, 10.0, 0.1)
    yy = sum([model.coef_[0][i] * np.power(XX, i) for i in range(degree + 1)]) + model.intercept_[0]
    plt.plot(XX, yy, '-r')
    plt.xlabel("Engine size")
    plt.ylabel("Emission")
    plt.show()
def evaluate_model(model, poly, test_x, test_y):
    test_x_poly = poly.transform(test_x)
    test_y_pred = model.predict(test_x_poly)
    print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_pred - test_y)))
    print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_pred - test_y) ** 2))
    print("R2-score: %.2f" % r2_score(test_y_pred, test_y))
df = load_and_preview_data("FuelConsumption.csv")
cdf = select_features(df)
plot_engine_size_vs_emissions(cdf)
train, test = split_data(cdf)
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
test_x = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
model, poly = prepare_polynomial_regression(train_x, degree=2)
print('Coefficients:', model.coef_)
print('Intercept:', model.intercept_)
plot_regression_line(model, poly, train, degree=2)
evaluate_model(model, poly, test_x, test_y)
model3, poly3 = prepare_polynomial_regression(train_x, degree=3)
print('Coefficients:', model3.coef_)
print('Intercept:', model3.intercept_)
plot_regression_line(model3, poly3, train, degree=3)
evaluate_model(model3, poly3, test_x, test_y)