import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv('Ass1.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 3].values
b4 = LinearRegression()
b4.fit(b2, b3)
b5 = PolynomialFeatures(degree=4)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
b7.fit(b6, b3)
def fonk1(model, b2, b3, title, xlabel, ylabel, b8 = None, smoother=False):
    plt.scatter(b2, b3, b9 = 'red')
    if smoother:
        b10 = np.arange(min(b2), max(b2), 0.1).reshape(-1, 1)
        plt.plot(b10, model.predict(b8(b10)), b9 = 'blue')
    else:
        plt.plot(b2, model.predict(b8(b2)), b9 = 'blue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
fonk1(b4, b2, b3, 'Truth or Bluff (Linear Regression)', 'Position Level', 'Salary', b8 = lambda x: x)
fonk1(b7, b2, b3, 'Truth or Bluff (Polynomial Regression)', 'Position Level', 'Salary', b8 = b5.fit_transform)
fonk1(b7, b2, b3, 'Truth or Bluff (Polynomial Regression - Smooth Curve)', 'Position Level', 'Salary', b8 = b5.fit_transform, smoother=True)
a1 = 6.5
b11 = b4.predict(np.array([[a1]]))[0]
b12 = b7.predict(b5.fit_transform(np.array([[a1]])))[0]
print(f"Linear Regression Prediction for {a1}: {b11}")
print(f"Polynomial Regression Prediction for {a1}: {b12}")