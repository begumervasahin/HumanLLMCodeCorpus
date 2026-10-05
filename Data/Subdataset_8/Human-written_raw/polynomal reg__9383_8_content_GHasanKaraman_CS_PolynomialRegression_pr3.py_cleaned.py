import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
datas=pd.read_csv("datasets/dollar.csv")
X=np.array(datas["Day"]).reshape(-1,1)
Y=np.array(datas["Price"]).reshape(-1,1)
plt.plot(X,Y,"ob")
polinom = PolynomialFeatures(degree = 2)
X_ = polinom.fit_transform(X,Y)
lr = LinearRegression()
lr.fit(X_,Y)
plt.plot(X,lr.predict(X_),color = "red")