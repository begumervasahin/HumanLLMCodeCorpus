
import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
from sklearn.metrics import r2_score
b1 = pd.read_csv("FuelConsumption.csv")
b1.head()
b2 = b1[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
b2.head(9)
plt.scatter(b2.ENGINESIZE, b2.CO2EMISSIONS,  b3 = 'blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()
b4 = np.random.rand(len(b1)) < 0.8
b5 = b2[b4]
b6 = b2[~b4]
b7 = np.asanyarray(b5[['ENGINESIZE']])
b8 = np.asanyarray(b5[['CO2EMISSIONS']])
b9 = np.asanyarray(b6[['ENGINESIZE']])
b10 = np.asanyarray(b6[['CO2EMISSIONS']])
b11 = PolynomialFeatures(degree=2)
b12 = b11.fit_transform(b7)
b12
b13 = linear_model.LinearRegression()
b14 = b13.fit(b12, b8)
print ('Coefficients: ', b13.coef_)
print ('Intercept: ',b13.intercept_)
plt.scatter(b5.ENGINESIZE, b5.CO2EMISSIONS,  b3 = 'blue')
b15 = np.arange(0.0, 10.0, 0.1)
b16 = b13.intercept_[0]+ b13.coef_[0][1]*b15+ b13.coef_[0][2]*np.power(b15, 2)
plt.plot(b15, b16, '-r' )
plt.xlabel("Engine size")
plt.ylabel("Emission")
b17 = b11.fit_transform(b9)
b18 = b13.predict(b17)
print("Mean absolute error: %.2f" % np.mean(np.absolute(b18 - b10)))
print("Residual sum of squares (MSE): %.2f" % np.mean((b18 - b10) ** 2))
print("R2-score: %.2f" % r2_score(b18 , b10) )
b19 = PolynomialFeatures(degree=3)
b20 = b19.fit_transform(b7)
b21 = linear_model.LinearRegression()
b22 = b21.fit(b20, b8)
print ('Coefficients: ', b21.coef_)
print ('Intercept: ',b21.intercept_)
plt.scatter(b5.ENGINESIZE, b5.CO2EMISSIONS,  b3 = 'blue')
b15 = np.arange(0.0, 10.0, 0.1)
b16 = b21.intercept_[0]+ b21.coef_[0][1]*b15 + b21.coef_[0][2]*np.power(b15, 2) + b21.coef_[0][3]*np.power(b15, 3)
plt.plot(b15, b16, '-r' )
plt.xlabel("Engine size")
plt.ylabel("Emission")
b23 = b19.fit_transform(b9)
b24 = b21.predict(b23)
print("Mean absolute error: %.2f" % np.mean(np.absolute(b24 - b10)))
print("Residual sum of squares (MSE): %.2f" % np.mean((b24 - b10) ** 2))
print("R2-score: %.2f" % r2_score(b24 , b10) )