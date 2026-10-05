from sklearn import linear_model
from sklearn.datasets.samples_generator import make_regression
import matplotlib.pyplot as plt
import scipy.stats as stats
plt.style.use('seaborn-whitegrid')
x2, y2 = make_regression(n_samples=100, n_features=1, noise=10)
regr = linear_model.LinearRegression()
regr.fit(x2, y2)
y_pred = regr.predict(x2)
def plot_lin_reg(x, y, y_pred):
    plt.scatter(x, y, color='black')
    plt.plot(x, y_pred, linewidth=3)
    plt.title("Linear Regression")
    plt.xlabel("Observed Values")
    plt.ylabel("Predicted Values")
    plt.show()
plot_lin_reg(x2, y2, y_pred)
residuals = y_pred - y2
def plot_residuals(residuals, x):
    plt.scatter(x, residuals, color='black')
    plt.axhline(0)
    plt.title("Residuals Versus Observed Values")
    plt.xlabel("Observed Values")
    plt.ylabel("Residuals")
    plt.show()
plot_residuals(residuals, x2)
def plot_qq(x):
    stats.probplot(x[:, 0], dist="norm", plot=plt)
    plt.title("QQ plot for Normality")
    plt.xlabel("Quantiles")
    plt.ylabel("Observed Values")
    plt.show()
plot_qq(x2)