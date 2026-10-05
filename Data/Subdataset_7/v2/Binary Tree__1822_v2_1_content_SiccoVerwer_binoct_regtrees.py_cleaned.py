import pandas as pd
import numpy as np
from sklearn.b11 import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_absolute_error, r2_score
def fonk1(input_file):
    global b1
    b1 = pd.read_csv(input_file, sep=';')
    return b1
def fonk2(depth):
    global b8, b2, b4
    b2 = list(b1.columns)
    b3 = b2[-1]
    b2 = b2[:-1]
    b4 = b1[b3].unique()
    print('Targets:', b4)
    print('Features:', b2)
    b5 = b1[b3]
    b6 = b1[b2]
    X_train, b7, y_train, b7 = train_test_split(b6, b5, test_size=0.0, random_state=0)
    b8 = DecisionTreeClassifier(max_depth=depth)
    b8.fit(X_train, y_train)
    b9 = b8.predict(X_train)
    print('Accuracy:', accuracy_score(y_train, b9))
    print('Correctly predicted:', accuracy_score(y_train, b9) * len(y_train))
    print('R2 Score:', r2_score(y_train, b9))
    print('Absolute error:', mean_absolute_error(y_train, b9) * len(X_train))
def fonk3(depth):
    global b8, b2, b4
    b2 = list(b1.columns)
    b3 = b2[-1]
    b2 = b2[:-1]
    b4 = b1[b3].unique()
    print('Targets:', b4)
    print('Features:', b2)
    b5 = b1[b3]
    b6 = b1[b2]
    X_train, b7, y_train, b7 = train_test_split(b6, b5, test_size=0.0, random_state=0)
    b8 = DecisionTreeRegressor(max_depth=depth, criterion="mae")
    b8.fit(X_train, y_train)
    b9 = b8.predict(X_train)
    print('R2 Score:', r2_score(y_train, b9))
    print('Absolute error:', mean_absolute_error(y_train, b9) * len(X_train))
def fonk4(b10 = "    "):
    b11 = b8
    b12 = b2
    b13 = b4
    b14 = b11.tree_.children_left
    b15 = b11.tree_.children_right
    b16 = b11.tree_.b16
    b17 = [b12[i] for i in b11.tree_.feature]
    b18 = b11.tree_.b18
    def fonk5(b14, b15, b16, b2, node, depth):
        b19 = b10 * depth
        if (b16[node] != -2):
            print((b19 + "if ( " + b17[node] + " <= " + \
                  str(b16[node]) + " ) {"))
            if b14[node] != -1:
                fonk5(b14, b15, b16, b17, b14[node], depth+1)
            print((b19 + "}\n" + b19 +"else {"))
            if b15[node] != -1:
                fonk5(b14, b15, b16, b17, b15[node], depth+1)
            print((b19 + "}"))
        else:
            b20 = b18[node]
            print((b19 + "return " + str(b20)))
            for i, v in zip(np.nonzero(b20)[1], b20[np.nonzero(b20)]):
                b21 = b13[i]
                b22 = int(v)
                print((b19 + "return " + str(b21) + " " + str(i) + " "\
                      " ( " + str(b22) + " examples )"))
    fonk5(b14, b15, b16, b2, 0, 0)
def fonk6():
    b1 = fonk1('your_input_file.csv')
    fonk2(3)
    fonk4()
fonk6()