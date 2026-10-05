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
py.init_notebook_mode(connected=True)
dataset_dir = '/Users/santanupaul/Documents/Personal/Masters in Analytics/UConn/Study Related/Python/Project/fer2013'
dataset = pd.read_csv(os.path.join(dataset_dir, 'fer2013.csv'))
filtered_dataset = dataset[(dataset['emotion'] == 3) | (dataset['emotion'] == 4)]
print("Shape of filtered dataset:", filtered_dataset.shape)
happy_proportion = filtered_dataset['emotion'].value_counts(normalize=True)[3]
sad_proportion = filtered_dataset['emotion'].value_counts(normalize=True)[4]
print('Proportion of Happy (3) emotion:', happy_proportion)
print('Proportion of Sad (4) emotion:', sad_proportion)
for subset in ['Training', 'PublicTest', 'PrivateTest']:
    subset_emotions = filtered_dataset[filtered_dataset['Usage'] == subset]['emotion'].value_counts()
    print(f"{subset} set emotion distribution:")
    print(subset_emotions)
pixels_data = filtered_dataset['pixels'].str.split(" ", expand=True).astype(int)
X = pixels_data.values
Y = filtered_dataset['emotion'].values
X_std = StandardScaler().fit_transform(X)
pca = PCA(n_components=107)
X_pca = pca.fit_transform(X_std)
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(pca.explained_variance_ratio_) + 1), np.cumsum(pca.explained_variance_ratio_), marker='o', linestyle='-')
plt.title('Cumulative Explained Variance by Principal Components')
plt.xlabel('Number of Principal Components')
plt.ylabel('Cumulative Explained Variance (%)')
plt.grid(True)
plt.show()
plt.figure(figsize=(10, 6))
for emotion in np.unique(Y):
    plt.scatter(X_pca[Y == emotion, 0], X_pca[Y == emotion, 1], label=f'Emotion {emotion}', alpha=0.7)
plt.title('Principal Component Analysis (PCA)')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.legend()
plt.grid(True)
plt.show()
X_train, X_test, Y_train, Y_test = train_test_split(X_pca, Y, random_state=42, test_size=0.2)
svm_classifier = SVC()
svm_classifier.fit(X_train, Y_train)
train_score = svm_classifier.score(X_train, Y_train)
test_score = svm_classifier.score(X_test, Y_test)
print('Train Score: ', train_score)
print('Test Score: ', test_score)