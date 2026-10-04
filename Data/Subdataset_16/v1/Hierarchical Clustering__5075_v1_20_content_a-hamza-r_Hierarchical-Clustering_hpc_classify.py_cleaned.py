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
b1 = pd.read_csv('10k.anon.csv')
b1 = b1.sample(frac=1).reset_index(drop=True)
print(b1.head(10).to_string())
print("Number of classes:", len(b1['app_name'].unique()))
print("Number of samples:", len(b1))
b2 = LabelEncoder()
b3 = b2.fit_transform(b1['app_name'])
b1['app_name'] = b3
print("Encoded classes:", list(b2.classes_))
X_train, X_test, y_train, b4 = train_test_split(b1.iloc[:, 0:7], b3, test_size=0.4)
def fonk1(y_train, b4):
    unique_train, b5 = np.unique(y_train, return_counts=True)
    unique_test, b6 = np.unique(b4, return_counts=True)
    plt.bar(unique_train, b5, b7 = 0.6, label='Training set')
    plt.bar(unique_test, b6, b7 = 0.6, label='Testing set')
    plt.title('Class Frequency Distribution')
    plt.xlabel('Class (encoded)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()
fonk1(y_train, b4)
def fonk2(classifier, X_train, y_train, X_test, b4, classifier_name):
    classifier.fit(X_train, y_train)
    b8 = classifier.predict(X_test)
    b9 = set(b4) - set(b8)
    print(f"*** {classifier_name} ***")
    print("Classes not predicted:", str(b9), str(len(b9)))
    print("F-score:", f1_score(b4, b8, b10 = 'weighted', labels=np.unique(b8)))
    print("Accuracy:", accuracy_score(b4, b8))
    del classifier
    del b8
    gc.collect()
b11 = KNeighborsClassifier(n_neighbors=5, weights='uniform', algorithm='kd_tree', leaf_size=30)
fonk2(b11, X_train, y_train, X_test, b4, "KNN")
b12 = GaussianNB()
fonk2(b12, X_train, y_train, X_test, b4, "Naive Bayes (Gaussian)")
b13 = MLPClassifier(hidden_layer_sizes=(100,), activation='relu', solver='lbfgs', max_iter=200, shuffle=True)
fonk2(b13, X_train, y_train, X_test, b4, "Multilayer Perceptron")
b14 = RandomForestClassifier(n_estimators=100, criterion='gini', class_weight='balanced')
b14.fit(X_train, y_train)
export_graphviz(b14.estimators_[5], b15 = 'tree.dot', feature_names=list(b1.columns[0:7]),
                b16 = list(b2.classes_), rounded=True, proportion=False, precision=2, filled=True)
b8 = b14.predict(X_test)
b9 = set(b4) - set(b8)
print("*** Random Forest ***")
print("Classes not predicted:", str(b9), str(len(b9)))
print("F-score:", f1_score(b4, b8, b10 = 'weighted', labels=np.unique(b8)))
print("Accuracy:", accuracy_score(b4, b8))
b17 = cross_val_score(RandomForestClassifier(n_estimators=100, criterion='gini', class_weight='balanced'),
                         b1.iloc[:, 0:7], b3, b18 = 5, scoring='accuracy')
print("Cross-validated accuracy:", b17)
_, b19 = plt.subplots()
b19.scatter(b20 = range(0, len(b4)), b3=b4, c='blue', label='Actual', b7=0.3)
b19.scatter(b20 = range(0, len(b8)), b3=b8, c='red', label='Predicted', b7=0.3)
plt.title('Actual and Predicted Values')
plt.xlabel('Samples')
plt.ylabel('Classes')
plt.legend()
plt.show()
gc.collect()