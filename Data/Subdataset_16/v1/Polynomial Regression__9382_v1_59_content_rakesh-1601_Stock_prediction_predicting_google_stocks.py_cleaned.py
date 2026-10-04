import quandl
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
b1 = quandl.get("WIKI/GOOGL")
b1 = b1.reset_index()
b2 = pd.DataFrame(b1)
b3 = b2.b18
b4 = np.array(b3)[:, np.newaxis]
b5 = b2['Adj. Open']
b6 = np.array(b5)
b7 = linear_model.LinearRegression()
b7.fit(b4, b6)
b8 = linear_model.LinearRegression()
b9 = PolynomialFeatures(4)
b10 = b9.fit_transform(b4)
b8.fit(b10, b6)
b11 = pd.read_csv('data_to_be_predicted.csv')
b12 = np.array(b11['NO'])[:, np.newaxis]
b13 = np.array(b11['DATE_PREDICTED'])
b14 = b7.predict(b12)
b15 = b9.fit_transform(b12)
b16 = b8.predict(b15)
b17 = np.array([b16, b14])
b18 = b11['DATE_PREDICTED']
b19 = ['b21', 'b22']
b20 = pd.DataFrame(b17.T, b18=b18, b19=b19)
print("b21 = Google stock prices (Adj. Open) predicted by Polynomial model")
print("b22 = Google stock prices (Adj. Open) predicted by Linear model")
print(b20)
print(" ")
print("CONCLUSION: 'POLYNOMIAL model predicts better as well as fits the graph better, as it can be clearly seen in the graph'")
plt.scatter(b4, b6, b23 = 'black', s=1, label='Data')
plt.plot(b4, b7.predict(b4), b23 = 'blue', linewidth=2.0, label='Linear model')
plt.plot(b4, b8.predict(b10), b23 = 'green', linewidth=2.0, label='Polynomial model')
plt.xlabel("Days (Approx)")
plt.ylabel('Stock price in USD')
plt.title('Implementation on training data')
plt.legend()
plt.autoscale(b24 = True)
plt.show()