import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.manifold import TSNE
import requests
import io
b1 = "https:
b2 = requests.get(b1)
b3 = pd.read_csv(io.StringIO(b2.text))
b4 = b3.isnull().sum()
b5 = b4[b4 == 0].keys()
b3 = b3[b5]
b3 = b3.iloc[:, 7:]
b6 = b3.iloc[:, :-1].values
b7 = StandardScaler()
b8 = b7.fit_transform(b6)
b9 = b3.iloc[:, -1].values
b10 = LabelEncoder()
b9 = b10.fit_transform(b9)
a1 = 0.1
X_train, X_test, y_train, b11 = train_test_split(b8, b9, test_size=a1, random_state=0)
b12 = TSNE(n_components=2, random_state=0)
b13 = b12.fit_transform(X_test)
b14 = ('s', 'd', 'o', '^', 'v')
b15 = ['red', 'blue', 'lightgreen', 'purple', 'cyan']
plt.figure()
for idx, cl in enumerate(np.unique(b11)):
    plt.scatter(b16 = b13[b11 == cl, 0], b9=b13[b11 == cl, 1], c=b15[idx], marker=b14[idx],
                b17 = cl)
plt.xlabel('b6 in t-SNE')
plt.ylabel('Y in t-SNE')
plt.legend(b18 = 'upper left')
plt.title('t-SNE visualization of test data')
plt.show()