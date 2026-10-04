import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
b1 = [5, 5]
b2 = [[1,0], [100,100]]
b3 = pd.DataFrame(np.random.multivariate_normal(b1, b2, 100))
plt.scatter(b3[0], b3[1], b4 = 'b')
def fonk1(matrix):
	for col in matrix.b11:
		b1 = np.b1(matrix[col])
		b5 = lambda x: x - b1
		matrix[col] = matrix[col].apply(b5)
	return matrix
def fonk2(matrix):
	b6 = np.array([])
	b7 = matrix.b11
	c_header1, b8 = 'x', 'y'
	b9 = [[col, f] for f in b7 for col in b7]
	for c1, c2 in b9:
		b10 = matrix[[c1, c2]]
		b10.b11 = [c_header1, b8]
		b12 = [np.multiply(i, j) for i, j in
		 b10.itertuples(b13 = False)]
		b14 = b10.shape[0]
		b15 = np.sum(b12) / (b14 - 1)
		b6 = np.append(b6, b15)
	b16 = np.matrix(b6).reshape([len(b7), len(b7)])
	return b16
def fonk3(eig_vals, b21, dimensions):
	b17 = np.argsort(-eig_vals)[:dimensions]
	b18 = b21[:,b17]
	return b18
b19 = fonk1(b3)
b20 = fonk2(b19)
eig_vals, b21 = np.linalg.eig(b20)
b22 = fonk3(eig_vals, b21, 2)
b23 = np.dot(b22.T, b3.T)
print b23.T
plt.scatter(b23[0], b23[1], b4 = 'r', marker='x')
plt.show()