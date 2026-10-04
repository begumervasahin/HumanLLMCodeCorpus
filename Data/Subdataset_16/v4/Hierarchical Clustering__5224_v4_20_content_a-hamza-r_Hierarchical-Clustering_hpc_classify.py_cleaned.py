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
    b1['app_name'] = b3
    return b4, b3, b2.classes_
def fonk3(y_train, b17):
    plt.figure(b5 = (10, 5))
    unique_train, b6 = np.unique(y_train, return_counts=True)
    unique_test, b7 = np.unique(b17, return_counts=True)
    plt.bar(unique_train - 0.2, b6, b8 = 0.4, label='Training set', alpha=0.6)
    plt.bar(unique_test + 0.2, b7, b8 = 0.4, label='Testing set', alpha=0.6)
    plt.title('Class Frequency Distribution')
    plt.xlabel('Class (encoded)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()
def fonk4(classifier, X_train, y_train, X_test, b17, classifier_name):
    classifier.fit(X_train, y_train)
    b9 = classifier.predict(X_test)
    b10 = set(b17) - set(b9)
    print(f"*** {classifier_name} ***")
    print("Classes not predicted:", str(b10), len(b10))
    print("F-score:", f1_score(b17, b9, b11 = 'weighted', labels=np.unique(b9)))
    print("Accuracy:", accuracy_score(b17, b9))
    del classifier
    del b9
    gc.collect()
def fonk5(classifier, b22, b14):
    b12 = classifier.estimators_[5]
    export_graphviz(b12, b13 = 'tree.dot', b22=b22,
                    b14 = b14, rounded=True, proportion=False,
                    b15 = 2, filled=True)
def fonk6(b17, b9):
    plt.figure(b5 = (10, 5))
    plt.scatter(range(len(b17)), b17, b16 = 'blue', label='Actual', alpha=0.3)
    plt.scatter(range(len(b9)), b9, b16 = 'red', label='Predicted', alpha=0.3)
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
    b4, b3, b14 = fonk2(b1)
    print("Encoded classes:", list(b14))
    X_train, X_test, y_train, b17 = train_test_split(b4, b3, test_size=0.4)
    fonk3(y_train, b17)
    b18 = {
        "KNN": KNeighborsClassifier(b19 = 5, weights='uniform', algorithm='kd_tree', leaf_size=30),
        "Naive Bayes (Gaussian)": GaussianNB(),
        "Multilayer Perceptron": MLPClassifier(b20 = (100,), activation='relu', solver='lbfgs', max_iter=200)
    }
    for name, clf in b18.items():
        fonk4(clf, X_train, y_train, X_test, b17, name)
    b21 = RandomForestClassifier(n_estimators=100, criterion='gini', class_weight='balanced')
    b21.fit(X_train, y_train)
    fonk5(b21, b22 = b1.columns[0:7], b14=b14)
    b9 = b21.predict(X_test)
    print("*** Random Forest ***")
    print("F-score:", f1_score(b17, b9, b11 = 'weighted', labels=np.unique(b9)))
    print("Accuracy:", accuracy_score(b17, b9))
    b23 = cross_val_score(b21, b4, b3, cv=5, scoring='accuracy')
    print("Cross-validated accuracy:", b23)
    fonk6(b17, b9)
    gc.collect()
if b24 = = "__main__":
    fonk7()