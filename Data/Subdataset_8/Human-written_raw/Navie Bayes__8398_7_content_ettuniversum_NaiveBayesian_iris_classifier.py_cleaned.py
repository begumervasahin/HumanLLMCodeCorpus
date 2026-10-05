import numpy as np
import scipy as sp
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris_dataset = load_iris()
print ()
print ("Iris Dataset Keys:")
print (iris_dataset.keys())
X = iris_dataset.data
y = iris_dataset.target
print ()
print ("Class Labels are:")
print (iris_dataset.target_names)
Cn = len(iris_dataset.target_names)
print ("{} class labels".format(Cn))
n,d_features = X.shape
print ()
print ("We have {} samples".format(n))
print ("With {} features each".format(d_features))
X_train, X_test, y_train, y_test = train_test_split(X, y)
n_train = len(X_train)
n_test = len(X_test)
print ()
print ("{} samples in the training set".format(n_train))
print ("{} samples in the test set".format(n_test))
mu_mat = np.zeros((Cn,d_features), dtype=float)
sig_mat = np.zeros((Cn,d_features), dtype=float)
for i in range(0,Cn):
	mu_mat[i] = X_train[y_train==i].mean(axis=0)
	sig_mat[i] = X_train[y_train==i].std(axis=0)
epsilon = 0.01
class_likelihood = np.zeros(Cn, dtype=float)
for i in range(0,Cn):
	class_likelihood[i] = (y_train==i).sum()/n_train
class_given_data_mat = np.zeros((n_test,Cn), dtype=float)
for i in range(0,n_test):
	for k in range(0,Cn):
		class_given_data = np.log(class_likelihood[k])
		for j in range(0,d_features):
			class_given_data = class_given_data + np.log(sp.stats.norm.pdf(X_test[i,j],mu_mat[k,j],sig_mat[k,j])*2*epsilon)
		class_given_data_mat[i,k] = class_given_data
print ()
print ("Probability that the Model predicts the correct class label:")
print ((class_given_data_mat.argmax(axis=1)==y_test).sum()/n_test)
print ()