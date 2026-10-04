import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
data = pd.read_csv("maize.csv", usecols=['Year', 'Crop', 'Entity', 'Code'], nrows=54)
x = data['Year'].values.reshape(-1, 1)
y = data['Crop'].values.reshape(-1, 1)
model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)
rmse = mean_squared_error(y, y_pred, squared=False)
r2 = r2_score(y, y_pred)
print(f'The RMSE of the linear regression model is {rmse}')
print(f'The R2 score of the linear regression model is {r2}')
future_years = np.array([2015, 2016, 2017, 2018, 2019, 2020]).reshape(-1, 1)
future_predictions = model.predict(future_years)
future_predictions = np.round(future_predictions, 4)
x_combined = np.concatenate((x.ravel(), future_years.ravel()))
y_combined = np.concatenate((y_pred.ravel(), future_predictions.ravel()))
y_combined_print = np.concatenate((y.ravel(), future_predictions.ravel()))
entities = data['Entity'].values
extra_entities = entities[:6]
entities_combined = np.concatenate((entities, extra_entities))
codes = data['Code'].values
extra_codes = codes[:6]
codes_combined = np.concatenate((codes, extra_codes))
output_data = {
    'Entity': entities_combined,
    'Code': codes_combined,
    'Year': x_combined,
    'crop(tonnes per hectare)': y_combined_print
}
df = pd.DataFrame(output_data, columns=['Entity', 'Code', 'Year', 'crop(tonnes per hectare)'])
df.to_csv('test.csv', index=False)
plt.scatter(x, y, s=10, color='c', label='Original Data')
plt.scatter(future_years, future_predictions, s=10, color='r', label='Predicted Data')
plt.plot(x_combined, y_combined, color='m', label='Regression Line')
plt.xlabel('Year')
plt.ylabel('Crop (tonnes per hectare)')
plt.legend()
plt.show()