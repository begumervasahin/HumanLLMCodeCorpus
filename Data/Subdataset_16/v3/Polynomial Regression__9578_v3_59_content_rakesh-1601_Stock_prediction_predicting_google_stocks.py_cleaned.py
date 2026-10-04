import quandl
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
b1 = quandl.get("WIKI/GOOGL").reset_index()
b2 = np.arange(len(b1)).reshape(-1, 1)
b3 = b1['Adj. Open'].values
b4 = linear_model.LinearRegression()
b4.fit(b2, b3)
a1 = 4
b5 = PolynomialFeatures(degree=a1)
b6 = b5.fit_transform(b2)
b7 = linear_model.LinearRegression()
b7.fit(b6, b3)
b8 = pd.read_csv('data_to_be_predicted.csv')
b9 = b8['NO'].values.reshape(-1, 1)
b10 = b8['DATE_PREDICTED'].values
b11 = b4.predict(b9)
b12 = b5.transform(b9)
b13 = b7.predict(b12)
b14 = pd.DataFrame({
    'Date': b10,
    'Polynomial Model': b13,
    'Linear Model': b11
})
print("b15 = Google stock prices (Adj. Open) predicted by Polynomial model")
print("b16 = Google stock prices (Adj. Open) predicted by Linear model")
print(b14)
print("\nCONCLUSION: 'POLYNOMIAL model predicts better as well as fits the graph better, as it can be clearly seen in the graph'")
plt.scatter(b2, b3, b17 = 'black', s=1, label='Data')
plt.plot(b2, b4.predict(b2), b17 = 'blue', linewidth=2.0, label='Linear model')
plt.plot(b2, b7.predict(b6), b17 = 'green', linewidth=2.0, label='Polynomial model')
plt.xlabel("Days (Approx)")
plt.ylabel('Stock price in USD')
plt.title('Implementation on training data')
plt.legend()
plt.autoscale(b18 = True)
plt.show()