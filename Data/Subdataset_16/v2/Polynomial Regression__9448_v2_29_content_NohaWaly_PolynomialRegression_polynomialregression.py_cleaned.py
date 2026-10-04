import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
b1 = pd.read_csv("FuelConsumption.csv")
b2 = b1[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]
plt.scatter(b2.ENGINESIZE, b2.CO2EMISSIONS, b3 = 'blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()
b4 = np.random.rand(len(b1)) < 0.8
b5 = b2[b4]
b6 = b2[~b4]
b7 = b5[['ENGINESIZE']].values
b8 = b5[['CO2EMISSIONS']].values
b9 = b6[['ENGINESIZE']].values
b10 = b6[['CO2EMISSIONS']].values
def fonk1(b18, b7, b8, b9, b10):
    b11 = PolynomialFeatures(b18=b18)
    b12 = b11.fit_transform(b7)
    b13 = LinearRegression()
    b13.fit(b12, b8)
    print(f'Degree {b18} Polynomial Regression:')
    print('Coefficients:', b13.coef_)
    print('Intercept:', b13.intercept_)
    plt.scatter(b5.ENGINESIZE, b5.CO2EMISSIONS, b3 = 'blue')
    b14 = np.arange(0.0, 10.0, 0.1)
    b15 = b13.intercept_[0]
    for i in range(1, b18 + 1):
        b15 += b13.coef_[0][i] * np.power(b14, i)
    plt.plot(b14, b15, '-r')
    plt.xlabel("Engine size")
    plt.ylabel("Emission")
    plt.show()
    b16 = b11.transform(b9)
    b17 = b13.predict(b16)
    print("Mean absolute error: %.2f" % np.mean(np.absolute(b17 - b10)))
    print("Residual sum of squares (MSE): %.2f" % np.mean((b17 - b10) ** 2))
    print("R2-score: %.2f" % r2_score(b17, b10))
fonk1(b18 = 2, b7=b7, b8=b8, b9=b9, b10=b10)
fonk1(b18 = 3, b7=b7, b8=b8, b9=b9, b10=b10)