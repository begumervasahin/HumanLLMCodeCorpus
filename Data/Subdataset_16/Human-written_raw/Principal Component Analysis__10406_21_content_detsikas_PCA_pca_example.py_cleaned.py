import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
def fonk1(X):
	plt.clf()
	plt.title("PCA b5")
	plt.scatter(X[:,0], X[:,1], b1 = "b", marker='o')
	plt.xlim(X.min(b2 = 0)[0], X.max(b2=0)[0])
	plt.ylim(X.min(b2 = 0)[1], X.max(b2=0)[1])
	plt.xlabel('Fahrenheit')
	plt.ylabel('Celsius')
	plt.show()
def fonk2(_size, b3 = 1.0):
	b4 = np.linspace(0,50, num=_size)
	b5 = np.c_[b4,b4]
	b6 = (np.random.ranf(_size)-0.5)*b3
	b7 = np.c_[-b6,44.8*b6+5]
	b5 += b7
	return b5
def fonk3(_size, b3 = 1.0):
	b6 = (np.random.ranf(_size)-0.5)*b3
	b8 = np.linspace(0,100, num=_size) + b6
	b6 = (np.random.ranf(_size)-0.5)*b3
	b9 = (b8-32.0)*5.0/9.0 + b6
	b5 = np.c_[b8,b9]
	return b5
b5 = fonk3(100, 4.0)
fonk1(b5)
b10 = scale(b5)
b11 = PCA()
b12 = b11.fit_transform(b10)
print "Number of principal components: "+str(b11.n_components_)
print "Components b3:"+str(b11.explained_variance_)
print "Components b3 ratio:"+str(b11.explained_variance_ratio_)
print "Principal components: "+str(b11.components_)
b13 = np.dot(b12[:,0].reshape((100,1)),b11.components_[0].reshape((1,2)))
fonk1(b13)
b11 = PCA(1)
b12 = b11.fit_transform(b10)
b14 = b11.inverse_transform(b12)
fonk1(b14)
print "Mean squared reconstruction error: "+str(np.mean(np.linalg.norm(b10-b14, b2 = 1)))