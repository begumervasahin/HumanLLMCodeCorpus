import random
import copy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import tree, ensemble, linear_model, svm, cross_validation
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier, export_graphviz
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score, mean_absolute_error, r2_score
def get_data(inputfile):
    df = pd.read_csv(inputfile, sep=';')
    return df
def learn_trees(depth):
    global dt, features, targets
    features = list(df.columns)[:-1]
    target_feature = df.columns[-1]
    targets = df[target_feature].unique()
    print('targets:', targets)
    print('features:', features)
    X = df[features]
    y = df[target_feature]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.0, random_state=0)
    dt = DecisionTreeClassifier(max_depth=depth)
    dt.fit(X_train, y_train)
    prediction = dt.predict(X_train)
    print('Accuracy:', accuracy_score(y_train, prediction))
    print('Number of correct predictions:', accuracy_score(y_train, prediction) * len(y_train))
    print('R2 Score:', r2_score(y_train, prediction))
    print('Mean Absolute Error:', mean_absolute_error(y_train, prediction) * len(X_train))
def learn_regression_trees(depth):
    global dt, features, targets
    features = list(df.columns)[:-1]
    target_feature = df.columns[-1]
    targets = df[target_feature].unique()
    print('targets:', targets)
    print('features:', features)
    X = df[features]
    y = df[target_feature]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.0, random_state=0)
    dt = DecisionTreeRegressor(max_depth=depth, criterion="mae")
    dt.fit(X_train, y_train)
    prediction = dt.predict(X_train)
    print('R2 Score:', r2_score(y_train, prediction))
    print('Mean Absolute Error:', mean_absolute_error(y_train, prediction) * len(X_train))
def get_code(spacer_base="    "):
    def recurse(left, right, threshold, features, node, depth):
        spacer = spacer_base * depth
        if threshold[node] != -2:
            print(f"{spacer}if ({feats[node]} <= {threshold[node]}) {{")
            if left[node] != -1:
                recurse(left, right, threshold, feats, left[node], depth + 1)
            print(f"{spacer}}}\n{spacer}else {{")
            if right[node] != -1:
                recurse(left, right, threshold, feats, right[node], depth + 1)
            print(f"{spacer}}}")
        else:
            target = value[node]
            for i, v in zip(np.nonzero(target)[1], target[np.nonzero(target)]):
                target_name = target_names[i]
                target_count = int(v)
                print(f"{spacer}return {target_name} {i} ({target_count} examples)")
    tree = dt
    feature_names = features
    target_names = targets
    left = tree.tree_.children_left
    right = tree.tree_.children_right
    threshold = tree.tree_.threshold
    feats = [feature_names[i] for i in tree.tree_.feature]
    value = tree.tree_.value
    recurse(left, right, threshold, features, 0, 0)
def run_tree(inputfile):
    global df
    df = get_data(inputfile)
    learn_trees(3)
    get_code()
