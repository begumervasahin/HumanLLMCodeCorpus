import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_excel('placements.xlsx')
X = dataset.iloc[:, 2:3].values
y = dataset.iloc[:, 3].values
lin_reg = LinearRegression()
lin_reg.fit(X, y)
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg.predict(X), color='blue')
plt.title('PLACEMENT RECORD (Linear Regression)')
plt.xlabel('NO. of Students placed')
plt.ylabel('YEAR')
plt.show()
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color='blue')
plt.title('Truth or Bluff (PLACEMENTS RECORD)')
plt.xlabel('NO. of Students placed')
plt.ylabel('YEAR')
plt.show()
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color='red')
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color='blue')
plt.title('PLACEMENT RECORD (Polynomial Regression)')
plt.xlabel('NO. of Students placed')
plt.ylabel('YEAR')
plt.show()