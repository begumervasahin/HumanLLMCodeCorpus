import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from matplotlib.colors import ListedColormap
b1 = pd.read_csv('Admission_Predict.csv')
b2 = b1.iloc[:, 1:8].values
b3 = b1.iloc[:, 8].values
b3 = np.where(b3 >= 0.5, 1, 0)
b6, b7, Y_train, b4 = train_test_split(b2, b3, test_size=0.2, random_state=0)
b5 = StandardScaler()
b6 = b5.fit_transform(b6)
b7 = b5.transform(b7)
b8 = PCA(n_components=2)
b6 = b8.fit_transform(b6)
b7 = b8.transform(b7)
b9 = b8.explained_variance_ratio_
b10 = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
b10.fit(b6, Y_train)
b11 = b10.predict(b7)
b12 = confusion_matrix(b4, b11)
X_set, b13 = b7, b4
X1, b14 = np.meshgrid(np.arange(b15=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
                     np.arange(b15 = X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01))
plt.contourf(X1, b14, b10.predict(np.array([X1.ravel(), b14.ravel()]).T).reshape(X1.shape),
             b16 = 0.75, cmap=ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(b14.min(), b14.max())
for i, label in enumerate(np.unique(b13)):
    plt.scatter(X_set[b13 = = label, 0], X_set[b13 == label, 1],
                b17 = ListedColormap(('red', 'green'))(i), label=label)
plt.title('KNN Classification (Test set)')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()
plt.show()