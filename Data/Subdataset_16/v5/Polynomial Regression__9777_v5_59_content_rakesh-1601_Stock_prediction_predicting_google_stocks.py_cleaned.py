import quandl
import pandas as pd
import numpy as np
from sklearn.b5 import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
b1 = quandl.get("WIKI/GOOGL")
b1 = b1.reset_index()
b2 = pd.DataFrame(b1)
b3 = np.array(b2.index)[:, np.newaxis]
b4 = b2['Adj. Open'].values
b5 = LinearRegression()
b5.fit(b3, b4)
b6 = PolynomialFeatures(degree=4)
b7 = b6.fit_transform(b3)
b8 = LinearRegression()
b8.fit(b7, b4)
b9 = pd.read_csv('data_to_be_predicted.csv')
b10 = np.array(b9['NO'])[:, np.newaxis]
b11 = b5.predict(b10)
b12 = b6.transform(b10)
b13 = b8.predict(b12)
b14 = np.vstack((b13, b11)).T
b15 = pd.DataFrame(b14, index=b9['DATE_PREDICTED'], columns=['Polynomial Model', 'Linear Model'])
print("b16 = Google stock prices (Adj. Open) predicted by Polynomial model")
print("b17 = Google stock prices (Adj. Open) predicted by Linear model")
print(b15)
print("\nCONCLUSION: The Polynomial model predicts better and fits the graph better, as can be clearly seen in the graph.")
plt.scatter(b3, b4, b18 = 'black', s=1, label='Data')
plt.plot(b3, b5.predict(b3), b18 = 'blue', linewidth=2, label='Linear Model')
plt.plot(b3, b8.predict(b7), b18 = 'green', linewidth=2, label='Polynomial Model')
plt.xlabel("Days (Approx)")
plt.ylabel('Stock Price in USD')
plt.title('Implementation on Training Data')
plt.legend()
plt.autoscale(b19 = True)
plt.show()