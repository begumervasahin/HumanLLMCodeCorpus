import random
import copy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import tree, ensemble, linear_model, svm, cross_validation
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier, export_graphviz
from sklearn.cross_validation import train_test_split
from sklearn.externals.six import StringIO
from sklearn.metrics import accuracy_score, mean_absolute_error, r2_score
df = None
dt = None
features = None
targets = None
def get_data(inputfile):
    global df
    df = pd.read_csv(inputfile, sep=';')
    return df
def learnTrees(depth):
    global dt, features, targets
    features = list(df.columns)
    target_feature = features[-1]
    features = list(features[:len(features) - 1])
    targets = df[target_feature].unique()
    print('targets:', targets)
    print('features:', features)
    y = df[target_feature]
    X = df[features]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.0, random_state=0)
    dt = DecisionTreeClassifier(max_depth=depth)
    dt.fit(X_train, y_train)
    prediction = dt.predict(X_train)
    print('accuracy:', accuracy_score(y_train, prediction))
    print('num correct:', accuracy_score(y_train, prediction) * len(y_train))
    print('R2 Score:', r2_score(y_train, prediction))
    print('absolute error:', mean_absolute_error(y_train, prediction) * len(X_train))
def learnRegTrees(depth):
    global dt, features, targets
    features = list(df.columns)
    target_feature = features[-1]
    features = list(features[:len(features) - 1])
    targets = df[target_feature].unique()
    print('targets:', targets)
    print('features:', features)
    y = df[target_feature]
    X = df[features]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.0, random_state=0)
    dt = DecisionTreeRegressor(max_depth=depth, criterion="mae")
    dt.fit(X_train, y_train)
    prediction = dt.predict(X_train)
    print('R2 Score:', r2_score(y_train, prediction))
    print('absolute error:', mean_absolute_error(y_train, prediction) * len(X_train))
def get_code(spacer_base="    "):
    tree = dt
    feature_names = features
    target_names = targets
    left = tree.tree_.children_left
    right = tree.tree_.children_right
    threshold = tree.tree_.threshold
    feats = [feature_names[i] for i in tree.tree_.feature]
    value = tree.tree_.value
    def recurse(left, right, threshold, features, node, depth):
        spacer = spacer_base * depth
        if (threshold[node] != -2):
            print((spacer + "if ( " + feats[node] + " <= " + \
                  str(threshold[node]) + " ) {"))
            if left[node] != -1:
                recurse(left, right, threshold, feats, left[node], depth + 1)
            print((spacer + "}\n" + spacer + "else {"))
            if right[node] != -1:
                recurse(left, right, threshold, feats, right[node], depth + 1)
            print((spacer + "}"))
        else:
            target = value[node]
            print((spacer + "return " + str(target)))
            for i, v in zip(np.nonzero(target)[1], target[np.nonzero(target)]):
                target_name = target_names[i]
                target_count = int(v)
                print((spacer + "return " + str(target_name) + " " + str(i) + " "\
                      " ( " + str(target_count) + " examples )"))
    recurse(left, right, threshold, features, 0, 0)
def run_tree():
    df = get_data(inputfile)
    learnTrees(3)
    get_code()