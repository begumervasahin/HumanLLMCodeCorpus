import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
import scipy.stats as stats
plt.style.use('seaborn-whitegrid')
X, y = make_regression(n_samples=100, n_features=1, noise=10)
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
def plot_linear_regression(X, y, y_pred):
    plt.scatter(X, y, color='black')
    plt.plot(X, y_pred, linewidth=3)
    plt.title("Linear Regression")
    plt.xlabel("Observed Values")
    plt.ylabel("Predicted Values")
    plt.show()
plot_linear_regression(X, y, y_pred)
residuals = y_pred - y
def plot_residuals_vs_observed(residuals, X):
    plt.scatter(X, residuals, color='black')
    plt.axhline(0)
    plt.title("Residuals Versus Observed Values")
    plt.xlabel("Observed Values")
    plt.ylabel("Residuals")
    plt.show()
plot_residuals_vs_observed(residuals, X)
def plot_qq_plot(X):
    stats.probplot(X[:, 0], dist="norm", plot=plt)
    plt.title("QQ plot for Normality")
    plt.xlabel("Quantiles")
    plt.ylabel("Observed Values")
    plt.show()
plot_qq_plot(X)