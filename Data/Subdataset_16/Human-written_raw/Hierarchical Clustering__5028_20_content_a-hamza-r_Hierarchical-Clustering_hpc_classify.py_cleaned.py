import gc
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score
from sklearn.tree import export_graphviz
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
warnings.filterwarnings("ignore")
b1 = pd.read_csv('10k.anon.csv')
b1 = b1.sample(frac=1).reset_index(drop=True)
print(b1[:10].to_string())
print("Number of classes:", len(b1['app_name'].unique()))
print("Number of samples:", len(b1.index))
b2 = LabelEncoder()
b2.fit(b1['app_name'])
print("Encoded classes:", list(b2.classes_))
b3 = b2.transform(b1['app_name'])
b1 = b1.assign(app_name=b3)
X_train, X_test, y_train, b4 = train_test_split(b1.iloc[:, 0:7], b3, test_size=0.4)
unique, b5 = np.unique(y_train, return_counts=True)
plt.bar(unique, b5)
unique, b5 = np.unique(b4, return_counts=True)
plt.bar(unique, b5)
plt.title('Class Frequency')
plt.xlabel('Class (encoded)')
plt.ylabel('Frequency')
plt.show()
b6 = KNeighborsClassifier(n_neighbors=5, weights='uniform', algorithm='kd_tree', leaf_size=30)
b6.fit(X_train, y_train)
b7 = b6.predict(X_test)
b8 = set(b4) - set(b7)
print("*** KNN ***")
print("Classes not predicted:", str(b8), str(len(b8)))
print("F-score:", str(f1_score(b4, b7, b9 = 'weighted', labels=np.unique(b7))))
print("Accuracy:", str(accuracy_score(b4, b7)))
del b6
del b7
gc.collect()
b6 = GaussianNB()
b6.fit(X_train, y_train)
b7 = b6.predict(X_test)
b8 = set(b4) - set(b7)
print("*** Naive Bayes (Gaussian) ***")
print("Classes not predicted:", str(b8), str(len(b8)))
print("F-score:", str(f1_score(b4, b7, b9 = 'weighted', labels=np.unique(b7))))
print("Accuracy:", str(accuracy_score(b4, b7)))
del b6
del b7
gc.collect()
b6 = MLPClassifier(hidden_layer_sizes=(100,), activation='relu', solver='lbfgs', max_iter=200, shuffle=True)
b6.fit(X_train, y_train)
b7 = b6.predict(X_test)
b8 = set(b4) - set(b7)
print("*** Multilayer Perceptron ***")
print("Classes not predicted:", str(b8), str(len(b8)))
print("F-score:", str(f1_score(b4, b7, b9 = 'weighted', labels=np.unique(b7))))
print("Accuracy:", str(accuracy_score(b4, b7)))
del b6
del b7
gc.collect()
b6 = RandomForestClassifier(n_estimators=100, criterion='gini', class_weight='balanced')
b6.fit(X_train, y_train)
b10 = b6.estimators_[5]
export_graphviz(b10, b11 = 'tree.dot', feature_names=list(b1.columns[0:7]), class_names=list(b2.classes_),
	b12 = True, proportion=False, precision=2, filled=True)
b7 = b6.predict(X_test)
b8 = set(b4) - set(b7)
print("*** Random Forest ***")
print("Classes not predicted:", str(b8), str(len(b8)))
print("F-score:", str(f1_score(b4, b7, b9 = 'weighted', labels=np.unique(b7))))
print("Accuracy:", str(accuracy_score(b4, b7)))
del b6
gc.collect()
b6 = RandomForestClassifier(n_estimators=100, criterion='gini', class_weight='balanced')
b13 = cross_val_score(b6, b1.iloc[:, 0:7], b3, cv=5, scoring='accuracy')
print("Cross-validated accuracy:", b13)
_, b14 = plt.subplots()
b14.scatter(b15 = range(0, len(b4)), b3=b4, c='blue', label='Actual', alpha=0.3)
b14.scatter(b15 = range(0, len(b7)), b3=b7, c='red', label='Predicted', alpha=0.3)
plt.title('Actual and Predicted Values')
plt.xlabel('Samples')
plt.ylabel('Classes')
plt.legend()
plt.show()