import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
df = pd.read_csv("FuelConsumption.csv")
cdf = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]
plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS, color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()
msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]
train_x = train[['ENGINESIZE']].values
train_y = train[['CO2EMISSIONS']].values
test_x = test[['ENGINESIZE']].values
test_y = test[['CO2EMISSIONS']].values
def plot_polynomial_regression(degree, train_x, train_y, test_x, test_y):
    poly = PolynomialFeatures(degree=degree)
    train_x_poly = poly.fit_transform(train_x)
    model = LinearRegression()
    model.fit(train_x_poly, train_y)
    print(f'Degree {degree} Polynomial Regression:')
    print('Coefficients:', model.coef_)
    print('Intercept:', model.intercept_)
    plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color='blue')
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
plot_polynomial_regression(degree=2, train_x=train_x, train_y=train_y, test_x=test_x, test_y=test_y)
plot_polynomial_regression(degree=3, train_x=train_x, train_y=train_y, test_x=test_x, test_y=test_y)