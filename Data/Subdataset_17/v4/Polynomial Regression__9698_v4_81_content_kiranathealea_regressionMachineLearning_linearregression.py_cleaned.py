import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
data = pd.read_csv("maize.csv", usecols=['Year', 'Crop', 'Entity', 'Code'], nrows=54)
x = data['Year'].values.reshape(-1, 1)
y = data['Crop'].values
model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)
rmse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print(f'The RMSE of the linear regression model is {rmse}')
print(f'The R2 score of the linear regression model is {r2}')
future_years = np.array([2015, 2016, 2017, 2018, 2019, 2020]).reshape(-1, 1)
y_future_pred = model.predict(future_years)
y_future_pred = np.round(y_future_pred, 4)
x_combined = np.concatenate((x.ravel(), future_years.ravel()))
y_combined = np.concatenate((y_pred, y_future_pred))
y_combined_actual = np.concatenate((y, y_future_pred))
entity = data['Entity'].values
entity_extended = np.concatenate((entity, entity[:6]))
code = data['Code'].values
code_extended = np.concatenate((code, code[:6]))
final_data = {
    'Entity': entity_extended,
    'Code': code_extended,
    'Year': x_combined,
    'crop(tonnes per hectare)': y_combined_actual
}
df_final = DataFrame(final_data, columns=['Entity', 'Code', 'Year', 'crop(tonnes per hectare)'])
df_final.to_csv('/home/leathea/Downloads/Machine-Learning/PolynomialRegression/test.csv', index=False)
plt.scatter(x, y, s=10, color='c', label='Actual Data')
plt.scatter(future_years, y_future_pred, s=10, color='r', label='Predicted Future Data')
plt.plot(x_combined, y_combined, color='m', label='Regression Line')
plt.xlabel('Year')
plt.ylabel('Crop (tonnes per hectare)')
plt.legend()
plt.show()