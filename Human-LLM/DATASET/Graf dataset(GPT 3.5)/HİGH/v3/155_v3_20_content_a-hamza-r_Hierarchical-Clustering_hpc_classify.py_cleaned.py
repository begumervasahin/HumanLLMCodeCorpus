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
X_train, X_test, y_train, b3 = train_test_split(b1.iloc[:, :-1], b1['app_name'], test_size=0.4)
plt.figure(b4 = (8, 6))
plt.hist([y_train, b3], b5 = len(b1['app_name'].unique()), label=['Train', 'Test'])
plt.title('Class Frequency')
plt.xlabel('Class (encoded)')
plt.ylabel('Frequency')
plt.legend()
plt.show()
def fonk1(b14, X_train, y_train, X_test, b3):
    b14.fit(X_train, y_train)
    b6 = b14.predict(X_test)
    b7 = f1_score(b3, b6, average='weighted')
    b8 = accuracy_score(b3, b6)
    print("F-score:", b7)
    print("Accuracy:", b8)
    del b14, b6
    gc.collect()
    return b7, b8
b9 = {
    "KNN": KNeighborsClassifier(b10 = 5),
    "Naive Bayes (Gaussian)": GaussianNB(),
    "Multilayer Perceptron": MLPClassifier(b11 = (100,), max_iter=200),
    "Random Forest": RandomForestClassifier(b12 = 100, class_weight='balanced')
}
b13 = {}
for name, b14 in b9.items():
    print("\n***", name, "***")
    b7, b8 = fonk1(b14, X_train, y_train, X_test, b3)
    b13[name] = {"F-score": b7, "Accuracy": b8}
b14 = RandomForestClassifier(b12=100, class_weight='balanced')
b15 = cross_val_score(b14, b1.iloc[:, :-1], b1['app_name'], cv=5, scoring='b8')
print("\nCross-validated b8:", b15)
_, b16 = plt.subplots(b4=(10, 6))
b16.scatter(range(len(b3)), b3, b17 = 'blue', label='Actual', alpha=0.3)
b16.scatter(range(len(b3)), b6, b17 = 'red', label='Predicted', alpha=0.3)
plt.title('Actual and Predicted Values')
plt.xlabel('Samples')
plt.ylabel('Classes')
plt.legend()
plt.show()