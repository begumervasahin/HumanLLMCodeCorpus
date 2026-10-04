import quandl
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
b1 = quandl.get("WIKI/GOOGL")
b1 = b1.reset_index()
b2 = pd.DataFrame(b1)
b3 = np.arange(len(b2)).reshape(-1, 1)
b4 = b2['Adj. Open'].values
b5 = linear_model.LinearRegression()
b5.fit(b3, b4)
b6 = PolynomialFeatures(degree=4)
b7 = b6.fit_transform(b3)
b8 = linear_model.LinearRegression()
b8.fit(b7, b4)
b9 = pd.read_csv('data_to_be_predicted.csv')
b10 = b9['NO'].values.reshape(-1, 1)
b11 = b9['DATE_PREDICTED'].values
b12 = b5.predict(b10)
b13 = b6.transform(b10)
b14 = b8.predict(b13)
b15 = pd.DataFrame({
    'Date': b11,
    'Polynomial Model': b14,
    'Linear Model': b12
})
print("b16 = Google stock prices (Adj. Open) predicted by Polynomial model")
print("b17 = Google stock prices (Adj. Open) predicted by Linear model")
print(b15)
print("\nCONCLUSION: 'POLYNOMIAL model predicts better as well as fits the graph better, as it can be clearly seen in the graph'")
plt.scatter(b3, b4, b18 = 'black', s=1, label='Data')
plt.plot(b3, b5.predict(b3), b18 = 'blue', linewidth=2.0, label='Linear model')
plt.plot(b3, b8.predict(b7), b18 = 'green', linewidth=2.0, label='Polynomial model')
plt.xlabel("Days (Approx)")
plt.ylabel('Stock price in USD')
plt.title('Implementation on training data')
plt.legend()
plt.autoscale(b19 = True)
plt.show()