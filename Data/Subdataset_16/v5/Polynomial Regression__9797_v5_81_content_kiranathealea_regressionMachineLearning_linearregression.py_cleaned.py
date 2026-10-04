import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
b1 = pd.read_csv("maize.csv", usecols=['Year', 'Crop', 'Entity', 'Code'], nrows=54)
b2 = b1['Year'].values.reshape(-1, 1)
b3 = b1['Crop'].values
b4 = LinearRegression()
b4.fit(b2, b3)
b5 = b4.predict(b2)
b6 = mean_squared_error(b3, b5)
b7 = r2_score(b3, b5)
print(f'The RMSE of the linear regression b4 is {b6}')
print(f'The R2 score of the linear regression b4 is {b7}')
b8 = np.array([2015, 2016, 2017, 2018, 2019, 2020]).reshape(-1, 1)
b9 = b4.predict(b8)
b9 = np.round(b9, 4)
b10 = np.concatenate((b2.ravel(), b8.ravel()))
b11 = np.concatenate((b5, b9))
b12 = np.concatenate((b3, b9))
b13 = b1['Entity'].values
b14 = np.concatenate((b13, b13[:6]))
b15 = b1['Code'].values
b16 = np.concatenate((b15, b15[:6]))
b17 = {
    'Entity': b14,
    'Code': b16,
    'Year': b10,
    'crop(tonnes per hectare)': b12
}
b18 = DataFrame(b17, columns=['Entity', 'Code', 'Year', 'crop(tonnes per hectare)'])
b18.to_csv('/home/leathea/Downloads/Machine-Learning/PolynomialRegression/test.csv', b19 = False)
plt.scatter(b2, b3, b20 = 10, b21='c', label='Actual Data')
plt.scatter(b8, b9, b20 = 10, b21='r', label='Predicted Future Data')
plt.plot(b10, b11, b21 = 'm', label='Regression Line')
plt.xlabel('Year')
plt.ylabel('Crop (tonnes per hectare)')
plt.legend()
plt.show()