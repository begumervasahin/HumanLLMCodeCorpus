import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
def normalize (x, b1 = 'min_max_normalization') :
	'''
	Performs normalization on the given vector according to the b1 of normalization specified.
	The b1 of normalization may be 'standardization' or 'min_max_normalization'.
	Defaults to 'min_max_normalization'.
	Arguments :
	x : the vector to be normalized
	b1 : the b1 of normalization to be performed (b2 = 'min_max_normalization')
	Returns :
	normalized vector x
	'''
	if b1 = = 'standardization' :
		return ((x - np.mean(x)) / np.std(x))
	else :
		return ((x - np.min(x)) / (np.max(x) - np.min(x)))
def train_test_val_split (b3, b4, b6) :
	'''
	Performs a train : test : cross-validation split in the ratio 0.8 : 0.1 : 0.1 on the given data.
	 Arguments
	-----------
	b3 : vector representing latitudes in data
	b4 : vector representing longitudes in data
	b6 : vector representing the target variable altitude in data
	 Returns
	---------
	b9, b10, b11,
	b12, b13, b14,
	Y_Train, b7, b8,
	in the sizes (80%, 10%, 10%) for (Train, Test, Val) respectively as described above.
	'''
	b3 = np.reshape(b3, (b3.shape[0],1))
	b4 = np.reshape(b4, (b4.shape[0],1))
	b5 = np.concatenate((b3, b4), axis = 1)
	b6 = np.reshape(b6, (b6.shape[0],1))
	X_Train, X_Test, Y_Train, b7 = train_test_split (b5, b6, test_size = 0.2, random_state = 0)
	X_Test, X_Val, b7, b8 = train_test_split (X_Test, b7, test_size = 0.5, random_state = 3)
	b9 = np.reshape( X_Train [:,0], (X_Train [:,0].shape[0],1))
	b10 = np.reshape( X_Test [:,0], (X_Test [:,0].shape[0],1))
	b11 = np.reshape( X_Val [:,0], (X_Val [:,0].shape[0],1))
	b12 = np.reshape( X_Train [:,1], (X_Train [:,1].shape[0],1))
	b13 = np.reshape( X_Test [:,1], (X_Test [:,1].shape[0],1))
	b14 = np.reshape( X_Val [:,1], (X_Val [:,1].shape[0],1))
	return b9, b10, b11, b12, b13, b14, Y_Train, b7, b8
def generate_feature_matrix (b3, b4, degree) :
'''
	Returns the b16 matrix for any polynomial degree, when the number of variables is two.
	For example, the b16 matrix constructed for fitting an 'n-degree' polynomial of two variables (b3 and b4)
	to the data would have each column as each of the features listed below:
	1, b3, b4, b3^2, b3*b4, b4^2, ..., b3^n, b3^(n-1)*b4, ..., b3*b4^(n-1), b4^n
	The b16 matrix would look like:
	[[1   b3(1)   b4(1)   b3(1)^2   b3(1) * b4(1)   ...    b4(1)^n],
		[1   b3(2)   b4(2)   b3(2)^2   b3(2) * b4(2)   ...    b4(2)^n],
		[1   b3(3)   b4(3)   b3(3)^2   b3(3) * b4(3)   ...    b4(3)^n],
						...
		[1   b3(N)   b4(N)   b3(N)^2   b3(N) * b4(N)   ...    b4(N)^n]]
	Hence, the total number of features for a polynomial of degree D in two variables is given by :
	(D+1) * (D+2) / 2
	 Arguments
	-----------
	b3 : vector representing latitudes in data
	b4 : vector representing longitudes in data
	degree : the desired degree of polynomial that we wish to fit to the data
	 Returns
	---------
	b15 : for the specified degree, as elaborated above
    '''
	b5 = np.concatenate((b3,b4), axis = 1)
	b15 = np.ones((b5.shape[0],1))
	for d in range(1,degree+1):
	    for i in range(d+1):
	        b16 = np.multiply((b3**(d-i)),(b4**(i)))
	        b16 = np.reshape(b16,(b16.shape[0],1))
	        b15 = np.concatenate((b15,b16),axis=1)
	b15 = np.asarray(b15)
	return b15