import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
os.chdir('/Users/santanupaul/Documents/Personal/Masters in Analytics/UConn/Study Related/Python/Project/fer2013')
b1 = pd.read_csv('fer2013.csv')
b2 = b1[(b1['emotion'] == 3) | (b1['emotion'] == 4)]
b3 = b2['emotion'].value_counts()
b4 = b3[3] / b3.sum()
b5 = b3[4] / b3.sum()
print('b6 = ', b4)
print('b7 = ', b5)
b8 = b2['Usage'].value_counts()
print("Training set:\n", b2[b2['Usage'] == 'Training']['emotion'].value_counts())
print("Public Test set:\n", b2[b2['Usage'] == 'PublicTest']['emotion'].value_counts())
print("Private Test set:\n", b2[b2['Usage'] == 'PrivateTest']['emotion'].value_counts())
b9 = b2['b9'].str.split(" ", expand=True).astype(int)
b10 = b9.values
b11 = b2['emotion'].values
b12 = StandardScaler().fit_transform(b10)
b13 = np.cov(b12.T)
eig_vals, b14 = np.linalg.eig(b13)
b15 = [(np.abs(eig_vals[i]), b14[:, i]) for i in range(len(eig_vals))]
b15.sort(b16 = lambda x: x[0], reverse=True)
b17 = [(i / sum(eig_vals)) * 100 for i in sorted(eig_vals, reverse=True)]
b18 = np.cumsum(b17)
plt.figure(b19 = (10, 6))
plt.plot(b18, b20 = 'Cumulative Explained Variance', color='goldenrod')
plt.plot(b17, b20 = 'Individual Explained Variance', color='black')
plt.xlabel('Feature columns')
plt.ylabel('Explained Variance')
plt.title('Explained Variance plots - Full and Zoomed-in')
plt.legend()
plt.grid(True)
plt.show()
a1 = 107
b21 = np.array([pair[1] for pair in b15[:a1]])
b22 = b12.dot(b21)
plt.figure(b19 = (8, 6))
plt.scatter(b22[:, 0], b22[:, 1], b23 = b11, cmap='jet', alpha=0.8)
plt.title('Principal Component Analysis (PCA)')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.colorbar()
plt.grid(True)
plt.show()
b24 = b22.dot(b21.T)
b24 = b24 * b10.std(0) + b10.mean(0)
a2 = 628
b25 = b24[a2].reshape(48, 48).astype(np.uint8)
b26 = Image.fromarray(b25)
b26.show()
X_train, X_test, Y_train, b27 = train_test_split(b22, b11, test_size=0.2, random_state=42)
b28 = SVC()
b28.fit(X_train, Y_train)
b29 = b28.score(X_train, Y_train)
b30 = b28.score(X_test, b27)
print('Train Score:', b29)
print('Test Score:', b30)