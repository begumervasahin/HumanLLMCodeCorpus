import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
data = pd.read_csv("maize.csv", usecols=['Year', 'Crop', 'Entity', 'Code'], nrows=54)
x = data['Year'].values.reshape(-1, 1)
y = data['Crop'].values.reshape(-1, 1)
model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)
rmse_ = mean_squared_error(y, y_pred, squared=False)
r2_ = r2_score(y, y_pred)
print(f'The RMSE of the linear regression model is {rmse_}')
print(f'The R2 score of the linear regression model is {r2_}')
years = np.array([2015, 2016, 2017, 2018, 2019, 2020]).reshape(-1, 1)
y_next = model.predict(years)
y_next = np.round(y_next, 4)
x_final = np.concatenate((x.ravel(), years.ravel()))
y_final = np.concatenate((y_pred.ravel(), y_next.ravel()))
y_final_print = np.concatenate((y.ravel(), y_next.ravel()))
wilayah = data['Entity'].values
wil_tambahan = wilayah[:6]
wilayah = np.concatenate((wilayah, wil_tambahan))
kode = data['Code'].values
kode_tambahan = kode[:6]
kode = np.concatenate((kode, kode_tambahan))
recsv = {
    'Entity': wilayah,
    'Code': kode,
    'Year': x_final,
    'crop(tonnes per hectare)': y_final_print
}
df = DataFrame(recsv, columns=['Entity', 'Code', 'Year', 'crop(tonnes per hectare)'])
export_csv = df.to_csv('test.csv', index=None, header=True)
plt.scatter(x, y, s=10, color='c', label='Original Data')
plt.scatter(years, y_next, s=10, color='r', label='Predicted Data')
plt.plot(x_final, y_final, color='m', label='Regression Line')
plt.xlabel('Year')
plt.ylabel('Crop (tonnes per hectare)')
plt.legend()
plt.show()