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
print(b1.head(10))
print("Number of classes:", len(b1['app_name'].unique()))
print("Number of samples:", len(b1))
b2 = LabelEncoder()
b1['app_name'] = b2.fit_transform(b1['app_name'])
print("Encoded classes:", list(b2.classes_))
X_train, X_test, y_train, b3 = train_test_split(b1.iloc[:, :-1], b1['app_name'], test_size=0.4)
plt.figure(b4 = (8, 6))
plt.hist([y_train, b3], b5 = len(b1['app_name'].unique()), label=['Train', 'Test'])
plt.title('Class Frequency')
plt.xlabel('Class (encoded)')
plt.ylabel('Frequency')
plt.legend()
plt.show()
b6 = KNeighborsClassifier(n_neighbors=5)
b6.fit(X_train, y_train)
b7 = b6.predict(X_test)
print("*** KNN ***")
print("F-score:", f1_score(b3, b7, b8 = 'weighted'))
print("Accuracy:", accuracy_score(b3, b7))
del b6, b7
gc.collect()
b6 = GaussianNB()
b6.fit(X_train, y_train)
b7 = b6.predict(X_test)
print("*** Naive Bayes (Gaussian) ***")
print("F-score:", f1_score(b3, b7, b8 = 'weighted'))
print("Accuracy:", accuracy_score(b3, b7))
del b6, b7
gc.collect()
b6 = MLPClassifier(hidden_layer_sizes=(100,), max_iter=200)
b6.fit(X_train, y_train)
b7 = b6.predict(X_test)
print("*** Multilayer Perceptron ***")
print("F-score:", f1_score(b3, b7, b8 = 'weighted'))
print("Accuracy:", accuracy_score(b3, b7))
del b6, b7
gc.collect()
b6 = RandomForestClassifier(n_estimators=100, class_weight='balanced')
b6.fit(X_train, y_train)
b7 = b6.predict(X_test)
print("*** Random Forest ***")
print("F-score:", f1_score(b3, b7, b8 = 'weighted'))
print("Accuracy:", accuracy_score(b3, b7))
del b6, b7
gc.collect()
b6 = RandomForestClassifier(n_estimators=100, class_weight='balanced')
b9 = cross_val_score(b6, b1.iloc[:, :-1], b1['app_name'], cv=5, scoring='accuracy')
print("Cross-validated accuracy:", b9)
_, b10 = plt.subplots(b4=(10, 6))
b10.scatter(range(len(b3)), b3, b11 = 'blue', label='Actual', alpha=0.3)
b10.scatter(range(len(b3)), b7, b11 = 'red', label='Predicted', alpha=0.3)
plt.title('Actual and Predicted Values')
plt.xlabel('Samples')
plt.ylabel('Classes')
plt.legend()
plt.show()