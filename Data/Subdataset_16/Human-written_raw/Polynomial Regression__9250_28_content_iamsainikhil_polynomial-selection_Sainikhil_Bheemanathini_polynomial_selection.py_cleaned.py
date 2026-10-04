import time
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from pandas import Series, DataFrame
import pandas as pd
get_ipython().magic(u'matplotlib inline')
b1 = pd.read_csv("poly_data.csv")
print(b1.head(6))
sns.jointplot(b1['X1'], b1['y'])
sns.jointplot(b1['X2'], b1['y'])
sns.jointplot(b1['X1'], b1['X2'])
a1 = 0.75
b2 = int(b1.shape[0]*a1)
b3 = b1[0:b2]
b4 = b1[b2:]
print(b3.shape)
print(b4.shape)
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
b5 = PolynomialFeatures(degree=3)
b6 = b5.fit_transform(b1[['X1','X2']])
b7 = b6[0:b2]
b8 = b6[b2:]
def fonk1(X, y, model):
    return  ((y-model.predict(X))**2).sum()/y.shape[0]
b9 = LinearRegression()
b9.fit(b7, b3['y'])
b10 = fonk1(b7, b3['y'], b9)
print("Training Data Set's MSE is: \t", b10)
b11 = fonk1(b8, b4['y'], b9)
print("Testing Data Set's MSE is : \t", b11)
from sklearn.linear_model import Lasso
b12 = Lasso(alpha=0.15,normalize=True, max_iter=1e5, )
b12.fit(b7, b3['y'])
b12.coef_
b10 = fonk1(b7, b3['y'], b12)
print("Training Data Set's MSE is: \t", b10)
b11 = fonk1(b8, b4['y'], b12)
print("Testing Data Set's MSE is : \t", b11)
b13 = np.logspace(2, -5, base=10, num=50)
b13
b14 = []
b15 = []
for alpha in b13:
    b12 = Lasso(alpha=alpha,normalize=True, max_iter=1e5, )
    b12.fit(b7, b3['y'])
    b10 = fonk1(b7, b3['y'], b12)
    b11 = fonk1(b8, b4['y'], b12)
    b14.append(b10)
    b15.append(b11)
plt.plot(np.log10(b13), b14)
plt.plot(np.log10(b13), b15, b16 = 'r')
b13 = np.linspace(1, 10, 1000)
b14 = []
b15 = []
b17 = []
a2 = 0
for alpha in b13:
    b12 = Lasso(alpha=alpha,normalize=True, max_iter=1e5, )
    b12.fit(b7, b3['y'])
    b10 = fonk1(b7, b3['y'], b12)
    b11 = fonk1(b8, b4['y'], b12)
    b14.append(b10)
    b15.append(b11)
    b17.append(alpha)
    b18 = b10 - b11
    if (b18 > 0 and a2 != 1):
        b19 = alpha
        b20 = b10
        b21 = b11
        a2 = 1
print("The optimal alpha is", b19)
print("Train MSE is", b20)
print("Test MSE is", b21)
plt.plot(b17, b14)
plt.plot(b17, b15, b16 = 'r')
print("From the above diagram, I found that the optimized alpha value is 3.567. This means that, at this alpha value, we can prevent overfitting and underfitting. Lasso model with alpha value below 3.567 is underfitting and above 3.567 is overfitting the data. Instead of using linear model, I used Lasso linear model which is used to penalize number of features with low variance or correlation. These features can be found by looking at the coefficients of the Lasso linear model.\n")
print("Overall, from the dataset, I found the polynomial that best fits the data. I checked my model by dividing the dataset into training data and testing data. I generated the model using the training data of 75% and then test the model using the testing data of 25%. To prevent overfitting and underfitting, I generated Lasso linear model with the optimized alpha value to penalize the features and retain only the required features. Thus, I reached the best alpha value by minimizing the mean square error between training data and testing data.")