import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:/Users/pc/Desktop/kurs/HW1_DATA.csv")
x = data['x']
y = data['y']
plt.plot(x, y, '.')
plt.title("Original Data")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
def mean(num):
    return num / len(x)
xsum = np.sum(x)
ysum = np.sum(y)
yx = y.dot(x)
den = mean(x.dot(x)) - mean(xsum)**2
a = (mean(yx) - mean(xsum) * mean(ysum)) / den
b = (mean(ysum) * mean(x.dot(x)) - mean(yx) * mean(xsum)) / den
yhat = a * x + b
plt.plot(x, y, '.', label="Original Data")
plt.plot(x, yhat, '.', label="Linear Fit")
plt.title("Linear Regression Fit")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
sren = np.sum((y - yhat)**2)
stot = np.sum((y - mean(ysum))**2)
rsquare_linear = 1 - sren / stot
print(f"R-squared for linear fit: {rsquare_linear:.4f}")
def ypoly(p, x):
    yhat = 0
    l = len(p) - 1
    for i in range(len(p)):
        yhat += p[i] * x**(l - i)
    return yhat
ones = np.ones(len(x))
xhat = np.c_[x, ones]
def polynomial_regression(x, y, degree):
    xhat = np.vander(x, degree + 1)
    w = np.linalg.solve(np.transpose(xhat).dot(xhat), np.transpose(xhat).dot(y))
    return w
for degree in range(1, 8):
    w = polynomial_regression(x, y, degree)
    print(f"Coefficients for degree {degree}: {w}")
w = polynomial_regression(x, y, 7)
y2 = ypoly(w, x)
rsquare_poly = rsquare(y2, y, stot)
plt.plot(x, y, '.', color='b', label="Original Data")
plt.plot(x, y2, '.', color='g', label="Polynomial Fit (degree 7)")
plt.title("Polynomial Regression Fit")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
print(f"R-squared for polynomial fit (degree 7): {rsquare_poly:.4f}")