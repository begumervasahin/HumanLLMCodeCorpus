from sklearn import linear_model
from sklearn.datasets.samples_generator import make_regression
import matplotlib.pyplot as plt
import scipy.stats as stats
plt.style.use('seaborn-whitegrid')
x2, b1 = make_regression(n_samples=100, n_features=1, noise=10)
b2 = linear_model.LinearRegression()
b2.fit(x2,b1)
b3 = b2.predict(x2)
def fonk1(x,y,b3):
    plt.scatter(x, y, b4 = 'black')
    plt.plot(x, b3, b5 = "3")
    plt.title("Linear Regression")
    plt.xlabel("Observed Values")
    plt.ylabel("Predicted Values")
    plt.show()
fonk1(x2,b1,b3)
b6 = b3-b1
def fonk2(b6,x):
    print(b6)
    plt.scatter(x, b6,  b4 = 'black')
    plt.axhline(0)
    plt.title("Residuals Versus Observed Values")
    plt.xlabel("Observed Values")
    plt.ylabel("Residuals")
    plt.show()
fonk2(b6,x2)
def fonk3(x):
    stats.probplot(x2[:,0], b7 = "norm", plot=plt)
    plt.title("QQ plot for Normality")
    plt.xlabel("Quantiles")
    plt.ylabel("Observed Values")
    plt.show()
fonk3(x2)