
from sklearn import linear_model
from sklearn.datasets.samples_generator import make_regression
import matplotlib.pyplot as plt
import scipy.stats as stats
plt.style.use('seaborn-whitegrid')
x2, y2 = make_regression(n_samples=100, n_features=1, noise=10)
regressor = linear_model.LinearRegression()
regressor.fit(x2, y2)
predicted_values = regressor.predict(x2)
def plot_linear_regression(x, y, predicted_values):
    plt.scatter(x, y, color='black')
    plt.plot(x, predicted_values, linewidth=3)
    plt.title("Linear Regression")
    plt.xlabel("Observed Values")
    plt.ylabel("Predicted Values")
    plt.show()
plot_linear_regression(x2, y2, predicted_values)
residuals = predicted_values - y2
def plot_residuals_vs_observed(residuals, x):
    plt.scatter(x, residuals, color='black')
    plt.axhline(0)
    plt.title("Residuals Versus Observed Values")
    plt.xlabel("Observed Values")
    plt.ylabel("Residuals")
    plt.show()
plot_residuals_vs_observed(residuals, x2)
def plot_qq_plot(x):
    stats.probplot(x[:, 0], dist="norm", plot=plt)
    plt.title("QQ plot for Normality")
    plt.xlabel("Quantiles")
    plt.ylabel("Observed Values")
    plt.show()
plot_qq_plot(x2)