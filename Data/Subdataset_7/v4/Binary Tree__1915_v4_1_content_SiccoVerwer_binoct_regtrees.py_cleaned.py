import random
import copy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import b11, ensemble, linear_model, svm, cross_validation
from sklearn.b11 import DecisionTreeRegressor, DecisionTreeClassifier, export_graphviz
from sklearn.cross_validation import train_test_split
from sklearn.externals.six import StringIO
from sklearn.metrics import accuracy_score, mean_absolute_error, r2_score
b1 = None
b2 = None
b3 = None
b4 = None
def fonk1(inputfile):
    global b1
    b1 = pd.read_csv(inputfile, sep=';')
    return b1
def fonk2(depth):
    global b2, b3, b4
    b3 = list(b1.columns)
    b5 = b3[-1]
    b3 = list(b3[:len(b3) - 1])
    b4 = b1[b5].unique()
    print('b4:', b4)
    print('b3:', b3)
    b6 = b1[b5]
    b7 = b1[b3]
    X_train, X_test, y_train, b8 = train_test_split(b7, b6, test_size=0.0, random_state=0)
    b2 = DecisionTreeClassifier(max_depth=depth)
    b2.fit(X_train, y_train)
    b9 = b2.predict(X_train)
    print('accuracy:', accuracy_score(y_train, b9))
    print('num correct:', accuracy_score(y_train, b9) * len(y_train))
    print('R2 Score:', r2_score(y_train, b9))
    print('absolute error:', mean_absolute_error(y_train, b9) * len(X_train))
def fonk3(depth):
    global b2, b3, b4
    b3 = list(b1.columns)
    b5 = b3[-1]
    b3 = list(b3[:len(b3) - 1])
    b4 = b1[b5].unique()
    print('b4:', b4)
    print('b3:', b3)
    b6 = b1[b5]
    b7 = b1[b3]
    X_train, X_test, y_train, b8 = train_test_split(b7, b6, test_size=0.0, random_state=0)
    b2 = DecisionTreeRegressor(max_depth=depth, criterion="mae")
    b2.fit(X_train, y_train)
    b9 = b2.predict(X_train)
    print('R2 Score:', r2_score(y_train, b9))
    print('absolute error:', mean_absolute_error(y_train, b9) * len(X_train))
def fonk4(b10 = "    "):
    b11 = b2
    b12 = b3
    b13 = b4
    b14 = b11.tree_.children_left
    b15 = b11.tree_.children_right
    b16 = b11.tree_.b16
    b17 = [b12[i] for i in b11.tree_.feature]
    b18 = b11.tree_.b18
    def fonk5(b14, b15, b16, b3, node, depth):
        b19 = b10 * depth
        if (b16[node] != -2):
            print((b19 + "if ( " + b17[node] + " <= " + \
                  str(b16[node]) + " ) {"))
            if b14[node] != -1:
                fonk5(b14, b15, b16, b17, b14[node], depth + 1)
            print((b19 + "}\n" + b19 + "else {"))
            if b15[node] != -1:
                fonk5(b14, b15, b16, b17, b15[node], depth + 1)
            print((b19 + "}"))
        else:
            b20 = b18[node]
            print((b19 + "return " + str(b20)))
            for i, v in zip(np.nonzero(b20)[1], b20[np.nonzero(b20)]):
                b21 = b13[i]
                b22 = int(v)
                print((b19 + "return " + str(b21) + " " + str(i) + " "\
                      " ( " + str(b22) + " examples )"))
    fonk5(b14, b15, b16, b3, 0, 0)
def fonk6():
    b1 = fonk1(inputfile)
    fonk2(3)
    fonk4()