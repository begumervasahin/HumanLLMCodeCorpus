import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv("datasets/dollar.csv")
b2 = np.array(b1["Day"]).reshape(-1,1)
b3 = np.array(b1["Price"]).reshape(-1,1)
plt.plot(b2,b3,"ob")
b4 = PolynomialFeatures(degree = 2)
b5 = b4.fit_transform(b2,b3)
b6 = LinearRegression()
b6.fit(b5,b3)
plt.plot(b2,b6.predict(b5),b7 = "red")