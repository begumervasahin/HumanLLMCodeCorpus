import random
import copy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import b14, ensemble, linear_model, svm, cross_validation
from sklearn.b14 import DecisionTreeRegressor, DecisionTreeClassifier, export_graphviz
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score, mean_absolute_error, r2_score
def fonk1(inputfile):
    return pd.read_csv(inputfile, b1 = ';')
def fonk2(b20, max_depth):
    b2 = b20.columns[:-1]
    b3 = b20.columns[-1]
    b4 = b20[b2]
    b5 = b20[b3]
    X_train, X_test, y_train, b6 = train_test_split(b4, b5, test_size=0.0, random_state=0)
    b7 = DecisionTreeClassifier(max_depth=max_depth)
    b7.fit(X_train, y_train)
    b8 = b7.predict(X_train)
    print(f'Accuracy: {accuracy_score(y_train, b8):.2f}')
    print(f'Number of correct predictions: {accuracy_score(y_train, b8) * len(y_train)}')
    print(f'R2 Score: {r2_score(y_train, b8):.2f}')
    print(f'Mean Absolute Error: {mean_absolute_error(y_train, b8) * len(X_train):.2f}')
    return b7, b2, b5.unique()
def fonk3(b20, max_depth):
    b2 = b20.columns[:-1]
    b3 = b20.columns[-1]
    b4 = b20[b2]
    b5 = b20[b3]
    X_train, X_test, y_train, b6 = train_test_split(b4, b5, test_size=0.0, random_state=0)
    b7 = DecisionTreeRegressor(max_depth=max_depth, criterion="mae")
    b7.fit(X_train, y_train)
    b8 = b7.predict(X_train)
    print(f'R2 Score: {r2_score(y_train, b8):.2f}')
    print(f'Mean Absolute Error: {mean_absolute_error(y_train, b8) * len(X_train):.2f}')
    return b7, b2, b5.unique()
def fonk4(b7, b2, b21, b9 = "    "):
    def fonk5(b15, b16, b17, b2, node, b19):
        b10 = b9 * b19
        if b17[node] != -2:
            print(f"{b10}if ({b2[node]} <= {b17[node]}) {{")
            if b15[node] != -1:
                fonk5(b15, b16, b17, b2, b15[node], b19 + 1)
            print(f"{b10}}}\n{b10}else {{")
            if b16[node] != -1:
                fonk5(b15, b16, b17, b2, b16[node], b19 + 1)
            print(f"{b10}}}")
        else:
            b11 = b18[node]
            for i, v in zip(np.nonzero(b11)[1], b11[np.nonzero(b11)]):
                b12 = b21[i]
                b13 = int(v)
                print(f"{b10}return {b12} ({b13} examples)")
    b14 = b7.tree_
    b15 = b14.children_left
    b16 = b14.children_right
    b17 = b14.b17
    b2 = [b2[i] for i in b14.feature]
    b18 = b14.b18
    fonk5(b15, b16, b17, b2, 0, 0)
def fonk6(inputfile, b19 = 3):
    b20 = fonk1(inputfile)
    b7, b2, b21 = fonk2(b20, b19)
    fonk4(b7, b2, b21)
