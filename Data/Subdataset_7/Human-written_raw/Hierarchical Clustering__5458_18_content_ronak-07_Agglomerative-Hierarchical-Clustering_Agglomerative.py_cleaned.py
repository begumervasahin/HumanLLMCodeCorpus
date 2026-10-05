from scipy.cluster import hierarchy
import numpy as np
import scipy
import matplotlib.pyplot as plt
import distance
import time
def fonk1(double1,double2):
	if (double1< double2):
		return double1
	else:
		return double2
def fonk2(double1,double2):
	if (double1>double2):
		return double1
	else:
		return double2
def fonk3(b6,b7,k):
	a1 = 999.0
	a2 = 555
	a3 = 555
	for i in range(0,b7-1):
		for j in range (1,b7):
			if (i<j):
				if (b6[i][j]<a1):
					a1 = b6[i][j]
					a2 = i
					a3 = j
	b1 = []
	if(a2<a3):
		b1.append(b8[a2])
		b1.append(b8[a3])
		b8[a2]=b1
		del b8[a3]
	if(b10[a2]==-1 and b10[a3]==-1):
		b9[k][0]=a2
		b9[k][1]=a3
		b2 = fonk1(a2,a3)
		b10[b2]=b7+k
		b9[k][3]=2
	elif(b10[a2]!=-1 and b10[a3]!=-1):
		b9[k][0]=b10[a2]
		b9[k][1]=b10[a3]
		if(a2<a3):
			b10[a2]=b7+k
		else:
			b10[a3]=b7+k
		b9[k][3]=b9[int(fonk2(b9[k][0],b9[k][1])-b7)][3] + 1
	elif(b10[a2]!=-1 and b10[a3]==-1):
		if(a2<a3):
			b9[k][0]=b10[a2]
			b9[k][1]=a3
			b9[k][3]=b9[int(fonk2(b9[k][0],b9[k][1])-b7)][3] + 1
			b10[a2]=b7+k
		else:
			b9[k][0]=a2
			b9[k][1]=b10[a3]
			b9[k][3]=b9[int(fonk2(b9[k][0],b9[k][1])-b7)][3] + 1
			b10[a3]=b7+k
	elif(b10[a2]==-1 and b10[a3]!=-1):
		if(a2<a3):
			b9[k][0]=a2
			b9[k][1]=b10[a3]
			b9[k][3]=b9[int(fonk2(b9[k][0],b9[k][1])-b7)][3] + 1
			b10[a2]=b7+k
		else:
			b9[k][0]=b10[a2]
			b9[k][1]=a3
			b9[k][3]=b9[int(fonk2(b9[k][0],b9[k][1])-b7)][3] + 1
			b10[a3]=b7+k
	else:
		print("Error")
	b9[k][2]=a1
	for j in range(0,b7):
		if (j!=a3):
			b6[j][a2] = fonk1(b6[j][a2],b6[j][a3])
		b6[a2][j] = b6[j][a2]
		b6[j][a3] = 9999.0
		b6[a3][j] = 9999.0
	return b6
def fonk4(*args, **kwargs):
	b3 = scipy.cluster.hierarchy.dendrogram(*args, **kwargs)
	if not kwargs.get('no_plot', False):
		for i, d in zip(b3['icoord'], b3['dcoord']):
			b2 = 0.5 * sum(i[1:3])
			b4 = d[1]
			plt.plot(b2, b4, 'ro')
			plt.annotate("%.3g" % b4, (b2, b4), b5 = (0,12),textcoords='offset points',va='top', ha='center')
	return b3
b6 = np.load('distance_matrix.npy')
b7 = len(b6)
b8 = {}
b9 = np.zeros(shape=(b7-1,4))
b10 = {}
for i in range(0,b7):
	b11 = []
	b11.append(i)
	b8[i]=b11
for i in range(0,b7):
	b10[i]=-1
b12 = time.time()
for k in range(0,b7-1):
	b6 = fonk3(b6,b7,k)
print("Clustering done\t" + str(time.time()-b12))
b13 = [i for i in range(0,b7)]
plt.figure(b14 = (25, 25))
plt.title('Hierarchical Clustering Dendrogram (Agglomerative)')
plt.xlabel('Sequence No.')
plt.ylabel('Distance')
fonk4(b9,b15 = b13,show_leaf_counts=True,p=25,truncate_mode='lastp')
plt.show()