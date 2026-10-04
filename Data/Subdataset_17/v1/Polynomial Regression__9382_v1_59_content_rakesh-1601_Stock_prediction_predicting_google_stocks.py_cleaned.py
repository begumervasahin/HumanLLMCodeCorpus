import quandl
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
g = quandl.get("WIKI/GOOGL")
g = g.reset_index()
df = pd.DataFrame(g)
index_ = df.index
days_ = np.array(index_)[:, np.newaxis]
price_open = df['Adj. Open']
price_train = np.array(price_open)
regres_simple = linear_model.LinearRegression()
regres_simple.fit(days_, price_train)
reg_with_poly = linear_model.LinearRegression()
poly = PolynomialFeatures(4)
x_transform = poly.fit_transform(days_)
reg_with_poly.fit(x_transform, price_train)
tes = pd.read_csv('data_to_be_predicted.csv')
test_date = np.array(tes['NO'])[:, np.newaxis]
dates_predict = np.array(tes['DATE_PREDICTED'])
pred_by_simple_regression = regres_simple.predict(test_date)
xtest_trans = poly.fit_transform(test_date)
pred_by_poly_regression = reg_with_poly.predict(xtest_trans)
dataframe_data = np.array([pred_by_poly_regression, pred_by_simple_regression])
index = tes['DATE_PREDICTED']
columns = ['A', 'B']
pred_dataframe = pd.DataFrame(dataframe_data.T, index=index, columns=columns)
print("A = Google stock prices (Adj. Open) predicted by Polynomial model")
print("B = Google stock prices (Adj. Open) predicted by Linear model")
print(pred_dataframe)
print(" ")
print("CONCLUSION: 'POLYNOMIAL model predicts better as well as fits the graph better, as it can be clearly seen in the graph'")
plt.scatter(days_, price_train, color='black', s=1, label='Data')
plt.plot(days_, regres_simple.predict(days_), color='blue', linewidth=2.0, label='Linear model')
plt.plot(days_, reg_with_poly.predict(x_transform), color='green', linewidth=2.0, label='Polynomial model')
plt.xlabel("Days (Approx)")
plt.ylabel('Stock price in USD')
plt.title('Implementation on training data')
plt.legend()
plt.autoscale(tight=True)
plt.show()