import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.manifold import TSNE
import requests
import io
url = "https:
response = requests.get(url)
dataframe_all = pd.read_csv(io.StringIO(response.text))
count_null = dataframe_all.isnull().sum()
columns_without_null = count_null[count_null == 0].keys()
dataframe_all = dataframe_all[columns_without_null]
dataframe_all = dataframe_all.iloc[:, 7:]
X = dataframe_all.iloc[:, :-1].values
scaler = StandardScaler()
X_std = scaler.fit_transform(X)
y = dataframe_all.iloc[:, -1].values
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)
test_percentage = 0.1
X_train, X_test, y_train, y_test = train_test_split(X_std, y, test_size=test_percentage, random_state=0)
tsne = TSNE(n_components=2, random_state=0)
X_test_2d = tsne.fit_transform(X_test)
markers = ('s', 'd', 'o', '^', 'v')
colors = ['red', 'blue', 'lightgreen', 'purple', 'cyan']
plt.figure()
for idx, cl in enumerate(np.unique(y_test)):
    plt.scatter(x=X_test_2d[y_test == cl, 0], y=X_test_2d[y_test == cl, 1], c=colors[idx], marker=markers[idx],
                label=cl)
plt.xlabel('X in t-SNE')
plt.ylabel('Y in t-SNE')
plt.legend(loc='upper left')
plt.title('t-SNE visualization of test data')
plt.show()