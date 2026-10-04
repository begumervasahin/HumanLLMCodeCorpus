
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
def fonk1(file_path):
    b1 = pd.read_csv(file_path)
    print(b1.head())
    return b1
def fonk2(b1):
    b2 = b1[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]
    print(b2.head(9))
    return b2
def fonk3(data):
    plt.scatter(data.ENGINESIZE, data.CO2EMISSIONS, b3 = 'blue')
    plt.xlabel("Engine size")
    plt.ylabel("Emission")
    plt.show()
def fonk4(data, b4 = 0.8):
    b5 = np.random.rand(len(data)) < b4
    b6 = data[b5]
    b7 = data[~b5]
    return b6, b7
def fonk5(b17, b8 = 2):
    b9 = PolynomialFeatures(b8=b8)
    b10 = b9.fit_transform(b17)
    b11 = LinearRegression()
    b11.fit(b10, b18)
    return b11, b9
def fonk6(b11, b9, b6, b8 = 2):
    plt.scatter(b6.ENGINESIZE, b6.CO2EMISSIONS, b3 = 'blue')
    b12 = np.arange(0.0, 10.0, 0.1)
    b13 = sum([b11.coef_[0][i] * np.power(b12, i) for i in range(b8 + 1)]) + b11.intercept_[0]
    plt.plot(b12, b13, '-r')
    plt.xlabel("Engine size")
    plt.ylabel("Emission")
    plt.show()
def fonk7(b11, b9, b19, b20):
    b14 = b9.transform(b19)
    b15 = b11.predict(b14)
    print("Mean absolute error: %.2f" % np.mean(np.absolute(b15 - b20)))
    print("Residual sum of squares (MSE): %.2f" % np.mean((b15 - b20) ** 2))
    print("R2-score: %.2f" % r2_score(b15, b20))
b1 = fonk1("FuelConsumption.csv")
b16 = fonk2(b1)
fonk3(b16)
b6, b7 = fonk4(b16)
b17 = np.asanyarray(b6[['ENGINESIZE']])
b18 = np.asanyarray(b6[['CO2EMISSIONS']])
b19 = np.asanyarray(b7[['ENGINESIZE']])
b20 = np.asanyarray(b7[['CO2EMISSIONS']])
b11, b9 = fonk5(b17, b8=2)
print('Coefficients:', b11.coef_)
print('Intercept:', b11.intercept_)
fonk6(b11, b9, b6, b8 = 2)
fonk7(b11, b9, b19, b20)
model3, b21 = fonk5(b17, b8=3)
print('Coefficients:', model3.coef_)
print('Intercept:', model3.intercept_)
fonk6(model3, b21, b6, b8 = 3)
fonk7(model3, b21, b19, b20)