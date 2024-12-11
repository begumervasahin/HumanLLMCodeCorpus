1. Repository: DanShai/kernalized-tsne
   File: main.py
   URL: https:
   Code Content:
import matplotlib.pyplot as plt
from ktsne import Ktsne
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.utils import shuffle
b1 = datasets.load_digits()
b2 = b1.data
b3 = b1.target
b2, b3 = shuffle(b2, b3)
b2 = b2[:500]
b3 = b3[:500]
b4 = MinMaxScaler(feature_range=(-1, 1))
b5 = {'p_degree': 2.0, 'p_dims': 12, 'eta': 25.0,
          'perplexity': 50.0, 'n_dims': 2, 'ker': 'pca', 'gamma': 1.0}
b6 = b5["ker"]
plt.clf()
b7 = b4.fit_transform(b2)
plt.subplot(2, 1, 1)
b8 = PCA(n_components=2).fit_transform(b7)
x_min, b9 = b8[:, 0].min() - .5, b8[:, 0].max() + .5
y_min, b10 = b8[:, 1].min() - .5, b8[:, 1].max() + .5
plt.scatter(b8[:, 0], b8[:, 1], b11 = b3, cmap=plt.cm.Set1,
            b12 = 'k')
plt.xlabel('p1')
plt.ylabel('p2')
plt.xlim(x_min, b9)
plt.ylim(y_min, b10)
plt.xticks(())
plt.yticks(())
plt.title(" PCA without ktsne ")
b13 = Ktsne(b7, b5=b5)
b14 = b13.get_solution(3000)
b14 = b4.fit_transform(b14)
plt.subplot(2, 1, 2)
plt.scatter(b14[:, 0], b14[:, 1], b11 = b3, cmap=plt.cm.Set1,
            b12 = 'k')
x1_min, b15 = b14[:, 0].min() - .5, b14[:, 0].max() + .5
y1_min, b16 = b14[:, 1].min() - .5, b14[:, 1].max() + .5
plt.xlabel(' V1 ')
plt.ylabel(' V2 ')
plt.xlim(x1_min, b15)
plt.ylim(y1_min, b16)
plt.xticks(())
plt.yticks(())
plt.title("with ktsne %s b6 " % b6)
plt.subplots_adjust(b17 = 0.5)
plt.show()
   README Content:
A simple alternative implementation of Laurens van der Maaten t-Distributed Stochastic Neighbor Embedding (t-SNE) , with use of kernals.
- joint probability pij
  ![Screenshot](img/pij.png)
- joint probability qij
  ![Screenshot](img/qij.png)
- Cost
  ![Screenshot](img/cost.png)
- gradient
  ![Screenshot](img/gra.png)
- gradient update
  ![Screenshot](img/graupdate.png)
for more information read the PDF file included.
Apart from pca, available kernels are:
- iquad
- cauchy
- fourier
- rbf
- poly
- cosine
- anova
you can add new/own b6 and test it, make sure to tune the parameters in b5 to get better results!
License : MIT and you are free to do what ever you want with it !
![Screenshot](img/ktsne.png)
![Screenshot](img/ktsne2.png)
