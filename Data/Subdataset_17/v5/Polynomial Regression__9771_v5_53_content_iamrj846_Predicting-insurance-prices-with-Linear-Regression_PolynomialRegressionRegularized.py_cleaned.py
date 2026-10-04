import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler, PolynomialFeatures
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
dataset = pd.read_csv('insurance.csv')
X = dataset.iloc[:, :5].values
y = dataset.iloc[:, 6].values
def encode_categorical_features(X):
    labelencoder = LabelEncoder()
    X[:, 1] = labelencoder.fit_transform(X[:, 1])
    X[:, 4] = labelencoder.fit_transform(X[:, 4])
    return X
X = encode_categorical_features(X)
def one_hot_encode(X):
    onehotencoder = OneHotEncoder(categorical_features=[1, 4])
    X = onehotencoder.fit_transform(X).toarray()
    return X[:, [1, 3, 4, 5, 6]]
X = one_hot_encode(X)
sc_X = StandardScaler()
X = sc_X.fit_transform(X)
sc_y = StandardScaler()
y = sc_y.fit_transform(y.reshape(-1, 1))
poly_regressor = PolynomialFeatures(degree=4)
X_poly = poly_regressor.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=0)
lasso_regressor = Lasso(alpha=0.01, fit_intercept=False)
lasso_regressor.fit(X_train, y_train)
def make_predictions(model, X_train, X_test, sc_y):
    y_pred_train = model.predict(X_train)
    y_pred_train = sc_y.inverse_transform(y_pred_train)
    y_pred_test = model.predict(X_test)
    y_pred_test = sc_y.inverse_transform(y_pred_test)
    return y_pred_train, y_pred_test
y_pred_train, y_pred_test = make_predictions(lasso_regressor, X_train, X_test, sc_y)
y_train = sc_y.inverse_transform(y_train)
y_test = sc_y.inverse_transform(y_test)
def evaluate_model_performance(y_true, y_pred):
    return r2_score(y_true, y_pred) * 100
r2_score_train = evaluate_model_performance(y_train, y_pred_train)
r2_score_test = evaluate_model_performance(y_test, y_pred_test)
print(f'R2 Score on Training Set: {r2_score_train:.2f}%')
print(f'R2 Score on Test Set: {r2_score_test:.2f}%')