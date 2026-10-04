
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import sklearn as sklearn
import matplotlib.pyplot as mlt
import io
from sklearn.model_selection import train_test_split
import io
b1 = pd.read_csv("https:
b1.head()
b2 = b1.shape[0]
b2
b3 = b1.isnull().sum()
b4 = b3[b3 == 0]
b1 = b1[b4.keys()]
b1 = b1.ix[:,7:]
b5 = b1.columns
b6 = b1.ix[:,:-1].values
b7 = StandardScaler()
b8 = b7.fit_transform(b6)
b9 = b1.ix[:,-1].values
b10 = np.unique(b9)
b11 = LabelEncoder()
b9 = b11.fit_transform(b9)
b10
a1 = 0.1
x_train, x_test, y_train, b12 = train_test_split(b8, b9, test_size = a1, random_state = 0)
from sklearn.manifold import TSNE
b13 = TSNE()
b14 = TSNE(n_components = 2, random_state =0)
b15 = b14.fit_transform(x_test)
b16 = ('s', 'd', 'o', '^', 'v')
b17 = {0:'red', 1:'blue', 2:'lightgreen', 3:'purple', 4:'cyan'}
mlt.figure()
for idx, cl in enumerate(np.unique(b12)):
    mlt.scatter(b6 = b15[b12==cl,0], b9=b15[b12==cl,1], c=b17[idx], marker=b16[idx], label=cl)
mlt.xlabel('X in t-SNE')
mlt.ylabel('Y in t-SNE')
mlt.legend(b18 = 'upper left')
mlt.title('t-SNE visualization of test data')
mlt.show()
