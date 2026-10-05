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
print("Sample Data:\n", b1.head(10))
print("\nNumber of classes:", len(b1['app_name'].unique()))
print("Number of samples:", len(b1))
b2 = LabelEncoder()
b1['app_name'] = b2.fit_transform(b1['app_name'])
print("Encoded classes:", list(b2.classes_))
X_train, X_test, y_train, b3 = train_test_split(b1.iloc[:, 0:7], b1['app_name'], test_size=0.4)
plt.figure(b4 = (8, 6))
plt.hist([y_train, b3], b5 = len(b1['app_name'].unique()), label=['Train', 'Test'])
plt.title('Class Frequency')
plt.xlabel('Class (encoded)')
plt.ylabel('Frequency')
plt.legend()
plt.show()
def fonk1(classifier, X_train, y_train, X_test, b3):
    classifier.fit(X_train, y_train)
    b6 = classifier.predict(X_test)
    b7 = set(b3) - set(b6)
    b8 = f1_score(b3, b6, average='weighted', labels=np.unique(b6))
    b9 = accuracy_score(b3, b6)
    print("Classes not predicted:", str(b7), str(len(b7)))
    print("F-score:", str(b8))
    print("Accuracy:", str(b9))
    del classifier, b6
    gc.collect()
    return b8, b9
print("\n*** KNN ***")
b10 = KNeighborsClassifier(n_neighbors=5, weights='uniform', algorithm='kd_tree', leaf_size=30)
fonk1(b10, X_train, y_train, X_test, b3)
print("\n*** Naive Bayes (Gaussian) ***")
b11 = GaussianNB()
fonk1(b11, X_train, y_train, X_test, b3)
print("\n*** Multilayer Perceptron ***")
b12 = MLPClassifier(hidden_layer_sizes=(100,), activation='relu', solver='lbfgs', max_iter=200, shuffle=True)
fonk1(b12, X_train, y_train, X_test, b3)
print("\n*** Random Forest ***")
b13 = RandomForestClassifier(n_estimators=100, criterion='gini', class_weight='balanced')
b13.fit(X_train, y_train)
b14 = b13.estimators_[5]
export_graphviz(b14, b15 = 'tree.dot', feature_names=list(b1.columns[0:7]), class_names=list(b2.classes_),
                b16 = True, proportion=False, precision=2, filled=True)
fonk1(b13, X_train, y_train, X_test, b3)
del b13
gc.collect()
print("\nCross-validated b9:")
b17 = RandomForestClassifier(n_estimators=100, criterion='gini', class_weight='balanced')
b18 = cross_val_score(b17, b1.iloc[:, 0:7], b1['app_name'], cv=5, scoring='b9')
print(b18)
_, b19 = plt.subplots()
b19.scatter(b20 = range(0, len(b3)), y=b3, c='blue', label='Actual', alpha=0.3)
b19.scatter(b20 = range(0, len(b6)), y=b6, c='red', label='Predicted', alpha=0.3)
plt.title('Actual and Predicted Values')
plt.xlabel('Samples')
plt.ylabel('Classes')
plt.legend()
plt.show()