import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.manifold import TSNE
import io
import requests
url = "https:
response = requests.get(url)
dataframe_all = pd.read_csv(io.StringIO(response.text))
count_null = dataframe_all.isnull().sum()
counter_without_null = count_null[count_null == 0]
dataframe_all = dataframe_all[counter_without_null.keys()]
dataframe_all = dataframe_all.iloc[:, 7:]
x = dataframe_all.iloc[:, :-1].values
standard_scaler = StandardScaler()
x_std = standard_scaler.fit_transform(x)
y = dataframe_all.iloc[:, -1].values
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)
test_percentage = 0.1
x_train, x_test, y_train, y_test = train_test_split(x_std, y, test_size=test_percentage, random_state=0)
tsne = TSNE(n_components=2, random_state=0)
x_test_2d = tsne.fit_transform(x_test)
markers = ('s', 'd', 'o', '^', 'v')
color_map = {0: 'red', 1: 'blue', 2: 'lightgreen', 3: 'purple', 4: 'cyan'}
plt.figure()
for idx, cl in enumerate(np.unique(y_test)):
    plt.scatter(x=x_test_2d[y_test == cl, 0], y=x_test_2d[y_test == cl, 1], c=color_map[idx], marker=markers[idx],
                label=cl)
plt.xlabel('X in t-SNE')
plt.ylabel('Y in t-SNE')
plt.legend(loc='upper left')
plt.title('t-SNE visualization of test data')
plt.show()