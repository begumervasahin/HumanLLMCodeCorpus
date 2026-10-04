import gc
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import export_graphviz
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import f1_score, accuracy_score
warnings.filterwarnings("ignore")
def fonk1(file_path):
    b1 = pd.read_csv(file_path)
    b1 = b1.sample(frac=1).reset_index(drop=True)
    return b1
def fonk2(b1):
    b2 = LabelEncoder()
    b3 = b2.fit_transform(b1['app_name'])
    b4 = b1.iloc[:, 0:7].values
    return b4, b3, b2.classes_
def fonk3(y_train, b14):
    unique_train, b5 = np.unique(y_train, return_counts=True)
    unique_test, b6 = np.unique(b14, return_counts=True)
    plt.bar(unique_train, b5, b7 = 0.6, label='Training set')
    plt.bar(unique_test, b6, b7 = 0.6, label='Testing set')
    plt.title('Class Frequency Distribution')
    plt.xlabel('Class (encoded)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()
def fonk4(classifier, X_train, y_train, X_test, b14, classifier_name):
    classifier.fit(X_train, y_train)
    b8 = classifier.predict(X_test)
    b9 = set(b14) - set(b8)
    print(f"*** {classifier_name} ***")
    print("Classes not predicted:", str(b9), str(len(b9)))
    print("F-score:", f1_score(b14, b8, b10 = 'weighted', labels=np.unique(b8)))
    print("Accuracy:", accuracy_score(b14, b8))
    del classifier
    del b8
    gc.collect()
def fonk5(b14, b8):
    _, b11 = plt.subplots()
    b11.scatter(range(len(b14)), b14, b12 = 'blue', label='Actual', b7=0.3)
    b11.scatter(range(len(b8)), b8, b12 = 'red', label='Predicted', b7=0.3)
    plt.title('Actual and Predicted Values')
    plt.xlabel('Samples')
    plt.ylabel('Classes')
    plt.legend()
    plt.show()
def fonk6():
    b1 = fonk1('10k.anon.csv')
    print(b1.head(10).to_string())
    print("Number of classes:", b1['app_name'].nunique())
    print("Number of samples:", len(b1))
    b4, b3, b13 = fonk2(b1)
    print("Encoded classes:", list(b13))
    X_train, X_test, y_train, b14 = train_test_split(b4, b3, test_size=0.4)
    fonk3(y_train, b14)
    b15 = {
        "KNN": KNeighborsClassifier(b16 = 5, weights='uniform', algorithm='kd_tree', leaf_size=30),
        "Naive Bayes (Gaussian)": GaussianNB(),
        "Multilayer Perceptron": MLPClassifier(b17 = (100,), activation='relu', solver='lbfgs', max_iter=200)
    }
    for name, clf in b15.items():
        fonk4(clf, X_train, y_train, X_test, b14, name)
    b18 = RandomForestClassifier(n_estimators=100, criterion='gini', class_weight='balanced')
    b18.fit(X_train, y_train)
    export_graphviz(b18.estimators_[5], b19 = 'tree.dot', feature_names=b1.columns[0:7],
                    b13 = b13, rounded=True, proportion=False, precision=2, filled=True)
    b8 = b18.predict(X_test)
    print("*** Random Forest ***")
    print("F-score:", f1_score(b14, b8, b10 = 'weighted', labels=np.unique(b8)))
    print("Accuracy:", accuracy_score(b14, b8))
    b20 = cross_val_score(b18, b4, b3, cv=5, scoring='accuracy')
    print("Cross-validated accuracy:", b20)
    fonk5(b14, b8)
    gc.collect()
if b21 = = "__main__":
    fonk6()