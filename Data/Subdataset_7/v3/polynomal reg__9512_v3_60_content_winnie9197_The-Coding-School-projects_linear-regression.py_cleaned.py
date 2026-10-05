import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
import scipy.stats as stats
plt.style.use('seaborn-whitegrid')
X, b1 = make_regression(n_samples=100, n_features=1, noise=10)
b2 = LinearRegression()
b2.fit(X, b1)
b3 = b2.predict(X)
def fonk1(X, b1, b3):
    plt.scatter(X, b1, b4 = 'black')
    plt.plot(X, b3, b5 = 3)
    plt.title("Linear Regression")
    plt.xlabel("Observed Values")
    plt.ylabel("Predicted Values")
    plt.show()
fonk1(X, b1, b3)
b6 = b3 - b1
def fonk2(b6, X):
    plt.scatter(X, b6, b4 = 'black')
    plt.axhline(0)
    plt.title("Residuals Versus Observed Values")
    plt.xlabel("Observed Values")
    plt.ylabel("Residuals")
    plt.show()
fonk2(b6, X)
def fonk3(X):
    stats.probplot(X[:, 0], b7 = "norm", plot=plt)
    plt.title("QQ plot for Normality")
    plt.xlabel("Quantiles")
    plt.ylabel("Observed Values")
    plt.show()
fonk3(X)