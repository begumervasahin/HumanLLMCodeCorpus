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
    print("Sample Data:\n", b1.head(10))
    print("\nNumber of classes:", len(b1['app_name'].unique()))
    print("Number of samples:", len(b1))
    b2 = LabelEncoder()
    b1['app_name'] = b2.fit_transform(b1['app_name'])
    print("Encoded classes:", list(b2.classes_))
    return b1, b2
def fonk2(y_train, b9):
    plt.figure(b3 = (8, 6))
    plt.hist([y_train, b9], b4 = len(np.unique(y_train)), label=['Train', 'Test'])
    plt.title('Class Frequency')
    plt.xlabel('Class (encoded)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()
def fonk3(classifier, X_train, y_train, X_test, b9):
    classifier.fit(X_train, y_train)
    b5 = classifier.predict(X_test)
    b6 = set(b9) - set(b5)
    b7 = f1_score(b9, b5, average='weighted', labels=np.unique(b5))
    b8 = accuracy_score(b9, b5)
    print("Classes not predicted:", str(b6), str(len(b6)))
    print("F-score:", str(b7))
    print("Accuracy:", str(b8))
    del classifier, b5
    gc.collect()
    return b7, b8
b1, b2 = fonk1('10k.anon.csv')
X_train, X_test, y_train, b9 = train_test_split(b1.iloc[:, :-1], b1['app_name'], test_size=0.4)
fonk2(y_train, b9)
print("\n*** KNN ***")
b10 = KNeighborsClassifier(n_neighbors=5, weights='uniform', algorithm='kd_tree', leaf_size=30)
fonk3(b10, X_train, y_train, X_test, b9)
print("\n*** Naive Bayes (Gaussian) ***")
b11 = GaussianNB()
fonk3(b11, X_train, y_train, X_test, b9)
print("\n*** Multilayer Perceptron ***")
b12 = MLPClassifier(hidden_layer_sizes=(100,), activation='relu', solver='lbfgs', max_iter=200, shuffle=True)
fonk3(b12, X_train, y_train, X_test, b9)
print("\n*** Random Forest ***")
b13 = RandomForestClassifier(n_estimators=100, criterion='gini', class_weight='balanced')
rf_f_score, b14 = fonk3(b13, X_train, y_train, X_test, b9)
del b13
gc.collect()
print("\nCross-validated b8:")
b15 = RandomForestClassifier(n_estimators=100, criterion='gini', class_weight='balanced')
b16 = cross_val_score(b15, b1.iloc[:, :-1], b1['app_name'], cv=5, scoring='b8')
print(b16)