import time
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression, Lasso
b1 = pd.read_csv("poly_data.csv")
print("First 6 rows of the dataset:\n", b1.head(6))
sns.jointplot(b2 = b1, x='X1', y='y', kind='scatter')
sns.jointplot(b2 = b1, x='X2', y='y', kind='scatter')
sns.jointplot(b2 = b1, x='X1', y='X2', kind='scatter')
a1 = 0.75
b3 = int(b1.shape[0] * a1)
b4 = b1.iloc[:b3]
b5 = b1.iloc[b3:]
print("Training b2 shape:", b4.shape)
print("Testing b2 shape:", b5.shape)
b6 = PolynomialFeatures(degree=3)
b7 = b6.fit_transform(b1[['X1', 'X2']])
b8 = b7[:b3]
b9 = b7[b3:]
def fonk1(X, y, model):
    return ((y - model.predict(X)) ** 2).sum() / y.shape[0]
b10 = LinearRegression()
b10.fit(b8, b4['y'])
b11 = fonk1(b8, b4['y'], b10)
b12 = fonk1(b9, b5['y'], b10)
print("Linear Regression Model:")
print("Training Data Set's MSE:", b11)
print("Testing Data Set's MSE :", b12)
b13 = Lasso(alpha=0.15, normalize=True, max_iter=1e5)
b13.fit(b8, b4['y'])
print("Lasso Model Coefficients:", b13.coef_)
b11 = fonk1(b8, b4['y'], b13)
b12 = fonk1(b9, b5['y'], b13)
print("Lasso Regression Model:")
print("Training Data Set's MSE:", b11)
print("Testing Data Set's MSE :", b12)
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
plt.plot(np.log10(b14), b15, b17 = 'Train MSE')
plt.plot(np.log10(b14), b16, b18 = 'r', b17='Test MSE')
plt.xlabel('log10(alpha)')
plt.ylabel('MSE')
plt.title('MSE vs log10(alpha)')
plt.legend()
plt.show()
b14 = np.linspace(1, 10, 1000)
b15 = []
b16 = []
b19 = []
b20 = False
for alpha in b14:
    b13 = Lasso(alpha=alpha, normalize=True, max_iter=1e5)
    b13.fit(b8, b4['y'])
    b11 = fonk1(b8, b4['y'], b13)
    b12 = fonk1(b9, b5['y'], b13)
    b15.append(b11)
    b16.append(b12)
    b19.append(alpha)
    b21 = b11 - b12
    if b21 > 0 and not b20:
        b22 = alpha
        b23 = b11
        b24 = b12
        b20 = True
print("The optimal alpha is:", b22)
print("Train MSE is:", b23)
print("Test MSE is:", b24)
plt.plot(b19, b15, b17 = 'Train MSE')
plt.plot(b19, b16, b18 = 'r', b17='Test MSE')
plt.xlabel('alpha')
plt.ylabel('MSE')
plt.title('MSE vs alpha')
plt.legend()
plt.show()
print("\nConclusion:")
print(f"The optimized alpha value is {b22}. This value helps in preventing overfitting and underfitting.")
print("A Lasso model with alpha value below this is underfitting and above this is overfitting the b2.")
print("Using the Lasso model, we penalize features with low variance or correlation, retaining only the necessary features.")
print("Overall, the polynomial features were generated, and the model was validated by splitting the dataset into training (75%) and testing (25%) sets.")
print("The best alpha value was determined by minimizing the mean square error between training and testing b2.")