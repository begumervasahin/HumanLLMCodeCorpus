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
df = pd.read_csv('fer2013.csv')
df_filtered = df[(df['emotion'] == 3) | (df['emotion'] == 4)]
emotion_counts = df_filtered['emotion'].value_counts()
happy_percentage = emotion_counts[3] / emotion_counts.sum()
sad_percentage = emotion_counts[4] / emotion_counts.sum()
print('Happy = ', happy_percentage)
print('Sad = ', sad_percentage)
usage_counts = df_filtered['Usage'].value_counts()
print("Training set:\n", df_filtered[df_filtered['Usage'] == 'Training']['emotion'].value_counts())
print("Public Test set:\n", df_filtered[df_filtered['Usage'] == 'PublicTest']['emotion'].value_counts())
print("Private Test set:\n", df_filtered[df_filtered['Usage'] == 'PrivateTest']['emotion'].value_counts())
pixels = df_filtered['pixels'].str.split(" ", expand=True).astype(int)
X = pixels.values
Y = df_filtered['emotion'].values
X_std = StandardScaler().fit_transform(X)
cov_mat = np.cov(X_std.T)
eig_vals, eig_vecs = np.linalg.eig(cov_mat)
eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:, i]) for i in range(len(eig_vals))]
eig_pairs.sort(key=lambda x: x[0], reverse=True)
var_exp = [(i / sum(eig_vals)) * 100 for i in sorted(eig_vals, reverse=True)]
cum_var_exp = np.cumsum(var_exp)
plt.figure(figsize=(10, 6))
plt.plot(cum_var_exp, label='Cumulative Explained Variance', color='goldenrod')
plt.plot(var_exp, label='Individual Explained Variance', color='black')
plt.xlabel('Feature columns')
plt.ylabel('Explained Variance')
plt.title('Explained Variance plots - Full and Zoomed-in')
plt.legend()
plt.grid(True)
plt.show()
n_components = 107
selected_eig_vecs = np.array([pair[1] for pair in eig_pairs[:n_components]])
X_projected = X_std.dot(selected_eig_vecs)
plt.figure(figsize=(8, 6))
plt.scatter(X_projected[:, 0], X_projected[:, 1], c=Y, cmap='jet', alpha=0.8)
plt.title('Principal Component Analysis (PCA)')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.colorbar()
plt.grid(True)
plt.show()
X_reconstructed = X_projected.dot(selected_eig_vecs.T)
X_reconstructed = X_reconstructed * X.std(0) + X.mean(0)
img_index = 628
img_data = X_reconstructed[img_index].reshape(48, 48).astype(np.uint8)
img = Image.fromarray(img_data)
img.show()
X_train, X_test, Y_train, Y_test = train_test_split(X_projected, Y, test_size=0.2, random_state=42)
svc = SVC()
svc.fit(X_train, Y_train)
train_score = svc.score(X_train, Y_train)
test_score = svc.score(X_test, Y_test)
print('Train Score:', train_score)
print('Test Score:', test_score)