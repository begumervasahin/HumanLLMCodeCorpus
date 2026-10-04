import random
import copy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import b15, ensemble, linear_model, svm, cross_validation
from sklearn.b15 import DecisionTreeRegressor, DecisionTreeClassifier, export_graphviz
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score, mean_absolute_error, r2_score
def fonk1(inputfile):
    b1 = pd.read_csv(inputfile, sep=';')
    return b1
def fonk2(depth):
    global b8, b2, b4
    b2 = list(b1.columns)[:-1]
    b3 = b1.columns[-1]
    b4 = b1[b3].unique()
    print('b4:', b4)
    print('b2:', b2)
    b5 = b1[b2]
    b6 = b1[b3]
    X_train, X_test, y_train, b7 = train_test_split(b5, b6, test_size=0.0, random_state=0)
    b8 = DecisionTreeClassifier(max_depth=depth)
    b8.fit(X_train, y_train)
    b9 = b8.predict(X_train)
    print('Accuracy:', accuracy_score(y_train, b9))
    print('Number of correct predictions:', accuracy_score(y_train, b9) * len(y_train))
    print('R2 Score:', r2_score(y_train, b9))
    print('Mean Absolute Error:', mean_absolute_error(y_train, b9) * len(X_train))
def fonk3(depth):
    global b8, b2, b4
    b2 = list(b1.columns)[:-1]
    b3 = b1.columns[-1]
    b4 = b1[b3].unique()
    print('b4:', b4)
    print('b2:', b2)
    b5 = b1[b2]
    b6 = b1[b3]
    X_train, X_test, y_train, b7 = train_test_split(b5, b6, test_size=0.0, random_state=0)
    b8 = DecisionTreeRegressor(max_depth=depth, criterion="mae")
    b8.fit(X_train, y_train)
    b9 = b8.predict(X_train)
    print('R2 Score:', r2_score(y_train, b9))
    print('Mean Absolute Error:', mean_absolute_error(y_train, b9) * len(X_train))
def fonk4(b10 = "    "):
    def fonk5(b18, b19, b20, b2, node, depth):
        b11 = b10 * depth
        if b20[node] != -2:
            print(f"{b11}if ({b21[node]} <= {b20[node]}) {{")
            if b18[node] != -1:
                fonk5(b18, b19, b20, b21, b18[node], depth + 1)
            print(f"{b11}}}\n{b11}else {{")
            if b19[node] != -1:
                fonk5(b18, b19, b20, b21, b19[node], depth + 1)
            print(f"{b11}}}")
        else:
            b12 = b22[node]
            for i, v in zip(np.nonzero(b12)[1], b12[np.nonzero(b12)]):
                b13 = b17[i]
                b14 = int(v)
                print(f"{b11}return {b13} {i} ({b14} examples)")
    b15 = b8
    b16 = b2
    b17 = b4
    b18 = b15.tree_.children_left
    b19 = b15.tree_.children_right
    b20 = b15.tree_.b20
    b21 = [b16[i] for i in b15.tree_.feature]
    b22 = b15.tree_.b22
    fonk5(b18, b19, b20, b2, 0, 0)
def fonk6(inputfile):
    global b1
    b1 = fonk1(inputfile)
    fonk2(3)
    fonk4()
