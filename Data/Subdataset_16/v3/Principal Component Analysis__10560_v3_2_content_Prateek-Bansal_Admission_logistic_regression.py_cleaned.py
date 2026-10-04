import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
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
b9 = LogisticRegression(random_state=0)
b9.fit(b6, Y_train)
b10 = b9.predict(b7)
b11 = confusion_matrix(b4, b10)
print("Confusion Matrix:\n", b11)
def fonk1(X_set, b15, b9, title):
    X1, b12 = np.meshgrid(
        np.arange(b13 = X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
        np.arange(b13 = X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01)
    )
    plt.contourf(X1, b12, b9.predict(np.array([X1.ravel(), b12.ravel()]).T).reshape(X1.shape),
                 b14 = 0.75, cmap=ListedColormap(('red', 'green')))
    plt.xlim(X1.min(), X1.max())
    plt.ylim(b12.min(), b12.max())
    for i, j in enumerate(np.unique(b15)):
        plt.scatter(X_set[b15 = = j, 0], X_set[b15 == j, 1],
                    b16 = ListedColormap(('red', 'green'))(i), label=j)
    plt.title(title)
    plt.xlabel('Principal Component 1 (PC1)')
    plt.ylabel('Principal Component 2 (PC2)')
    plt.legend()
    plt.show()
fonk1(b7, b4, b9, 'Logistic Regression (Test set)')