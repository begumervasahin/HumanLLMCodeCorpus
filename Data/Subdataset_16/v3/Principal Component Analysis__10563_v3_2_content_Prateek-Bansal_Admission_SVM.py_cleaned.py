import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
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
b9 = b8.fit_transform(b6)
b10 = b8.transform(b7)
b11 = b8.explained_variance_ratio_
b12 = SVC(kernel='linear', random_state=0)
b12.fit(b9, Y_train)
b13 = b12.predict(b10)
b14 = confusion_matrix(b4, b13)
print("Confusion Matrix:")
print(b14)
def fonk1(b2, b18, b12, title):
    X1, b15 = np.meshgrid(
        np.arange(b16 = b2[:, 0].min() - 1, stop=b2[:, 0].max() + 1, step=0.01),
        np.arange(b16 = b2[:, 1].min() - 1, stop=b2[:, 1].max() + 1, step=0.01)
    )
    plt.contourf(
        X1, b15, b12.predict(np.array([X1.ravel(), b15.ravel()]).T).reshape(X1.shape),
        b17 = 0.75, cmap=ListedColormap(('red', 'green'))
    )
    plt.xlim(X1.min(), X1.max())
    plt.ylim(b15.min(), b15.max())
    for i, j in enumerate(np.unique(b18)):
        plt.scatter(b2[b18 = = j, 0], b2[b18 == j, 1],
                    b19 = ListedColormap(('red', 'green'))(i), label=j)
    plt.title(title)
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend()
    plt.show()
fonk1(b10, b4, b12, 'SVM (Test set)')