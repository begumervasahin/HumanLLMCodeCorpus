import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
def fonk1(filepath):
    return pd.read_csv(filepath, b1 = None)
def fonk2(data):
    b2 = data.iloc[:, :-1].values
    b3 = data.iloc[:, -1].values
    return b2, b3
def fonk3(b2, b3, b4 = 0.3, random_state=1):
    return train_test_split(b2, b3, b4 = b4, random_state=random_state)
def fonk4(X_train, X_test, y_train, y_test, degrees):
    b5 = []
    b6 = []
    for degree in degrees:
        b7 = PolynomialFeatures(degree=degree)
        b8 = b7.fit_transform(X_train)
        b9 = b7.transform(X_test)
        model