import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.manifold import TSNE
import io
import requests
b1 = "https:
b2 = requests.get(b1)
b3 = pd.read_csv(io.StringIO(b2.text))
b4 = b3.isnull().sum()
b5 = b4[b4 == 0].index
b6 = b3[b5].iloc[:, 7:]
b7 = b6.iloc[:, :-1].values
b8 = StandardScaler()
b9 = b8.fit_transform(b7)
b10 = b6.iloc[:, -1].values
b11 = LabelEncoder()
b12 = b11.fit_transform(b10)
a1 = 0.1
X_train, X_test, y_train, b13 = train_test_split(b9, b12, test_size=a1, random_state=0)
b14 = TSNE(n_components=2, random_state=0)
b15 = b14.fit_transform(X_test)
b16 = ('s', 'd', 'o', '^', 'v')
b17 = ['red', 'blue', 'lightgreen', 'purple', 'cyan']
plt.figure()
for idx, cl in enumerate(np.unique(b13)):
    plt.scatter(b18 = b15[b13 == cl, 0], b10=b15[b13 == cl, 1], c=b17[idx], marker=b16[idx],
                b19 = cl)
plt.xlabel('b7 in t-SNE')
plt.ylabel('Y in t-SNE')
plt.legend(b20 = 'upper left')
plt.title('t-SNE visualization of test data')
plt.show()