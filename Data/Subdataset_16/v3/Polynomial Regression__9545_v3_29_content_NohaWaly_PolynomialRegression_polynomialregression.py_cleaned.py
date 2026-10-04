import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
def fonk1(filepath):
    b1 = pd.read_csv(filepath)
    b2 = b1[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]
    return b2
def fonk2(b1, b3 = 0.8):
    b4 = np.random.rand(len(b1)) < b3
    b5 = b1[b4]
    b6 = b1[~b4]
    return b5, b6
def fonk3(b5, b6, feature, target):
    b7 = b5[[feature]].values
    b8 = b5[[target]].values
    b9 = b6[[feature]].values
    b10 = b6[[target]].values
    return b7, b8, b9, b10
def fonk4(x, y, xlabel, ylabel, b11 = 'blue'):
    plt.scatter(x, y, b11 = b11)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
def fonk5(b19, b7, b8, b9, b10):
    b12 = PolynomialFeatures(b19=b19)
    b13 = b12.fit_transform(b7)
    b14 = LinearRegression()
    b14.fit(b13, b8)
    print(f'Degree {b19} Polynomial Regression:')
    print('Coefficients:', b14.coef_)
    print('Intercept:', b14.intercept_)
    plt.scatter(b7, b8, b11 = 'blue')
    b15 = np.arange(0.0, 10.0, 0.1)
    b16 = b14.intercept_[0]
    for i in range(1, b19 + 1):
        b16 += b14.coef_[0][i] * np.power(b15, i)
    plt.plot(b15, b16, '-r')
    plt.xlabel("Engine size")
    plt.ylabel("Emission")
    plt.show()
    b17 = b12.transform(b9)
    b18 = b14.predict(b17)
    print("Mean absolute error: %.2f" % np.mean(np.absolute(b18 - b10)))
    print("Residual sum of squares (MSE): %.2f" % np.mean((b18 - b10) ** 2))
    print("R2-score: %.2f" % r2_score(b18, b10))
def fonk6():
    b2 = fonk1("FuelConsumption.csv")
    fonk4(b2.ENGINESIZE, b2.CO2EMISSIONS, "Engine size", "Emission")
    b5, b6 = fonk2(b2)
    b7, b8, b9, b10 = fonk3(b5, b6, 'ENGINESIZE', 'CO2EMISSIONS')
    fonk5(b19 = 2, b7=b7, b8=b8, b9=b9, b10=b10)
    fonk5(b19 = 3, b7=b7, b8=b8, b9=b9, b10=b10)
if b20 = = "__main__":
    fonk6()