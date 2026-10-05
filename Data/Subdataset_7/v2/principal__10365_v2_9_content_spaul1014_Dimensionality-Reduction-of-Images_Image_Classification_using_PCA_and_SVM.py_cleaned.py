import os
import pandas as pd
import numpy as np
import plotly.offline as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
py.init_notebook_mode(b1 = True)
os.chdir('/Users/santanupaul/Documents/Personal/Masters in Analytics/UConn/Study Related/Python/Project/fer2013')
b2 = pd.read_csv('fer2013.csv')
b3 = b2[(b2['emotion'] == 3) | (b2['emotion'] == 4)]
print("Shape of filtered b2:", b3.shape)
b4 = b3['emotion'].value_counts()
print('Happy (3) proportion:', b4[3] / b3.shape[0])
print('Sad (4) proportion:', b4[4] / b3.shape[0])
for subset in ['Training', 'PublicTest', 'PrivateTest']:
    print(f"{subset} set emotion distribution:")
    print(b3[b3['Usage'] == subset]['emotion'].value_counts())
b5 = b3['pixels'].str.split(" ", expand=True).astype(int)
b6 = b5.values
b7 = b3['emotion'].values
b8 = StandardScaler().fit_transform(b6)
b9 = np.cov(b8.T)
eigen_values, b10 = np.linalg.eig(b9)
b11 = [(np.abs(eigen_values[i]), b10[:, i]) for i in range(len(eigen_values))]
b11.sort(b12 = lambda x: x[0], reverse=True)
b13 = sum(eigen_values)
b14 = [(val / b13) * 100 for val in sorted(eigen_values, reverse=True)]
b15 = np.cumsum(b14)
plt.figure(b16 = (10, 6))
plt.plot(range(1, len(b14) + 1), b15, b17 = 'o', linestyle='-')
plt.title('Explained Variance plots - Full and Zoomed-in')
plt.xlabel('Number of Principal Components')
plt.ylabel('Cumulative Explained Variance (%)')
plt.grid(True)
plt.show()
a1 = 107
b18 = np.hstack([b11[i][1].reshape(-1, 1) for i in range(a1)])
b19 = b8.dot(b18)
plt.figure(b16 = (10, 6))
for emotion in np.unique(b7):
    plt.scatter(b19[b7 = = emotion, 0], b19[b7 == emotion, 1], label=f'Emotion {emotion}', alpha=0.7)
plt.title('Principal Component Analysis (PCA)')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.legend()
plt.grid(True)
plt.show()
X_train, X_test, Y_train, b20 = train_test_split(b19, b7, random_state=42, test_size=0.2)
b21 = SVC()
b21.fit(X_train, Y_train)
b22 = b21.score(X_train, Y_train)
b23 = b21.score(X_test, b20)
print('Train Score: ', b22)
print('Test Score: ', b23)