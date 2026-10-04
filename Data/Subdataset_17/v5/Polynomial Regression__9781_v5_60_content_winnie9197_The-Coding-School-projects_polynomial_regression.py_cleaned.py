import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model, preprocessing
from sklearn.metrics import mean_squared_error, r2_score
import scipy.stats as stats
import operator
plt.style.use('seaborn-whitegrid')
def generate_data_set():
    np.random.seed(0)
    x = 2 - 3 * np.random.normal(0, 1, 20)
    y = x - 2 * (x ** 2) + 0.5 * (x ** 3) + np.random.normal(-3, 3, 20)
    x = x[:, np.newaxis]
    y = y[:, np.newaxis]
    return x, y
def plot_polynomial_regression(x, y, y_pred):
    sorted_zip = sorted(zip(x, y_pred), key=operator.itemgetter(0))
    x, y_pred = zip(*sorted_zip)
    plt.scatter(x, y, color='black')
    plt.plot(x, y_pred, linewidth=3)
    plt.title("Polynomial Regression")
    plt.xlabel("Observed Values")
    plt.ylabel("Predicted Values")
    plt.show()
def plot_qq(x):
    stats.probplot(x[:, 0], dist="norm", plot=plt)
    plt.title("QQ plot for Normality")
    plt.xlabel("Quantiles")
    plt.ylabel("Observed Values")
    plt.show()
def plot_residuals(residuals, y_pred):
    plt.scatter(y_pred, residuals, color='black')
    plt.axhline(0, color='red', linestyle='--')
    plt.title("Residuals Versus Predicted Values")
    plt.xlabel("Predicted Values")
    plt.ylabel("Residuals")
    plt.show()
def calculate_vif(exos, data):
    vif_dict, tolerance_dict = {}, {}
    for exo in exos:
        endos = [i for i in exos if i != exo]
        X, y = data[endos], data[exo]
        r_squared = linear_model.LinearRegression().fit(X, y).score(X, y)
        vif = 1 / (1 - r_squared)
        vif_dict[exo] = vif
        tolerance = 1 - r_squared
        tolerance_dict[exo] = tolerance
    df_vif = pd.DataFrame({'VIF': vif_dict, 'Tolerance': tolerance_dict})
    return df_vif
x_train, y_train = generate_data_set()
degree = 2
poly_features = preprocessing.PolynomialFeatures(degree=degree)
x_train_poly = poly_features.fit_transform(x_train)
poly_model = linear_model.LinearRegression()
poly_model.fit(x_train_poly, y_train)
y_poly_pred = poly_model.predict(x_train_poly)
plot_polynomial_regression(x_train, y_train, y_poly_pred)
plot_qq(x_train)
residuals_train = y_poly_pred - y_train
plot_residuals(residuals_train, y_poly_pred)
rmse_train = np.sqrt(mean_squared_error(y_train, y_poly_pred))
r2_train = r2_score(y_train, y_poly_pred)
print("The model performance for the training set")
print("-------------------------------------------")
print(f"RMSE for training: {rmse_train:.5f}")
print(f"R2 for training: {r2_train:.5f}")