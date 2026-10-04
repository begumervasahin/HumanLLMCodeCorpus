import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
data = pd.read_csv("maize.csv", usecols=['Year', 'Crop', 'Entity', 'Code'], nrows=54)
years = data['Year'].values.reshape(-1, 1)
crops = data['Crop'].values
model = LinearRegression()
model.fit(years, crops)
predicted_crops = model.predict(years)
rmse = mean_squared_error(crops, predicted_crops)
r2 = r2_score(crops, predicted_crops)
print(f'The RMSE of the linear regression model is {rmse}')
print(f'The R2 score of the linear regression model is {r2}')
future_years = np.array([2015, 2016, 2017, 2018, 2019, 2020]).reshape(-1, 1)
future_predictions = model.predict(future_years)
future_predictions = np.round(future_predictions, 4)
all_years = np.concatenate((years.ravel(), future_years.ravel()))
all_predictions = np.concatenate((predicted_crops, future_predictions))
all_actual_crops = np.concatenate((crops, future_predictions))
entities = data['Entity'].values
extended_entities = np.concatenate((entities, entities[:6]))
codes = data['Code'].values
extended_codes = np.concatenate((codes, codes[:6]))
final_data = {
    'Entity': extended_entities,
    'Code': extended_codes,
    'Year': all_years,
    'crop(tonnes per hectare)': all_actual_crops
}
df_final = DataFrame(final_data, columns=['Entity', 'Code', 'Year', 'crop(tonnes per hectare)'])
df_final.to_csv('/home/leathea/Downloads/Machine-Learning/PolynomialRegression/test.csv', index=False)
plt.scatter(years, crops, s=10, color='c', label='Actual Data')
plt.scatter(future_years, future_predictions, s=10, color='r', label='Predicted Future Data')
plt.plot(all_years, all_predictions, color='m', label='Regression Line')
plt.xlabel('Year')
plt.ylabel('Crop (tonnes per hectare)')
plt.legend()
plt.show()