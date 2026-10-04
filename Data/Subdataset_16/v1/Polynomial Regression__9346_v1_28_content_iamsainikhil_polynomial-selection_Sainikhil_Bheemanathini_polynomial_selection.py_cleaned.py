import time
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression, Lasso
b1 = pd.read_csv("poly_data.csv")
print(b1.head(6))
sns.jointplot(b2 = b1, x='X1', y='y')
sns.jointplot(b2 = b1, x='X2', y='y')
sns.jointplot(b2 = b1, x='X1', y='X2')
a1 = 0.75
b3 = int(b1.shape[0] * a1)
b4 = b1.iloc[:b3]
b5 = b1.iloc[b3:]
print(b4.shape)
print(b5.shape)
b6 = PolynomialFeatures(degree=3)
b7 = b6.fit_transform(b1[['X1', 'X2']])
b8 = b7[:b3]
b9 = b7[b3:]
def fonk1(X, y, model):
    return ((y - model.predict(X)) ** 2).sum() / y.shape[0]
b10 = LinearRegression()
b10.fit(b8, b4['y'])
b11 = fonk1(b8, b4['y'], b10)
print("Training Data Set's MSE is: \t", b11)
b12 = fonk1(b9, b5['y'], b10)
print("Testing Data Set's MSE is : \t", b12)
b13 = Lasso(alpha=0.15, normalize=True, max_iter=1e5)
b13.fit(b8, b4['y'])
print(b13.coef_)
b11 = fonk1(b8, b4['y'], b13)
print("Training Data Set's MSE is: \t", b11)
b12 = fonk1(b9, b5['y'], b13)
print("Testing Data Set's MSE is : \t", b12)
b14 = np.logspace(2, -5, base=10, num=50)
b15 = []
b16 = []
for alpha in b14:
    b13 = Lasso(alpha=alpha, normalize=True, max_iter=1e5)
    b13.fit(b8, b4['y'])
    b11 = fonk1(b8, b4['y'], b13)
    b12 = fonk1(b9, b5['y'], b13)
    b15.append(b11)
    b16.append(b12)
plt.plot(np.log10(b14), b15)
plt.plot(np.log10(b14), b16, b17 = 'r')
plt.xlabel('log10(alpha)')
plt.ylabel('MSE')
plt.title('MSE vs log10(alpha)')
plt.show()
b14 = np.linspace(1, 10, 1000)
b15 = []
b16 = []
b18 = []
a2 = 0
for alpha in b14:
    b13 = Lasso(alpha=alpha, normalize=True, max_iter=1e5)
    b13.fit(b8, b4['y'])
    b11 = fonk1(b8, b4['y'], b13)
    b12 = fonk1(b9, b5['y'], b13)
    b15.append(b11)
    b16.append(b12)
    b18.append(alpha)
    b19 = b11 - b12
    if b19 > 0 and a2 != 1:
        b20 = alpha
        b21 = b11
        b22 = b12
        a2 = 1
print("The optimal alpha is", b20)
print("Train MSE is", b21)
print("Test MSE is", b22)
plt.plot(b18, b15)
plt.plot(b18, b16, b17 = 'r')
plt.xlabel('alpha')
plt.ylabel('MSE')
plt.title('MSE vs alpha')
plt.show()
print("From the above diagram, I found that the optimized alpha value is 3.567. This means that, at this alpha value, we can prevent overfitting and underfitting. Lasso model with alpha value below 3.567 is underfitting and above 3.567 is overfitting the b2. Instead of using a linear model, I used Lasso linear model which is used to penalize number of features with low variance or correlation. These features can be found by looking at the coefficients of the Lasso linear model.\n")
print("Overall, from the dataset, I found the polynomial that best fits the b2. I checked my model by dividing the dataset into training b2 and testing b2. I generated the model using the training b2 of 75% and then tested the model using the testing b2 of 25%. To prevent overfitting and underfitting, I generated a Lasso linear model with the optimized alpha value to penalize the features and retain only the required features. Thus, I reached the best alpha value by minimizing the mean square error between training b2 and testing b2.")