import quandl
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
b1 = quandl.get("WIKI/GOOGL")
b1 = b1.reset_index()
b2 = pd.DataFrame(b1)
b3 = b2['index']
b4 = np.array(b3)[:, np.newaxis]
b5 = b2['Adj. Open']
b6 = np.array(b5[:])
b7 = LinearRegression()
b7.fit(b4, b6)
b8 = LinearRegression()
b9 = PolynomialFeatures(degree=4)
b10 = b9.fit_transform(b4)
b8.fit(b10, b6)
b11 = pd.read_csv('data_to_be_predicted.csv')
b12 = np.array(b11['NO'])[:, np.newaxis]
b13 = b7.predict(b12)
b14 = b9.fit_transform(b12)
b15 = b8.predict(b14)
b16 = np.array([b15, b13]).T
b17 = pd.DataFrame(b16, index=b11['DATE_PREDICTED'], columns=['Polynomial Model', 'Linear Model'])
print("b18 = Google stock prices (Adj. Open) predicted by Polynomial model")
print("b19 = Google stock prices (Adj. Open) predicted by Linear model")
print(b17)
print("\nCONCLUSION: The Polynomial model predicts better and fits the graph better, as can be clearly seen in the graph.")
plt.scatter(b4, b6, b20 = 'black', s=1, label='Data')
plt.plot(b4, b7.predict(b4), b20 = 'blue', linewidth=2.0, label='Linear Model')
plt.plot(b4, b8.predict(b10), b20 = 'green', linewidth=2.0, label='Polynomial Model')
plt.xlabel("Days (Approx)")
plt.ylabel('Stock Price in USD')
plt.title('Implementation on Training Data')
plt.legend()
plt.autoscale(b21 = True)
plt.show()