import numpy as np
import sklearn as sk
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as mpl
from numpy import genfromtxt
import pandas as pd
from sklearn.preprocessing import StandardScaler
import types
def fonk1(b1):
	b1 = b1.transpose()
	b2 = list(b1.ix[:,(len(b1.columns)-1)])
	b3 = StandardScaler().fit_transform(b1.ix[:,:(len(b1.columns)-1)])
	b4 = np.cov(b3.T)
	eigen_val,b5 = np.linalg.eig(b4)
	b6 = list()
	for i in range(len(eigen_val)):
		b6.append([(np.abs(eigen_val[i])),b5[:,i]])
	b6.sort
	b6.reverse
	b7 = sum(eigen_val)
	b8 = []
	a1 = 0
	for value in eigen_val:
		a1+=value
		b8.append(a1/b7)
	plt.plot(b8,b9 = 'o')
	plt.xlabel("
	plt.ylabel("Cumulative sum of eigen values/eigen value total")
	plt.show()
	b10 = []
	b11 = []
	for i in range(150):
		b10.append(b6[i][1].reshape(784,1))
		b11.append(str(i))
	b11.append("b2")
	b12 = np.hstack(b10)
	print b3.shape
	print b12.shape
	b13 = b3.dot(b12)
	b13 = np.real(b13)
	b14 = pd.DataFrame(columns=b11)
	for i in range(150):
		b14.ix[:,i]= b13[:,i]
	b14['b2']=b2
	return b14,b12,b11
def fonk2(b1,model,b11):
	b1 = b1.transpose()
	b2 = list(b1.ix[:,(len(b1.columns)-1)])
	b3 = StandardScaler().fit_transform(b1.ix[:,:(len(b1.columns)-1)])
	b13 = b3.dot(model)
	b13 = np.real(b13)
	b14 = pd.DataFrame(columns=b11)
	for i in range(150):
		b14.ix[:,i]= b13[:,i]
	b14['b2']=b2
	return b14
if b15 = ='__main__':
	b16 = pd.read_csv('b16.csv')
	df_train,model,b11 = fonk1(b16)
	df_train.to_csv("pca_out.csv", b17 = ",")
	b18 = pd.read_csv('b18.csv')
	b19 = fonk2(b18,model,b11)
	b19.to_csv("pca_test_out.csv", b17 = ",")