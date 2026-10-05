import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
b1 = '/Users/santanupaul/Documents/Personal/Masters in Analytics/UConn/Study Related/Python/Project/fer2013'
os.chdir(b1)
b2 = pd.read_csv('fer2013.csv')
b3 = b2[b2['emotion'].isin([3, 4])]
b4 = b3['emotion'].value_counts()
b5 = b4[3] / b4.sum()
b6 = b4[4] / b4.sum()
print('Happy Percentage:', b5)
print('Sad Percentage:', b6)
b7 = b3['Usage'].value_counts()
print("Training set:\n", b3[b3['Usage'] == 'Training']['emotion'].value_counts())
print("Public Test set:\n", b3[b3['Usage'] == 'PublicTest']['emotion'].value_counts())
print("Private Test set:\n", b3[b3['Usage'] == 'PrivateTest']['emotion'].value_counts())
b8 = b3['b8'].str.split(" ", expand=True).astype(int)
b9 = b8.values
b10 = b3['emotion'].values
b11 = StandardScaler().fit_transform(b9)
b12 = np.cov(b11.T)
eig_vals, b13 = np.linalg.eig(b12)
b14 = sorted([(np.abs(eig_vals[i]), b13[:, i]) for i in range(len(eig_vals))], reverse=True, key=lambda x: x[0])
b15 = [(i / sum(eig_vals)) * 100 for i in sorted(eig_vals, reverse=True)]
b16 = np.cumsum(b15)
plt.figure(b17 = (10, 6))
plt.plot(b16, b18 = 'Cumulative Explained Variance', color='goldenrod')
plt.plot(b15, b18 = 'Individual Explained Variance', color='black')
plt.xlabel('Feature Columns')
plt.ylabel('Explained Variance (%)')
plt.title('Explained Variance Plots - Full and Zoomed-in')
plt.legend()
plt.grid(True)
plt.show()
a1 = 107
b19 = np.array([pair[1] for pair in b14[:a1]])
b20 = b11.dot(b19)
plt.figure(b17 = (8, 6))
plt.scatter(b20[:, 0], b20[:, 1], b21 = b10, cmap='jet', alpha=0.8)
plt.title('Principal Component Analysis (PCA)')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.colorbar(b18 = 'Emotion')
plt.grid(True)
plt.show()
b22 = b20.dot(b19.T)
b22 = b22 * b9.std(0) + b9.mean(0)
a2 = 628
b23 = b22[a2].reshape(48, 48).astype(np.uint8)
b24 = Image.fromarray(b23)
b24.show()
X_train, X_test, Y_train, b25 = train_test_split(b20, b10, test_size=0.2, random_state=42)
b26 = SVC()
b26.fit(X_train, Y_train)
b27 = b26.score(X_train, Y_train)
b28 = b26.score(X_test, b25)
print('Train Score:', b27)
print('Test Score:', b28)