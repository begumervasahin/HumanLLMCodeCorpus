
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
b1 = pd.read_csv('iris.csv')
b2 = b1.iloc[:,:-1].values
b3 = b1.iloc[:,-1].values
from sklearn.preprocessing import LabelEncoder
b4 = LabelEncoder()
b3 = b4.fit_transform(b3)
from sklearn.cross_validation import train_test_split
b7,b8,y_train,b5 = train_test_split(b2,b3,test_size=0.3,random_state=0)
from sklearn.preprocessing import StandardScaler
b6 = StandardScaler()
b7 = b6.fit_transform(b7)
b8 = b6.fit_transform(b8)
from sklearn.decomposition import PCA
b9 = PCA(n_components = 2)
b7 = b9.fit_transform(b7)
b8 = b9.transform(b8)
b10 = b9.explained_variance_ratio_
from sklearn.tree import DecisionTreeClassifier
b11 = DecisionTreeClassifier(criterion='entropy',random_state=0)
b11.fit(b7,y_train)
b12 = b11.predict(b8)
from sklearn.metrics import confusion_matrix
b13 = confusion_matrix(b5, b12)
from matplotlib.colors import ListedColormap
X_set, b14 = b7, y_train
X1, b15 = np.meshgrid(np.arange(b16 = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(b16 = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, b15, b11.predict(np.array([X1.ravel(), b15.ravel()]).T).reshape(X1.shape),
             b17 = 0.75, cmap = ListedColormap(('red', 'green', 'blue')))
plt.xlim(X1.min(), X1.max())
plt.ylim(b15.min(), b15.max())
for i, j in enumerate(np.unique(b14)):
    plt.scatter(X_set[b14 = = j, 0], X_set[b14 == j, 1],
                b18 = ListedColormap(('red', 'green', 'blue'))(i), label = j)
plt.title('Logistic Regression (Training set)')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.legend()
plt.show()
from matplotlib.colors import ListedColormap
X_set, b14 = b8, b5
X1, b15 = np.meshgrid(np.arange(b16 = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(b16 = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, b15, b11.predict(np.array([X1.ravel(), b15.ravel()]).T).reshape(X1.shape),
             b17 = 0.75, cmap = ListedColormap(('red', 'green', 'blue')))
plt.xlim(X1.min(), X1.max())
plt.ylim(b15.min(), b15.max())
for i, j in enumerate(np.unique(b14)):
    plt.scatter(X_set[b14 = = j, 0], X_set[b14 == j, 1],
                b18 = ListedColormap(('red', 'green', 'blue'))(i), label = j)
plt.title('Logistic Regression (Test set)')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.legend()
plt.show()