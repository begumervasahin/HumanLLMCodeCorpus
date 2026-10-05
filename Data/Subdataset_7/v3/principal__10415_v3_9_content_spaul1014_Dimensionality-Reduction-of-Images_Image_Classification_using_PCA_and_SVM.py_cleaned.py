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
b2 = '/Users/santanupaul/Documents/Personal/Masters in Analytics/UConn/Study Related/Python/Project/fer2013'
b3 = pd.read_csv(os.path.join(b2, 'fer2013.csv'))
b4 = b3[(b3['emotion'] == 3) | (b3['emotion'] == 4)]
print("Shape of filtered b3:", b4.shape)
b5 = b4['emotion'].value_counts(normalize=True)[3]
b6 = b4['emotion'].value_counts(normalize=True)[4]
print('Proportion of Happy (3) emotion:', b5)
print('Proportion of Sad (4) emotion:', b6)
for subset in ['Training', 'PublicTest', 'PrivateTest']:
    b7 = b4[b4['Usage'] == subset]['emotion'].value_counts()
    print(f"{subset} set emotion distribution:")
    print(b7)
b8 = b4['pixels'].str.split(" ", expand=True).astype(int)
b9 = b8.values
b10 = b4['emotion'].values
b11 = StandardScaler().fit_transform(b9)
b12 = PCA(n_components=107)
b13 = b12.fit_transform(b11)
plt.figure(b14 = (10, 6))
plt.plot(range(1, len(b12.explained_variance_ratio_) + 1), np.cumsum(b12.explained_variance_ratio_), b15 = 'o', linestyle='-')
plt.title('Cumulative Explained Variance by Principal Components')
plt.xlabel('Number of Principal Components')
plt.ylabel('Cumulative Explained Variance (%)')
plt.grid(True)
plt.show()
plt.figure(b14 = (10, 6))
for emotion in np.unique(b10):
    plt.scatter(b13[b10 = = emotion, 0], b13[b10 == emotion, 1], label=f'Emotion {emotion}', alpha=0.7)
plt.title('Principal Component Analysis (PCA)')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.legend()
plt.grid(True)
plt.show()
X_train, X_test, Y_train, b16 = train_test_split(b13, b10, random_state=42, test_size=0.2)
b17 = SVC()
b17.fit(X_train, Y_train)
b18 = b17.score(X_train, Y_train)
b19 = b17.score(X_test, b16)
print('Train Score: ', b18)
print('Test Score: ', b19)