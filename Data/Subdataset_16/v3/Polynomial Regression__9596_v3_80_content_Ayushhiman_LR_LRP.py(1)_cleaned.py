import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures
from sklearn.feature_selection import f_regression, mutual_info_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
def fonk1(b14):
    b1 = pd.read_csv(b14)
    print(b1.head())
    print(b1.describe())
    return b1
def fonk2(b1):
    sns.set_palette("GnBu_d")
    sns.set_style('whitegrid')
    sns.jointplot(b2 = 'Time on Website', b3='Yearly Amount Spent', data=b1)
    sns.jointplot(b2 = 'Time on App', b3='Yearly Amount Spent', data=b1)
    sns.jointplot(b2 = 'Time on App', b3='Length of Membership', kind='hex', data=b1)
    sns.pairplot(b1)
    sns.lmplot(b2 = 'Length of Membership', b3='Yearly Amount Spent', data=b1)
    plt.show()
def fonk3(b1):
    b3 = b1['Yearly Amount Spent']
    b4 = b1[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
    return b4, b3
def fonk4(b4, b5 = 2):
    b6 = PolynomialFeatures(b5=b5, interaction_only=False, include_bias=True)
    return b6.fit_transform(b4)
def fonk5(b4, b3):
    print(f_regression(b4, b3, b7 = True))
    print(mutual_info_regression(b4, b3, b8 = 'auto', n_neighbors=3, copy=True, random_state=None))
def fonk6(b4, b3, b9 = 0.3, random_state=101):
    return train_test_split(b4, b3, b9 = b9, random_state=random_state)
def fonk7(X_train, y_train, X1_train, X2_train):
    b10 = LinearRegression()
    b11 = LinearRegression()
    b12 = LinearRegression()
    b10.fit(X_train, y_train)
    b11.fit(X1_train, y_train)
    b12.fit(X2_train, y_train)
    return b10, b11, b12
def fonk8(models):
    for i, model in enumerate(models, 1):
        print(f'Model {i} Coefficients:', model.coef_)
def fonk9(models, X_tests):
    return [model.predict(X_test) for model, X_test in zip(models, X_tests)]
def fonk10(b17, predictions, title):
    plt.scatter(b17, predictions)
    plt.xlabel('Y Test')
    plt.ylabel('Predicted Y')
    plt.title(title)
    plt.show()
def fonk11(b17, predictions, model_name):
    print(f'{model_name}')
    print('MAE:', metrics.mean_absolute_error(b17, predictions))
    print('MSE:', metrics.mean_squared_error(b17, predictions))
    print('RMSE:', np.sqrt(metrics.mean_squared_error(b17, predictions)))
    print()
if b13 = = "__main__":
    b14 = "Ecommerce Customers"
    b15 = fonk1(b14)
    fonk2(b15)
    b4, b3 = fonk3(b15)
    b16 = fonk4(b4)
    fonk5(b4, b3)
    X_train, X_test, y_train, b17 = fonk6(b4, b3)
    b18 = b4.drop('Time on App', axis=1)
    X1_train, X1_test, y_train, b17 = fonk6(b18, b3)
    X2_train, X2_test, y_train, b17 = fonk6(b16, b3)
    b10, b11, b12 = fonk7(X_train, y_train, X1_train, X2_train)
    fonk8([b10, b11, b12])
    predictions, predictions1, b19 = fonk9([b10, b11, b12], [X_test, X1_test, X2_test])
    fonk10(b17, predictions, 'Model 1 Predictions')
    fonk10(b17, predictions1, 'Model 2 Predictions')
    fonk10(b17, b19, 'Model 3 Predictions')
    fonk11(b17, predictions, 'Model 1')
    fonk11(b17, predictions1, 'Model 2')
    fonk11(b17, b19, 'Model 3')