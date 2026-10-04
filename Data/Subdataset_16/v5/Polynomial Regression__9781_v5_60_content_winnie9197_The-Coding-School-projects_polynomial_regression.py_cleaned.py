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
def fonk2(b1, b2, b4):
    b3 = sorted(zip(b1, b4), key=operator.itemgetter(0))
    b1, b4 = zip(*b3)
    plt.scatter(b1, b2, b5 = 'black')
    plt.plot(b1, b4, b6 = 3)
    plt.title("Polynomial Regression")
    plt.xlabel("Observed Values")
    plt.ylabel("Predicted Values")
    plt.show()
def fonk3(b1):
    stats.probplot(b1[:, 0], b7 = "norm", plot=plt)
    plt.title("QQ plot for Normality")
    plt.xlabel("Quantiles")
    plt.ylabel("Observed Values")
    plt.show()
def fonk4(residuals, b4):
    plt.scatter(b4, residuals, b5 = 'black')
    plt.axhline(0, b5 = 'red', linestyle='--')
    plt.title("Residuals Versus Predicted Values")
    plt.xlabel("Predicted Values")
    plt.ylabel("Residuals")
    plt.show()
def fonk5(exos, data):
    vif_dict, b8 = {}, {}
    for exo in exos:
        b9 = [i for i in exos if i != exo]
        X, b2 = data[b9], data[exo]
        b10 = linear_model.LinearRegression().fit(X, b2).score(X, b2)
        b11 = 1 / (1 - b10)
        vif_dict[exo] = b11
        b12 = 1 - b10
        b8[exo] = b12
    b13 = pd.DataFrame({'VIF': vif_dict, 'Tolerance': b8})
    return b13
x_train, b14 = fonk1()
a1 = 2
b15 = preprocessing.PolynomialFeatures(a1=a1)
b16 = b15.fit_transform(x_train)
b17 = linear_model.LinearRegression()
b17.fit(b16, b14)
b18 = b17.predict(b16)
fonk2(x_train, b14, b18)
fonk3(x_train)
b19 = b18 - b14
fonk4(b19, b18)
b20 = np.sqrt(mean_squared_error(b14, b18))
b21 = r2_score(b14, b18)
print("The model performance for the training set")
print("-------------------------------------------")
print(f"RMSE for training: {b20:.5f}")
print(f"R2 for training: {b21:.5f}")