from sklearn import linear_model
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error, r2_score
import operator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
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
def fonk2(b1,b2,b10):
    b8 = operator.itemgetter(0)
    b9 = sorted(zip(b1, b10), key=b8)
    b1, b10 = zip(*b9)
    plt.scatter(b1, b2, b11 = 'black')
    plt.plot(b1, b10, b12 = "3")
    plt.title("Polynomial Regression")
    plt.xlabel("Observed Values")
    plt.ylabel("Predicted Values")
    plt.show()
fonk2(x_train, b3,b7)
def fonk3(b1):
    stats.probplot(b1[:,0], b13 = "norm", plot=plt)
    plt.title("QQ plot for Normality")
    plt.xlabel("Quantiles")
    plt.ylabel("Observed Values")
    plt.show()
fonk3(x_train)
b14 = b7 - b3
def fonk4(residuals,b2):
    plt.scatter(b2, residuals,  b11 = 'black')
    plt.axhline(0)
    plt.title("Residuals Versus Predicted Values")
    plt.xlabel("Predicted Values")
    plt.ylabel("Residuals")
    plt.show()
fonk4(b14, b7)
def fonk5(exos, data):
    vif_dict, b15 = {}, {}
    for exo in exos:
        b16 = [i for i in exos if i != exo]
        X, b2 = data[b16], data[exo]
        b17 = linear_model.LinearRegression().fit(X, b2).score(X, b2)
        b18 = 1/(1 - b17)
        vif_dict[exo] = b18
        b19 = 1 - b17
        b15[exo] = b19
    b20 = pd.DataFrame({'VIF': vif_dict, 'Tolerance': b15})
    return b20
b21 = np.sqrt(mean_squared_error(b3, b7))
b22 = r2_score(b3, b7)
print("The model performance for the training set")
print("-------------------------------------------")
print("RMSE for training: {:.5f}".format(b21))
print("R2 for training: {:.5f}".format(b22))