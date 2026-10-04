import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from matplotlib.colors import ListedColormap
b1 = pd.read_csv('iris.csv')
b2 = b1.iloc[:, :-1].values
b3 = b1.iloc[:, -1].values
b4 = LabelEncoder()
b3 = b4.fit_transform(b3)
b7, b8, y_train, b5 = train_test_split(b2, b3, test_size=0.3, random_state=0)
b6 = StandardScaler()
b7 = b6.fit_transform(b7)
b8 = b6.transform(b8)
b9 = PCA(n_components=2)
b7 = b9.fit_transform(b7)
b8 = b9.transform(b8)
b10 = b9.explained_variance_ratio_
b11 = DecisionTreeClassifier(criterion='entropy', random_state=0)
b11.fit(b7, y_train)
b12 = b11.predict(b8)
b13 = confusion_matrix(b5, b12)
def fonk1(X_set, b17, b11, title):
    X1, b14 = np.meshgrid(np.arange(b15=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
                         np.arange(b15 = X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01))
    plt.contourf(X1, b14, b11.predict(np.array([X1.ravel(), b14.ravel()]).T).reshape(X1.shape),
                 b16 = 0.75, cmap=ListedColormap(('red', 'green', 'blue')))
    plt.xlim(X1.min(), X1.max())
    plt.ylim(b14.min(), b14.max())
    for i, j in enumerate(np.unique(b17)):
        plt.scatter(X_set[b17 = = j, 0], X_set[b17 == j, 1],
                    b18 = ListedColormap(('red', 'green', 'blue'))(i), label=j)
    plt.title(title)
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.legend()
    plt.show()
fonk1(b7, y_train, b11, 'Decision Tree Classifier (Training set)')
fonk1(b8, b5, b11, 'Decision Tree Classifier (Test set)')