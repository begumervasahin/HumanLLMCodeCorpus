import os
import pandas as pd
import numpy as np
from PIL import Image
import plotly.offline as py
import plotly.graph_objs as go
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
py.init_notebook_mode(b1 = True)
os.chdir('/Users/santanupaul/Documents/Personal/Masters in Analytics/UConn/Study Related/Python/Project/fer2013')
b2 = pd.read_csv('fer2013.csv')
b3 = b2[(b2['emotion'] == 3) | (b2['emotion'] == 4)]
print(b3.b27)
b4 = b3.emotion.value_counts()
print('b5 = ', b4[3]/(b4[3]+b4[4]))
print('b6 = ', b4[4]/(b4[3]+b4[4]))
print(b3[b3['Usage'] == 'Training'].groupby(['emotion']).agg({'emotion': 'count'}))
print(b3[b3['Usage'] == 'PublicTest'].groupby(['emotion']).agg({'emotion': 'count'}))
print(b3[b3['Usage'] == 'PrivateTest'].groupby(['emotion']).agg({'emotion': 'count'}))
b3 = pd.concat([b3[['emotion']], b3['pixels'].str.split(" ", expand=True)], axis=1)
b7 = b3.iloc[:, 1:].values
b8 = b3.iloc[:, 0].values
b7 = b7.astype(int)
b9 = StandardScaler().fit_transform(b7)
b10 = b7.mean(0)
b11 = b7.std(0)
b12 = np.mean(b9, axis=0)
b13 = (b9 - b12).T.dot((b9 - b12)) / (b9.b27[0]-1)
eig_vals, b14 = np.linalg.eig(b13)
b15 = [(np.abs(eig_vals[i]), b14[:, i]) for i in range(len(eig_vals))]
b15.sort(b16 = lambda b21: b21[0], reverse=True)
b17 = sum(eig_vals)
b18 = [(i/b17)*100 for i in sorted(eig_vals, reverse=True)]
b19 = np.cumsum(b18)
b20 = go.Scatter(
    b21 = list(range(784)),
    b22 = b19,
    b23 = 'lines+markers',
    b24 = "'Cumulative Explained Variance'",
    b25 = b19,
    b26 = dict(
        b27 = 'spline',
        b28 = 'goldenrod'
    )
)
b29 = go.Scatter(
    b21 = list(range(784)),
    b22 = b18,
    b23 = 'lines+markers',
    b24 = "'Individual Explained Variance'",
    b25 = b18,
    b26 = dict(
        b27 = 'linear',
        b28 = 'black'
    )
)
b30 = go.Figure(b49=[b20, b29])
b30.update_layout(
    b31 = 'Explained Variance plots - Full and Zoomed-in',
    b32 = dict(range=[0, 80], b31='Feature columns'),
    b33 = dict(range=[0, 60], b31='Explained Variance')
)
py.iplot(b30, b34 = 'explained-variance')
a1 = 107
b35 = b15[0][1].reshape(len(b14), 1)
for i in range(1, a1):
    b35 = np.hstack((b35, b15[i][1].reshape(len(b14), 1)))
b36 = b9.dot(b35)
a2 = 4
a3 = 7
plt.figure(b37 = (11, 8))
for i in range(a2 * a3):
    plt.subplot(a2, a3, i + 1)
    plt.imshow(b35[:, i].reshape(48, 48), b38 = 'jet')
    b39 = 'Eigenvector ' + str(i + 1)
    plt.b31(b39, b40 = 6.5)
    plt.xticks(())
    plt.yticks(())
plt.show()
b41 = go.Scatter(
    b21 = b36[:, 0],
    b22 = b36[:, 1],
    b24 = b8,
    b42 = b8,
    b23 = 'markers',
    b43 = b8,
    b44 = False,
    b45 = dict(
        b40 = 8,
        b28 = b8,
        b46 = 'Jet',
        b47 = False,
        b26 = dict(
            b48 = 2,
            b28 = 'rgb(255, 255, 255)'
        ),
        a4 = 0.8
    )
)
b49 = [b41]
b50 = go.Layout(
    b31 = 'Principal Component Analysis (PCA)',
    b51 = 'closest',
    b32 = dict(
        b31 = 'First Principal Component',
        b52 = 5,
        b53 = False,
        b54 = 2,
    ),
    b33 = dict(
        b31 = 'Second Principal Component',
        b52 = 5,
        b54 = 2,
    ),
    b44 = True
)
b30 = go.Figure(b49=b49, b50=b50)
py.iplot(b30, b34 = 'styled-scatter')
X_train, X_test, Y_train, b55 = train_test_split(b36, b8, random_state=42, test_size=0.2)
b56 = SVC()
b56.fit(X_train, Y_train)
print('Train Score: ', b56.score(X_train, Y_train))
print('Test Score: ', b56.score(X_test, b55))