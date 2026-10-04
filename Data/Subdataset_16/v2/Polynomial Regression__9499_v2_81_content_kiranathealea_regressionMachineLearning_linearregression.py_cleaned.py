import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
b1 = pd.read_csv("maize.csv", usecols=['Year', 'Crop', 'Entity', 'Code'], nrows=54)
b2 = b1['Year'].values.reshape(-1, 1)
b3 = b1['Crop'].values.reshape(-1, 1)
b4 = LinearRegression()
b4.fit(b2, b3)
b5 = b4.predict(b2)
b6 = mean_squared_error(b3, b5, squared=False)
b7 = r2_score(b3, b5)
print(f'The RMSE of the linear regression b4 is {b6}')
print(f'The R2 score of the linear regression b4 is {b7}')
b8 = np.array([2015, 2016, 2017, 2018, 2019, 2020]).reshape(-1, 1)
b9 = b4.predict(b8)
b9 = np.round(b9, 4)
b10 = np.concatenate((b2.ravel(), b8.ravel()))
b11 = np.concatenate((b5.ravel(), b9.ravel()))
b12 = np.concatenate((b3.ravel(), b9.ravel()))
b13 = b1['Entity'].values
b14 = b13[:6]
b15 = np.concatenate((b13, b14))
b16 = b1['Code'].values
b17 = b16[:6]
b18 = np.concatenate((b16, b17))
b19 = {
    'Entity': b15,
    'Code': b18,
    'Year': b10,
    'crop(tonnes per hectare)': b12
}
b20 = pd.DataFrame(b19, columns=['Entity', 'Code', 'Year', 'crop(tonnes per hectare)'])
b20.to_csv('test.csv', b21 = False)
plt.scatter(b2, b3, b22 = 10, b23='c', label='Original Data')
plt.scatter(b8, b9, b22 = 10, b23='r', label='Predicted Data')
plt.plot(b10, b11, b23 = 'm', label='Regression Line')
plt.xlabel('Year')
plt.ylabel('Crop (tonnes per hectare)')
plt.legend()
plt.show()