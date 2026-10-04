import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.b11 import DecisionTreeRegressor, DecisionTreeClassifier, export_graphviz
from sklearn.metrics import accuracy_score, mean_absolute_error, r2_score
b1 = None
b2 = None
b3 = None
b4 = None
def fonk1(b25):
    global b1
    b1 = pd.read_csv(b25, sep=';')
    return b1
def fonk2():
    global b3, b4
    b3 = list(b1.columns)
    b5 = b3.pop()
    b4 = b1[b5].unique()
    b6 = b1[b3]
    b7 = b1[b5]
    return b6, b7, b5
def fonk3(depth):
    global b2
    b6, b7, b5 = fonk2()
    print('Targets:', b4)
    print('Features:', b3)
    X_train, b8, y_train, b8 = train_test_split(b6, b7, test_size=0.0, random_state=0)
    b2 = DecisionTreeClassifier(max_depth=depth)
    b2.fit(X_train, y_train)
    b9 = b2.predict(X_train)
    print('Accuracy:', accuracy_score(y_train, b9))
    print('Number correct:', accuracy_score(y_train, b9) * len(y_train))
    print('R2 Score:', r2_score(y_train, b9))
    print('Absolute error:', mean_absolute_error(y_train, b9) * len(X_train))
def fonk4(depth):
    global b2
    b6, b7, b5 = fonk2()
    print('Targets:', b4)
    print('Features:', b3)
    X_train, b8, y_train, b8 = train_test_split(b6, b7, test_size=0.0, random_state=0)
    b2 = DecisionTreeRegressor(max_depth=depth, criterion="mae")
    b2.fit(X_train, y_train)
    b9 = b2.predict(X_train)
    print('R2 Score:', r2_score(y_train, b9))
    print('Absolute error:', mean_absolute_error(y_train, b9) * len(X_train))
def fonk5(b10 = "    "):
    global b2, b3, b4
    b11 = b2.tree_
    b12 = b3
    b13 = b4
    b14 = b11.children_left
    b15 = b11.children_right
    b16 = b11.b16
    b17 = [b12[i] for i in b11.feature]
    b18 = b11.b18
    def fonk6(node, depth):
        b19 = b10 * depth
        if b16[node] != -2:
            print(f"{b19}if ( {b17[node]} <= {b16[node]} ) {{")
            if b14[node] != -1:
                fonk6(b14[node], depth + 1)
            print(f"{b19}}}\n{b19}else {{")
            if b15[node] != -1:
                fonk6(b15[node], depth + 1)
            print(f"{b19}}}")
        else:
            b20 = b18[node]
            b21 = b13[np.argmax(b20)]
            b22 = int(np.sum(b20))
            print(f"{b19}return {b21} ( {b22} examples )")
    fonk6(0, 0)
def fonk7(b23 = "b11.dot"):
    with open(b23, 'w') as f:
        export_graphviz(b2, b24 = f, b12=b3)
def fonk8():
    global b1
    b25 = 'data.csv'
    b1 = fonk1(b25)
    fonk3(3)
    fonk5()
if b26 = = '__main__':
    fonk8()