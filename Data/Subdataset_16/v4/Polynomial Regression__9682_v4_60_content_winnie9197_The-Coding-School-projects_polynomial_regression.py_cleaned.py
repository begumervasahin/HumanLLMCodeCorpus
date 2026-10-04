import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model, preprocessing
from sklearn.metrics import mean_squared_error, r2_score
import scipy.stats as stats
import operator
plt.style.use('seaborn-whitegrid')
def fonk1():
    np.random.seed(0)
    b1 = 2 - 3 * np.random.normal(0, 1, 20)
    b2 = b1 - 2 * (b1 ** 2) + 0.5 * (b1 ** 3) + np.random.normal(-3, 3, 20)
    b1 = b1[:, np.newaxis]
    b2 = b2[:, np.newaxis]
    return b1, b2
x_train, b3 = fonk1()
a1 = 2
b4 = preprocessing.PolynomialFeatures(a1=a1)
b5 = b4.fit_transform(x_train)
b6 = linear_model.LinearRegression()
b6.fit(b5, b3)
b7 = b6.predict(b5)
def fonk2(b1, b2, b9):
    b8 = sorted(zip(b1, b9), key=operator.itemgetter(0))
    b1, b9 = zip(*b8)
    plt.scatter(b1, b2, b10 = 'black')
    plt.plot(b1, b9, b11 = 3)
    plt.title("Polynomial Regression")
    plt.xlabel("Observed Values")
    plt.ylabel("Predicted Values")
    plt.show()
fonk2(x_train, b3, b7)
def fonk3(b1):
    stats.probplot(b1[:, 0], b12 = "norm", plot=plt)
    plt.title("QQ plot for Normality")
    plt.xlabel("Quantiles")
    plt.ylabel("Observed Values")
    plt.show()
fonk3(x_train)
b13 = b7 - b3
def fonk4(residuals, b2):
    plt.scatter(b2, residuals, b10 = 'black')
    plt.axhline(0, b10 = 'red', linestyle='--')
    plt.title("Residuals Versus Predicted Values")
    plt.xlabel("Predicted Values")
    plt.ylabel("Residuals")
    plt.show()
fonk4(b13, b7)
def fonk5(exos, data):
    vif_dict, b14 = {}, {}
    for exo in exos:
        b15 = [i for i in exos if i != exo]
        X, b2 = data[b15], data[exo]
        b16 = linear_model.LinearRegression().fit(X, b2).score(X, b2)
        b17 = 1 / (1 - b16)
        vif_dict[exo] = b17
        b18 = 1 - b16
        b14[exo] = b18
    b19 = pd.DataFrame({'VIF': vif_dict, 'Tolerance': b14})
    return b19
b20 = np.sqrt(mean_squared_error(b3, b7))
b21 = r2_score(b3, b7)
print("The model performance for the training set")
print("-------------------------------------------")
print(f"RMSE for training: {b20:.5f}")
print(f"R2 for training: {b21:.5f}")