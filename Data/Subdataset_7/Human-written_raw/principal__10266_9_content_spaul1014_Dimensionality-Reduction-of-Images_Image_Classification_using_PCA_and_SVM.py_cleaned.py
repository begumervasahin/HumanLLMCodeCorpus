import os
import pandas as pd
import numpy as np
from PIL import Image
import plotly.offline as py
py.init_notebook_mode(b1 = True)
import plotly.graph_objs as go
import plotly.tools as tls
import seaborn as sns
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib
get_ipython().magic('matplotlib inline')
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
os.chdir('/Users/santanupaul/Documents/Personal/Masters in Analytics/UConn/Study Related/Python/Project/fer2013')
get_ipython().system('pwd')
b2 = pd.read_csv('fer2013.csv')
b2.head()
print(b2.b27)
b3 = b2[(b2['emotion'] == 3) | (b2['emotion'] == 4)]
print(b3.b27)
b4 = b3.emotion.value_counts()
print('b5 = ', b4[3]/(b4[3]+b4[4]))
print('b6 = ', b4[4]/(b4[3]+b4[4]))
b3.Usage.value_counts()
print(b3[b3['Usage'] == 'Training'].groupby(['emotion']).agg({'emotion': 'count'}))
print(b3[b3['Usage'] == 'PublicTest'].groupby(['emotion']).agg({'emotion': 'count'}))
print(b3[b3['Usage'] == 'PrivateTest'].groupby(['emotion']).agg({'emotion': 'count'}))
b3 = pd.concat([b3[['emotion']], b3['pixels'].str.split(" ", expand = True)], axis = 1)
b3.head()
b7 = b3.iloc[:, 1:].values
b8 = b3.iloc[:, 0].values
b7 = b7.astype(int)
b10
from sklearn.preprocessing import StandardScaler
b9 = StandardScaler().fit_transform(b7)
b10 = b7.mean(0)
b11 = b7.std(0)
b12 = np.mean(b9, axis=0)
b13 = (b9 - b12).T.dot((b9 - b12)) / (b9.b27[0]-1)
print('Covariance matrix \n', b13)
eig_vals, b14 = np.linalg.eig(b13)
print('Eigenvectors \n', b14)
print('\nEigenvalues \n', eig_vals)
print(b14[0, :].dot(b14[5, :]))
print(b14[3, :].dot(b14[12, :]))
for i in range(len(eig_vals)):
        np.testing.assert_array_almost_equal(1.0, np.linalg.norm(b14[:, i]))
b15 = [ (np.abs(eig_vals[i]),b14[:,i]) for i in range(len(eig_vals))]
b15.sort(b16 = lambda b21: b21[0], reverse= True)
b17 = sum(eig_vals)
b18 = [(i/b17)*100 for i in sorted(eig_vals, reverse=True)]
b19 = np.cumsum(b18)
b19
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
b30 = tls.make_subplots(insets=[{'cell': (1,1), 'l': 0.7, 'b': 0.5}],
                          b31 = True)
b30.append_trace(b20, 1, 1)
b30.append_trace(b29,1,1)
b30.b52.b32 = 'Explained Variance plots - Full and Zoomed-in'
b30.b52.b33 = dict(range=[0, 80], b32 = 'Feature columns')
b30.b52.b34 = dict(range=[0, 60], b32 = 'Explained Variance')
b30['b51'] += [go.Scatter(b21 = list(range(784)) , b22=b19, b33='x2', b34='y2', b24 = 'Cumulative Explained Variance')]
b30['b51'] += [go.Scatter(b21 = list(range(784)), b22=b18, b33='x2', b34='y2',b24 = 'Individual Explained Variance')]
py.iplot(b30, b35 = 'inset example')
a1 = 107
b36 = b15[0][1].reshape(len(b14),1)
for i in range(1, a1):
    b36 = np.hstack((b36, b15[i][1].reshape(len(b14),1)))
print(b36)
b37 = b9.dot(b36)
print(b37.b27)
b38 = b36.T
a2 = 4
a3 = 7
plt.figure(b39 = (11,8))
for i in list(range(a2 * a3)):
    a4 = 0
    plt.subplot(a2, a3, i + 1)
    plt.imshow(b38[i].reshape(48,48), b40 = 'jet')
    b41 = 'Eigenvector ' + str(i + 1)
    plt.b32(b41, b42 = 6.5)
    plt.xticks(())
    plt.yticks(())
plt.show()
b43 = go.Scatter(
    b21 = b37[:,0],
    b22 = b37[:,1],
    b24 = b8,
    b44 = b8,
    b23 = 'markers',
    b45 = b8,
    b46 = False,
    b47 = dict(
        b42 = 8,
        b28 = b8,
        b48 = 'Jet',
        b49 = False,
        b26 = dict(
            b50 = 2,
            b28 = 'rgb(255, 255, 255)'
        ),
        a5 = 0.8
    )
)
b51 = [b43]
b52 = go.Layout(
    b32 = 'Principal Component Analysis (PCA)',
    b53 = 'closest',
    b33 = dict(
         b32 = 'First Principal Component',
        b54 = 5,
        b55 = False,
        b56 = 2,
    ),
    b34 = dict(
        b32 = 'Second Principal Component',
        b54 = 5,
        b56 = 2,
    ),
    b46 = True
)
b30 = dict(b51=b51, b52=b52)
py.iplot(b30, b35 = 'styled-scatter')
b57 = b37.dot(b38)
b57 *= b11
b57 += b10
a6 = 628
b58 = b57[a6]
b59 = np.array(b58, dtype=np.uint8)
b59.resize(48, 48)
b60 = Image.fromarray(b59)
b60.show()
b58 = b3.iloc[a6, 1:]
b59 = np.array(b58, dtype=np.uint8)
b59.resize(48, 48)
b60 = Image.fromarray(b59)
b60.show()
from sklearn.svm import SVC
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, b61 = train_test_split(b37, b8, random_state = 42,
                                                    b62 = 0.2)
print('Train SVM...')
b63 = SVC()
b63.fit(X_train, Y_train)
print('Train Score: \n', b63.score(X_train, Y_train))
print('\n\nTest Score: \n', b63.score(X_test, b61))
a1 = 259
b36 = b15[0][1].reshape(len(b14),1)
for i in range(1, a1):
    b36 = np.hstack((b36, b15[i][1].reshape(len(b14),1)))
print(b36)
b37 = b9.dot(b36)
print(b37.b27)
b38 = b36.T
b57 = b37.dot(b38)
b57 *= b11
b57 += b10
a6 = 532
b58 = b57[a6]
b59 = np.array(b58, dtype=np.uint8)
b59.resize(48, 48)
b60 = Image.fromarray(b59)
b60.show()
b58 = b3.iloc[a6, 1:]
b59 = np.array(b58, dtype=np.uint8)
b59.resize(48, 48)
b60 = Image.fromarray(b59)
b60.show()
X_train, X_test, Y_train, b61 = train_test_split(b37, b8, random_state = 42,
                                                    b62 = 0.2)
print('Train SVM...')
b63 = SVC()
b63.fit(X_train, Y_train)
print('Train Score: \n', b63.score(X_train, Y_train))
print('\n\nTest Score: \n', b63.score(X_test, b61))
X_train, X_test, Y_train, b61 = train_test_split(b7, b8, random_state = 42,
                                                    b62 = 0.2)
print('Train SVM...')
b63 = SVC()
b63.fit(X_train, Y_train)
print('Train Score: \n', b63.score(X_train, Y_train))
print('\n\nTest Score: \n', b63.score(X_test, b61))