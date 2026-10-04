import quandl
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
g = quandl.get("WIKI/GOOGL")
g = g.reset_index()
df = pd.DataFrame(g)
days = np.arange(len(df)).reshape(-1, 1)
price_open = df['Adj. Open'].values
linear_regressor = linear_model.LinearRegression()
linear_regressor.fit(days, price_open)
poly_features = PolynomialFeatures(degree=4)
days_poly = poly_features.fit_transform(days)
poly_regressor = linear_model.LinearRegression()
poly_regressor.fit(days_poly, price_open)
test_data = pd.read_csv('data_to_be_predicted.csv')
test_days = test_data['NO'].values.reshape(-1, 1)
dates_predict = test_data['DATE_PREDICTED'].values
linear_predictions = linear_regressor.predict(test_days)
test_days_poly = poly_features.transform(test_days)
poly_predictions = poly_regressor.predict(test_days_poly)
predictions = pd.DataFrame({
    'Date': dates_predict,
    'Polynomial Model': poly_predictions,
    'Linear Model': linear_predictions
})
print("A = Google stock prices (Adj. Open) predicted by Polynomial model")
print("B = Google stock prices (Adj. Open) predicted by Linear model")
print(predictions)
print("\nCONCLUSION: 'POLYNOMIAL model predicts better as well as fits the graph better, as it can be clearly seen in the graph'")
plt.scatter(days, price_open, color='black', s=1, label='Data')
plt.plot(days, linear_regressor.predict(days), color='blue', linewidth=2.0, label='Linear model')
plt.plot(days, poly_regressor.predict(days_poly), color='green', linewidth=2.0, label='Polynomial model')
plt.xlabel("Days (Approx)")
plt.ylabel('Stock price in USD')
plt.title('Implementation on training data')
plt.legend()
plt.autoscale(tight=True)
plt.show()