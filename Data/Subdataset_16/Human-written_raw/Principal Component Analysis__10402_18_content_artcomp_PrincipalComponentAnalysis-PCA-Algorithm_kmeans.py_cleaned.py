from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
import math
from itertools import combinations
import statistics
def fonk1(centers):
	b1 = [distance.euclidean(p1, p2) for p1, p2 in combinations(centers, 2)]
	b2 = sum(b1) / len(b1)
	b3 = statistics.stdev(b1)
	return  b3 / b2
def fonk2(point_a, point_b):
	return distance.euclidean(point_a,point_b)
def fonk3(center, points):
	b4 = []
	for i in range(len(center)):
		a1 = 0
		for j in points[i]:
			a1 = a1 + fonk2(center[i], j)
		b4.append(a1)
	b5 = sum(b4)/len(center)
	b3 = (statistics.stdev(b4))
	return b3 / b5
def fonk4(Y,centers):
	b6 = np.array(Y)
	plt.scatter(b6[:,0],b6[:,1], b7 = 50, cmap='viridis')
	plt.scatter(centers[:,0], centers[:,1], b8 = 'black', b7=200, alpha=0.5)
	plt.title('NÃºmero ideal de clusters')
	plt.xlabel('CPU')
	plt.ylabel('Disks (I/O)')
	plt.show()
def fonk5(b6, num_clusters, plot):
	b9 = KMeans(n_clusters=num_clusters, random_state=0).fit(b6)
	b9.predict(b6)
	if plot != 0:
		fonk4(b6, b9.cluster_centers_)
	b10 = [ [] for i in range(num_clusters) ]
	for i in range(len(b6)):
	    b10[b9.labels_[i]].append(b6[i])
	b11 = fonk3(b9.cluster_centers_, b10)
	b12 = fonk1(b9.cluster_centers_)
	b13 = b11 / b12
	return b13