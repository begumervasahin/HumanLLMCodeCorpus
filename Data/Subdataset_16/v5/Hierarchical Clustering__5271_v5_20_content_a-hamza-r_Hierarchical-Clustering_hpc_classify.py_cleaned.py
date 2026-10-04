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
def fonk2(b1, b2 = 'app_name'):
    b3 = LabelEncoder()
    b4 = b3.fit_transform(b1[b2])
    b5 = b1.iloc[:, 0:7].values
    b1[b2] = b4
    return b5, b4, b3.classes_
def fonk3(y_train, b18):
    plt.figure(b6 = (10, 5))
    unique_train, b7 = np.unique(y_train, return_counts=True)
    unique_test, b8 = np.unique(b18, return_counts=True)
    plt.bar(unique_train - 0.2, b7, b9 = 0.4, label='Training set', alpha=0.6)
    plt.bar(unique_test + 0.2, b8, b9 = 0.4, label='Testing set', alpha=0.6)
    plt.title('Class Frequency Distribution')
    plt.xlabel('Class (encoded)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()
def fonk4(classifier, X_train, y_train, X_test, b18, classifier_name):
    classifier.fit(X_train, y_train)
    b10 = classifier.predict(X_test)
    b11 = set(b18) - set(b10)
    print(f"*** {classifier_name} ***")
    print("Classes not predicted:", str(b11), len(b11))
    print("F-score:", f1_score(b18, b10, b12 = 'weighted', labels=np.unique(b10)))
    print("Accuracy:", accuracy_score(b18, b10))
    del classifier
    del b10
    gc.collect()
def fonk5(classifier, b23, b15):
    b13 = classifier.estimators_[5]
    export_graphviz(b13, b14 = 'tree.dot', b23=b23,
                    b15 = b15, rounded=True, proportion=False,
                    b16 = 2, filled=True)
def fonk6(b18, b10):
    plt.figure(b6 = (10, 5))
    plt.scatter(range(len(b18)), b18, b17 = 'blue', label='Actual', alpha=0.3)
    plt.scatter(range(len(b10)), b10, b17 = 'red', label='Predicted', alpha=0.3)
    plt.title('Actual and Predicted Values')
    plt.xlabel('Samples')
    plt.ylabel('Classes')
    plt.legend()
    plt.show()
def fonk7():
    b1 = fonk1('10k.anon.csv')
    print(b1.head(10).to_string())
    print(f"Number of classes: {b1['app_name'].nunique()}")
    print(f"Number of samples: {len(b1)}")
    b5, b4, b15 = fonk2(b1)
    print("Encoded classes:", list(b15))
    X_train, X_test, y_train, b18 = train_test_split(b5, b4, test_size=0.4)
    fonk3(y_train, b18)
    b19 = {
        "KNN": KNeighborsClassifier(b20 = 5, weights='uniform', algorithm='kd_tree', leaf_size=30),
        "Naive Bayes (Gaussian)": GaussianNB(),
        "Multilayer Perceptron": MLPClassifier(b21 = (100,), activation='relu', solver='lbfgs', max_iter=200)
    }
    for name, clf in b19.items():
        fonk4(clf, X_train, y_train, X_test, b18, name)
    b22 = RandomForestClassifier(n_estimators=100, criterion='gini', class_weight='balanced')
    b22.fit(X_train, y_train)
    fonk5(b22, b23 = b1.columns[0:7], b15=b15)
    b10 = b22.predict(X_test)
    print("*** Random Forest ***")
    print("F-score:", f1_score(b18, b10, b12 = 'weighted', labels=np.unique(b10)))
    print("Accuracy:", accuracy_score(b18, b10))
    b24 = cross_val_score(b22, b5, b4, cv=5, scoring='accuracy')
    print("Cross-validated accuracy:", b24)
    fonk6(b18, b10)
    gc.collect()
if b25 = = "__main__":
    fonk7()