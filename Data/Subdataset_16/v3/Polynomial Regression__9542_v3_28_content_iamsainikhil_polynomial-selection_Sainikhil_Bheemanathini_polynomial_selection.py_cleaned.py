import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression, Lasso
def fonk1(file_path):
    b1 = pd.read_csv(file_path)
    print("First 6 rows of the dataset:\n", b1.head(6))
    return b1
def fonk2(b1):
    sns.jointplot(b1 = b1, x='X1', y='y', kind='scatter')
    sns.jointplot(b1 = b1, x='X2', y='y', kind='scatter')
    sns.jointplot(b1 = b1, x='X1', y='X2', kind='scatter')
    plt.show()
def fonk3(b1, b2 = 0.75):
    b3 = int(b1.shape[0] * b2)
    b4 = b1.iloc[:b3]
    b5 = b1.iloc[b3:]
    print("Training b1 shape:", b4.shape)
    print("Testing b1 shape:", b5.shape)
    return b4, b5
def fonk4(b1, b6 = 3):
    b7 = PolynomialFeatures(b6=b6)
    b8 = b7.fit_transform(b1[['X1', 'X2']])
    return b8
def fonk5(X, y, b9):
    return ((y - b9.predict(X)) ** 2).mean()
def fonk6(X_train, y_train):
    b9 = LinearRegression()
    b9.fit(X_train, y_train)
    return b9
def fonk7(X_train, y_train, b10 = 0.15):
    b9 = Lasso(b10=b10, normalize=True, max_iter=1e5)
    b9.fit(X_train, y_train)
    return b9
def fonk8(X_train, y_train, b23, b24, alphas):
    b11 = []
    b12 = []
    b13 = None
    b14 = None
    b15 = None
    b16 = False
    for b10 in alphas:
        b9 = fonk7(X_train, y_train, b10)
        b17 = fonk5(X_train, y_train, b9)
        b18 = fonk5(b23, b24, b9)
        b11.append(b17)
        b12.append(b18)
        if b17 > b18 and not b16:
            b13 = b10
            b14 = b17
            b15 = b18
            b16 = True
    return b13, b14, b15, b11, b12
def fonk9(alphas, b11, b12, xlabel, title):
    plt.plot(alphas, b11, b19 = 'Train MSE')
    plt.plot(alphas, b12, b20 = 'r', b19='Test MSE')
    plt.xlabel(xlabel)
    plt.ylabel('MSE')
    plt.title(title)
    plt.legend()
    plt.show()
def fonk10():
    b21 = fonk1("poly_data.csv")
    fonk2(b21)
    train_df, b22 = fonk3(b21)
    b8 = fonk4(b21)
    X_train, b23 = b8[:train_df.shape[0]], b8[train_df.shape[0]:]
    y_train, b24 = train_df['y'], b22['y']
    b25 = fonk6(X_train, y_train)
    print("Linear Regression Model:")
    print("Training Data Set's MSE:", fonk5(X_train, y_train, b25))
    print("Testing Data Set's MSE :", fonk5(b23, b24, b25))
    b26 = fonk7(X_train, y_train)
    print("Lasso Regression Model Coefficients:", b26.coef_)
    print("Lasso Regression Model:")
    print("Training Data Set's MSE:", fonk5(X_train, y_train, b26))
    print("Testing Data Set's MSE :", fonk5(b23, b24, b26))
    b27 = np.logspace(2, -5, base=10, num=50)
    b13, b14, b15, train_mse_log_array, b28 = fonk8(
        X_train, y_train, b23, b24, b27)
    fonk9(np.log10(b27), train_mse_log_array, b28, 'log10(b10)', 'MSE vs log10(b10)')
    b29 = np.linspace(1, 10, 1000)
    b13, b14, b15, train_mse_lin_array, b30 = fonk8(
        X_train, y_train, b23, b24, b29)
    fonk9(b29, train_mse_lin_array, b30, 'b10', 'MSE vs b10')
    print("\nConclusion:")
    print(f"The optimized b10 value is {b13}. This value helps in preventing overfitting and underfitting.")
    print("A Lasso b9 with b10 value below this is underfitting and above this is overfitting the b1.")
    print("Using the Lasso b9, we penalize features with low variance or correlation, retaining only the necessary features.")
    print("Overall, the polynomial features were generated, and the b9 was validated by splitting the dataset into training (75%) and testing (25%) sets.")
    print("The best b10 value was determined by minimizing the mean square error between training and testing b1.")
if b31 = = "__main__":
    fonk10()