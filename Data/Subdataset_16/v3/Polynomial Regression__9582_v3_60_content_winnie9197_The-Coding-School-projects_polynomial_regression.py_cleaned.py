import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model, preprocessing
from sklearn.metrics import mean_squared_error, r2_score
import operator
import scipy.stats as stats
plt.style.use('seaborn-whitegrid')
def fonk1(b1 = 0, num_samples=20):
    np.random.b1(b1)
    b2 = 2 - 3 * np.random.normal(0, 1, num_samples)
    b3 = b2 - 2 * (b2 ** 2) + 0.5 * (b2 ** 3) + np.random.normal(-3, 3, num_samples)
    b2 = b2[:, np.newaxis]
    b3 = b3[:, np.newaxis]
    return b2, b3
x_train, b4 = fonk1()
a1 = 2
b5 = preprocessing.PolynomialFeatures(a1=a1)
b6 = b5.fit_transform(x_train)
b7 = linear_model.LinearRegression()
b7.fit(b6, b4)
b8 = b7.predict(b6)
def fonk2(b2, b3, y_pred):
    b9 = sorted(zip(b2, y_pred), key=operator.itemgetter(0))
    x_sorted, b10 = zip(*b9)
    plt.scatter(b2, b3, b11 = 'black')
    plt.plot(x_sorted, b10, b12 = 3, b11='blue')
    plt.title("Polynomial Regression")
    plt.xlabel("Observed Values")
    plt.ylabel("Predicted Values")
    plt.show()
fonk2(x_train, b4, b8)
def fonk3(b2):
    stats.probplot(b2[:, 0], b13 = "norm", plot=plt)
    plt.title("Q-Q Plot for Normality")
    plt.xlabel("Quantiles")
    plt.ylabel("Observed Values")
    plt.show()
fonk3(x_train)
b14 = b8 - b4
def fonk4(residuals, y_pred):
    plt.scatter(y_pred, residuals, b11 = 'black')
    plt.axhline(0, b11 = 'red', linestyle='--')
    plt.title("Residuals Versus Predicted Values")
    plt.xlabel("Predicted Values")
    plt.ylabel("Residuals")
    plt.show()
fonk4(b14, b8)
def fonk5(exogenous_vars, data):
    vif_dict, b15 = {}, {}
    for exo in exogenous_vars:
        b16 = [i for i in exogenous_vars if i != exo]
        X, b3 = data[b16], data[exo]
        b17 = linear_model.LinearRegression().fit(X, b3).score(X, b3)
        b18 = 1 / (1 - b17)
        b19 = 1 - b17
        vif_dict[exo] = b18
        b15[exo] = b19
    b20 = pd.DataFrame({'VIF': vif_dict, 'Tolerance': b15})
    return b20
b21 = np.sqrt(mean_squared_error(b4, b8))
b22 = r2_score(b4, b8)
print("The model performance for the training set")
print("-------------------------------------------")
print(f"RMSE for training: {b21:.5f}")
print(f"R2 for training: {b22:.5f}")