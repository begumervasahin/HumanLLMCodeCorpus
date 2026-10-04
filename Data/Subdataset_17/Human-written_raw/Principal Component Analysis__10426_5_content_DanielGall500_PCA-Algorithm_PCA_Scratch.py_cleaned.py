import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
mean = [5, 5]
cov = [[1,0], [100,100]]
data = pd.DataFrame(np.random.multivariate_normal(mean, cov, 100))
plt.scatter(data[0], data[1], color='b')
def subtract_mean(matrix):
	for col in matrix.columns:
		mean = np.mean(matrix[col])
		sub_mean = lambda x: x - mean
		matrix[col] = matrix[col].apply(sub_mean)
	return matrix
def covariance(matrix):
	cov_list = np.array([])
	cols = matrix.columns
	c_header1, c_header2 = 'x', 'y'
	combinations = [[col, f] for f in cols for col in cols]
	for c1, c2 in combinations:
		comb_data = matrix[[c1, c2]]
		comb_data.columns = [c_header1, c_header2]
		multiplied_columns = [np.multiply(i, j) for i, j in
		 comb_data.itertuples(index=False)]
		n = comb_data.shape[0]
		covariance = np.sum(multiplied_columns) / (n - 1)
		cov_list = np.append(cov_list, covariance)
	cov_matrix = np.matrix(cov_list).reshape([len(cols), len(cols)])
	return cov_matrix
def get_principle_comp(eig_vals, eig_vecs, dimensions):
	eigval_max = np.argsort(-eig_vals)[:dimensions]
	eigvec_max = eig_vecs[:,eigval_max]
	return eigvec_max
mean_adjusted = subtract_mean(data)
covariance_data = covariance(mean_adjusted)
eig_vals, eig_vecs = np.linalg.eig(covariance_data)
principle_comp = get_principle_comp(eig_vals, eig_vecs, 2)
feature_vector = np.dot(principle_comp.T, data.T)
print feature_vector.T
plt.scatter(feature_vector[0], feature_vector[1], color='r', marker='x')
plt.show()