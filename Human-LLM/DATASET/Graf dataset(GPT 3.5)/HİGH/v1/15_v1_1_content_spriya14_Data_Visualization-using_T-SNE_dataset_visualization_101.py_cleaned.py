import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.manifold import TSNE
import io
import requests
b1 = "https:
b2 = requests.get(b1)
b3 = pd.read_csv(io.StringIO(b2.text))
b4 = b3.isnull().sum()
b5 = b4[b4 == 0]
b3 = b3[b5.keys()]
b3 = b3.iloc[:, 7:]
b6 = b3.iloc[:, :-1].values
b7 = StandardScaler()
b8 = b7.fit_transform(b6)
b9 = b3.iloc[:, -1].values
b10 = LabelEncoder()
b9 = b10.fit_transform(b9)
a1 = 0.1
x_train, x_test, y_train, b11 = train_test_split(b8, b9, test_size=a1, random_state=0)
b12 = TSNE(n_components=2, random_state=0)
b13 = b12.fit_transform(x_test)
b14 = ('s', 'd', 'o', '^', 'v')
b15 = {0: 'red', 1: 'blue', 2: 'lightgreen', 3: 'purple', 4: 'cyan'}
plt.figure()
for idx, cl in enumerate(np.unique(b11)):
    plt.scatter(b6 = b13[b11 == cl, 0], b9=b13[b11 == cl, 1], c=b15[idx], marker=b14[idx],
                b16 = cl)
plt.xlabel('X in t-SNE')
plt.ylabel('Y in t-SNE')
plt.legend(b17 = 'upper left')
plt.title('t-SNE visualization of test data')
plt.show()