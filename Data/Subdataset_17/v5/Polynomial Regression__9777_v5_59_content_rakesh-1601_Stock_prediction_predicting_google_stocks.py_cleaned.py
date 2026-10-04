import quandl
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
google_stock_data = quandl.get("WIKI/GOOGL")
google_stock_data = google_stock_data.reset_index()
df = pd.DataFrame(google_stock_data)
days = np.array(df.index)[:, np.newaxis]
price_open = df['Adj. Open'].values
linear_model = LinearRegression()
linear_model.fit(days, price_open)
poly_features = PolynomialFeatures(degree=4)
days_poly = poly_features.fit_transform(days)
poly_model = LinearRegression()
poly_model.fit(days_poly, price_open)
test_data = pd.read_csv('data_to_be_predicted.csv')
test_days = np.array(test_data['NO'])[:, np.newaxis]
pred_linear = linear_model.predict(test_days)
test_days_poly = poly_features.transform(test_days)
pred_poly = poly_model.predict(test_days_poly)
predictions = np.vstack((pred_poly, pred_linear)).T
pred_df = pd.DataFrame(predictions, index=test_data['DATE_PREDICTED'], columns=['Polynomial Model', 'Linear Model'])
print("A = Google stock prices (Adj. Open) predicted by Polynomial model")
print("B = Google stock prices (Adj. Open) predicted by Linear model")
print(pred_df)
print("\nCONCLUSION: The Polynomial model predicts better and fits the graph better, as can be clearly seen in the graph.")
plt.scatter(days, price_open, color='black', s=1, label='Data')
plt.plot(days, linear_model.predict(days), color='blue', linewidth=2, label='Linear Model')
plt.plot(days, poly_model.predict(days_poly), color='green', linewidth=2, label='Polynomial Model')
plt.xlabel("Days (Approx)")
plt.ylabel('Stock Price in USD')
plt.title('Implementation on Training Data')
plt.legend()
plt.autoscale(tight=True)
plt.show()