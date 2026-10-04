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
def load_data(inputfile):
    return pd.read_csv(inputfile, sep=';')
def train_decision_tree_classifier(df, max_depth):
    features = df.columns[:-1]
    target_feature = df.columns[-1]
    X = df[features]
    y = df[target_feature]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.0, random_state=0)
    dt = DecisionTreeClassifier(max_depth=max_depth)
    dt.fit(X_train, y_train)
    prediction = dt.predict(X_train)
    print(f'Accuracy: {accuracy_score(y_train, prediction):.2f}')
    print(f'Number of correct predictions: {accuracy_score(y_train, prediction) * len(y_train)}')
    print(f'R2 Score: {r2_score(y_train, prediction):.2f}')
    print(f'Mean Absolute Error: {mean_absolute_error(y_train, prediction) * len(X_train):.2f}')
    return dt, features, y.unique()
def train_decision_tree_regressor(df, max_depth):
    features = df.columns[:-1]
    target_feature = df.columns[-1]
    X = df[features]
    y = df[target_feature]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.0, random_state=0)
    dt = DecisionTreeRegressor(max_depth=max_depth, criterion="mae")
    dt.fit(X_train, y_train)
    prediction = dt.predict(X_train)
    print(f'R2 Score: {r2_score(y_train, prediction):.2f}')
    print(f'Mean Absolute Error: {mean_absolute_error(y_train, prediction) * len(X_train):.2f}')
    return dt, features, y.unique()
def generate_tree_code(dt, features, targets, spacer_base="    "):
    def recurse(left, right, threshold, features, node, depth):
        spacer = spacer_base * depth
        if threshold[node] != -2:
            print(f"{spacer}if ({features[node]} <= {threshold[node]}) {{")
            if left[node] != -1:
                recurse(left, right, threshold, features, left[node], depth + 1)
            print(f"{spacer}}}\n{spacer}else {{")
            if right[node] != -1:
                recurse(left, right, threshold, features, right[node], depth + 1)
            print(f"{spacer}}}")
        else:
            target = value[node]
            for i, v in zip(np.nonzero(target)[1], target[np.nonzero(target)]):
                target_name = targets[i]
                target_count = int(v)
                print(f"{spacer}return {target_name} ({target_count} examples)")
    tree = dt.tree_
    left = tree.children_left
    right = tree.children_right
    threshold = tree.threshold
    features = [features[i] for i in tree.feature]
    value = tree.value
    recurse(left, right, threshold, features, 0, 0)
def run_decision_tree(inputfile, depth=3):
    df = load_data(inputfile)
    dt, features, targets = train_decision_tree_classifier(df, depth)
    generate_tree_code(dt, features, targets)
