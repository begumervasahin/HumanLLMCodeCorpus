import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from matplotlib.colors import ListedColormap
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2(b21):
    b1 = b21.iloc[:, :-1].values
    b2 = b21.iloc[:, -1].values
    b2 = LabelEncoder().fit_transform(b2)
    X_train, X_test, y_train, b3 = train_test_split(b1, b2, test_size=0.3, random_state=0)
    return X_train, X_test, y_train, b3
def fonk3(X_train, X_test):
    b4 = StandardScaler()
    b5 = b4.fit_transform(X_train)
    b6 = b4.transform(X_test)
    return b5, b6
def fonk4(X_train, X_test, b7 = 2):
    b8 = PCA(b7=b7)
    b9 = b8.fit_transform(X_train)
    b10 = b8.transform(X_test)
    b11 = b8.explained_variance_ratio_
    return b9, b10, b11
def fonk5(X_train, y_train):
    b12 = DecisionTreeClassifier(criterion='entropy', random_state=0)
    b12.fit(X_train, y_train)
    return b12
def fonk6(b12, X_test, b3):
    b13 = b12.predict(X_test)
    b14 = confusion_matrix(b3, b13)
    return b14
def fonk7(X_set, b18, b12, title):
    X1, b15 = np.meshgrid(np.arange(b16=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
                         np.arange(b16 = X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01))
    plt.contourf(X1, b15, b12.predict(np.array([X1.ravel(), b15.ravel()]).T).reshape(X1.shape),
                 b17 = 0.75, cmap=ListedColormap(('red', 'green', 'blue')))
    plt.xlim(X1.min(), X1.max())
    plt.ylim(b15.min(), b15.max())
    for i, j in enumerate(np.unique(b18)):
        plt.scatter(X_set[b18 = = j, 0], X_set[b18 == j, 1],
                    b19 = ListedColormap(('red', 'green', 'blue'))(i), label=j)
    plt.title(title)
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.legend()
    plt.show()
if b20 = = "__main__":
    b21 = fonk1('iris.csv')
    X_train, X_test, y_train, b3 = fonk2(b21)
    b5, b6 = fonk3(X_train, X_test)
    b9, b10, b11 = fonk4(b5, b6)
    b12 = fonk5(b9, y_train)
    b14 = fonk6(b12, b10, b3)
    print("Confusion Matrix:\n", b14)
    fonk7(b9, y_train, b12, 'Decision Tree Classifier (Training set)')
    fonk7(b10, b3, b12, 'Decision Tree Classifier (Test set)')