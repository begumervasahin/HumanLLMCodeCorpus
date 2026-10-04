import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures
from sklearn.feature_selection import f_regression, mutual_info_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
def fonk1(b15):
    sns.set_palette("GnBu_d")
    sns.set_style('whitegrid')
    sns.jointplot(b1 = 'Time on Website', b2='Yearly Amount Spent', b15=b15)
    sns.jointplot(b1 = 'Time on App', b2='Yearly Amount Spent', b15=b15)
    sns.jointplot(b1 = 'Time on App', b2='Length of Membership', kind='hex', b15=b15)
    sns.pairplot(b15)
    sns.lmplot(b1 = 'Length of Membership', b2='Yearly Amount Spent', b15=b15)
    plt.show()
def fonk2(b15):
    b2 = b15['Yearly Amount Spent']
    b3 = b15[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
    b4 = PolynomialFeatures(degree=2, interaction_only=False, include_bias=True)
    b5 = b4.fit_transform(b3)
    return b3, b5, b2
def fonk3(b3, b2):
    f_scores, b6 = f_regression(b3, b2, center=True)
    b7 = mutual_info_regression(b3, b2, discrete_features='auto', n_neighbors=3, copy=True, random_state=None)
    print("F-regression scores:", f_scores)
    print("Mutual Information Regression scores:", b7)
def fonk4(b3, b2):
    return train_test_split(b3, b2, b8 = 0.3, random_state=101)
def fonk5(X_train, y_train, X_reduced_train, X_poly_train):
    b9 = LinearRegression()
    b10 = LinearRegression()
    b11 = LinearRegression()
    b9.fit(X_train, y_train)
    b10.fit(X_reduced_train, y_train)
    b11.fit(X_poly_train, y_train)
    return b9, b10, b11
def fonk6(b9, b10, b11):
    print('Coefficients for model with all features: \n', b9.coef_)
    print('Coefficients for model without Time on App: \n', b10.coef_)
    print('Coefficients for model with polynomial features: \n', b11.coef_)
def fonk7(models, test_sets):
    return [model.predict(test_set) for model, test_set in zip(models, test_sets)]
def fonk8(b16, b19):
    plt.figure(b12 = (10, 6))
    b13 = ['Model with all features', 'Model without Time on App', 'Model with polynomial features']
    for prediction, b14 in zip(b19, b13):
        plt.scatter(b16, prediction, b14 = b14)
    plt.xlabel('Y Test')
    plt.ylabel('Predicted Y')
    plt.legend()
    plt.show()
def fonk9(y_true, b19, b13):
    for prediction, b14 in zip(b19, b13):
        print(f'{b14}')
        print('MAE:', metrics.mean_absolute_error(y_true, prediction))
        print('MSE:', metrics.mean_squared_error(y_true, prediction))
        print('RMSE:', np.sqrt(metrics.mean_squared_error(y_true, prediction)))
        print()
def fonk10():
    b15 = pd.read_csv("Ecommerce Customers.csv")
    fonk1(b15)
    b3, b5, b2 = fonk2(b15)
    fonk3(b3, b2)
    X_train, X_test, y_train, b16 = fonk4(b3, b2)
    b17 = b3.drop('Time on App', axis=1)
    X_reduced_train, X_reduced_test, b18, b18 = fonk4(b17, b2)
    X_poly_train, X_poly_test, b18, b18 = fonk4(b5, b2)
    b9, b10, b11 = fonk5(X_train, y_train, X_reduced_train, X_poly_train)
    fonk6(b9, b10, b11)
    b19 = fonk7([b9, b10, b11], [X_test, X_reduced_test, X_poly_test])
    fonk8(b16, b19)
    b13 = ['Model with all features', 'Model without Time on App', 'Model with polynomial features']
    fonk9(b16, b19, b13)
if b20 = = "__main__":
    fonk10()