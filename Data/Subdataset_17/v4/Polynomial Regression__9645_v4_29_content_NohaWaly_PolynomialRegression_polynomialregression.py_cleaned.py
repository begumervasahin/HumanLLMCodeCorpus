
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
df = pd.read_csv("FuelConsumption.csv")
print(df.head())
cdf = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]
print(cdf.head(9))
plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS, color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()
mask = np.random.rand(len(df)) < 0.8
train = cdf[mask]
test = cdf[~mask]
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
test_x = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
poly = PolynomialFeatures(degree=2)
train_x_poly = poly.fit_transform(train_x)
model = LinearRegression()
model.fit(train_x_poly, train_y)
print('Coefficients:', model.coef_)
print('Intercept:', model.intercept_)
plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color='blue')
XX = np.arange(0.0, 10.0, 0.1)
yy = model.intercept_[0] + model.coef_[0][1] * XX + model.coef_[0][2] * np.power(XX, 2)
plt.plot(XX, yy, '-r')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()
test_x_poly = poly.transform(test_x)
test_y_pred = model.predict(test_x_poly)
print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_pred - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_pred - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y_pred, test_y))
poly3 = PolynomialFeatures(degree=3)
train_x_poly3 = poly3.fit_transform(train_x)
model3 = LinearRegression()
model3.fit(train_x_poly3, train_y)
print('Coefficients:', model3.coef_)
print('Intercept:', model3.intercept_)
plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color='blue')
yy3 = model3.intercept_[0] + model3.coef_[0][1] * XX + model3.coef_[0][2] * np.power(XX, 2) + model3.coef_[0][3] * np.power(XX, 3)
plt.plot(XX, yy3, '-r')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()
test_x_poly3 = poly3.transform(test_x)
test_y_pred3 = model3.predict(test_x_poly3)
print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_pred3 - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_pred3 - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y_pred3, test_y))