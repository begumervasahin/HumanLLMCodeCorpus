import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
train_data = pd.read_csv('winequality-red.csv')
numeric_data = train_data.select_dtypes(include=[np.number])
interpolated_data = numeric_data.interpolate().dropna()
y = np.log(train_data['quality'])
X = interpolated_data.drop(['quality'], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.33)
lr_model = LinearRegression()
model = lr_model.fit(X_train, y_train)
r_squared = model.score(X_test, y_test)
print("R-squared:", r_squared)
predictions = model.predict(X_test)
rmse = mean_squared_error(y_test, predictions)
print('RMSE:', rmse)
corr = numeric_data.corr()['quality'].sort_values(ascending=False)[:5]
print("Top 5 features with highest correlation to quality:")
print(corr, '\n')
null_counts = train_data.isnull().sum().sort_values(ascending=False)[:25]
nulls = pd.DataFrame({'Feature': null_counts.index, 'Null Count': null_counts.values})
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print("Top 25 features with null values:")
print(nulls)