import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
b1 = pd.read_csv("maize.csv", usecols = ['Year'], nrows = 54)
b2 = np.array(b1)
b3 = b2.ravel()
b4 = pd.read_csv("maize.csv", usecols = ['Crop'], nrows = 54)
b5 = np.array(b4)
b6 = LinearRegression()
b6.fit(b2, b5)
b7 = b6.predict(b2)
b8 = mean_squared_error(b5, b7)
b9 = r2_score(b5, b7)
print('The RMSE of the linear regression b6 is {}'.format(b8))
print('The R2 score of the linear regression b6 is {}'.format(b9))
b10 = np.array([2015, 2016, 2017, 2018, 2019, 2020])
b11 = b10[:, np.newaxis]
b12 = b6.predict(b11)
b12 = np.round(b12,4)
b13 = np.concatenate((b3, b10))
b14 = np.concatenate((b7, b12))
b15 = np.concatenate((b5, b12))
b16 = b10
b17 = b12
b18 = pd.read_csv("maize.csv", usecols = ['Entity'], nrows=54)
b18 = np.array(b18)
b18 = b18.ravel()
b19 = b18[0:6]
b18 = np.concatenate((b18, b19))
b20 = pd.read_csv("maize.csv", usecols=['Code'], nrows=54)
b20 = np.array(b20)
b20 = b20.ravel()
b21 = b20[0:6]
b20 = np.concatenate((b20, b21))
b22 = {
        'Entity' : b18,
        'Code' : b20,
        'Year': b13,
        'crop(tonnes per hectare)': b15.ravel()
        }
b23 = DataFrame(b22, columns= ['Entity','Code','Year', 'crop(tonnes per hectare)'])
b24 = b23.to_csv(r'/home/leathea/Downloads/Machine-Learning/PolynomialRegression/test.csv', index = None, header=True)
plt.scatter(b2, b5, b25 = 10, b26='c')
plt.scatter(b16, b17, b25 = 10, b26='r')
plt.plot(b13, b14, b26 = 'm')
plt.show()