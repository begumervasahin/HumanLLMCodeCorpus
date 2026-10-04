import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:/Users/pc/Desktop/kurs/HW1_DATA.csv")
x = data['x']
y = data['y']
plt.plot(x, y, '.')
plt.show()
xsum = np.sum(x)
ysum = np.sum(y)
yx = y.dot(x)
def mean(num):
    return num / 1000
den = mean(x.dot(x)) - mean(xsum)**2
a = mean(yx) - mean(xsum) * mean(ysum)
a = a / den
b = mean(ysum) * mean(x.dot(x)) - mean(yx) * mean(xsum)
b = b / den
yhat = a * x + b
plt.plot(x, y, '.')
plt.plot(x, yhat, '.')
plt.show()
sren = np.sum((y - yhat)**2)
stot = np.sum((y - mean(ysum))**2)
rsquare = 1 - sren / stot
def ypoly(p, x):
    yhat = 0
    l = len(p) - 1
    for i in range(len(p)):
        yhat = yhat + p[i] * x**(l - i)
    return yhat
def rsquare(yhat, y, stot):
    sren = np.sum((y - yhat)**2)
    return 1 - sren / stot
ones = np.ones(1000)
xhat = np.c_[x, ones]
w = np.linalg.solve(np.transpose(xhat).dot(xhat), np.transpose(xhat).dot(y))
print(w)
for degree in range(2, 8):
    xhat = np.c_[x**degree, xhat]
    w = np.linalg.solve(np.transpose(xhat).dot(xhat), np.transpose(xhat).dot(y))
    print(w)
y2 = ypoly(w, x)
a2 = rsquare(y2, y, stot)
plt.plot(x, y, '.', color='b')
plt.plot(x, y2, '.', color='g')
plt.show()