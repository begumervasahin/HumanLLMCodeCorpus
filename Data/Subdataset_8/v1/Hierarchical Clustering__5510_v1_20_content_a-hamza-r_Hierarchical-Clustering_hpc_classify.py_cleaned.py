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
df = pd.read_csv('10k.anon.csv')
df = df.sample(frac=1).reset_index(drop=True)
print(df.head(10))
print("Number of classes:", len(df['app_name'].unique()))
print("Number of samples:", len(df))
le = LabelEncoder()
df['app_name'] = le.fit_transform(df['app_name'])
print("Encoded classes:", list(le.classes_))
X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, :-1], df['app_name'], test_size=0.4)
plt.figure(figsize=(8, 6))
plt.hist([y_train, y_test], bins=len(df['app_name'].unique()), label=['Train', 'Test'])
plt.title('Class Frequency')
plt.xlabel('Class (encoded)')
plt.ylabel('Frequency')
plt.legend()
plt.show()
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print("*** KNN ***")
print("F-score:", f1_score(y_test, y_pred, average='weighted'))
print("Accuracy:", accuracy_score(y_test, y_pred))
del classifier, y_pred
gc.collect()
classifier = GaussianNB()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print("*** Naive Bayes (Gaussian) ***")
print("F-score:", f1_score(y_test, y_pred, average='weighted'))
print("Accuracy:", accuracy_score(y_test, y_pred))
del classifier, y_pred
gc.collect()
classifier = MLPClassifier(hidden_layer_sizes=(100,), max_iter=200)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print("*** Multilayer Perceptron ***")
print("F-score:", f1_score(y_test, y_pred, average='weighted'))
print("Accuracy:", accuracy_score(y_test, y_pred))
del classifier, y_pred
gc.collect()
classifier = RandomForestClassifier(n_estimators=100, class_weight='balanced')
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print("*** Random Forest ***")
print("F-score:", f1_score(y_test, y_pred, average='weighted'))
print("Accuracy:", accuracy_score(y_test, y_pred))
del classifier, y_pred
gc.collect()
classifier = RandomForestClassifier(n_estimators=100, class_weight='balanced')
scores = cross_val_score(classifier, df.iloc[:, :-1], df['app_name'], cv=5, scoring='accuracy')
print("Cross-validated accuracy:", scores)
_, ax = plt.subplots(figsize=(10, 6))
ax.scatter(range(len(y_test)), y_test, c='blue', label='Actual', alpha=0.3)
ax.scatter(range(len(y_test)), y_pred, c='red', label='Predicted', alpha=0.3)
plt.title('Actual and Predicted Values')
plt.xlabel('Samples')
plt.ylabel('Classes')
plt.legend()
plt.show()