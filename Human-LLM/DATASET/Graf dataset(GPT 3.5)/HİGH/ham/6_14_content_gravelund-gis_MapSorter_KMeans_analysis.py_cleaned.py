
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import datetime
def fonk1(data_array, k):
	"""
	Groups (clusters) the input images into "k" groups (user input for k is expected), based on K-Means clustering.
	Outputs a plot of the resulting clusters, including the cluster centers. No data scaling is performed.
	:param data_array, k:
	:return cluster plot, b2:
	"""
	b1 = KMeans(n_clusters=int(k))
	b1.fit(data_array)
	b2 = b1.predict(data_array)
	b3 = data_array[:, 0]
	b4 = data_array[:, 1]
	b5 = b1.cluster_centers_
	b6 = b5[:, 0]
	b7 = b5[:, 1]
	plt.scatter(b3, b4, b8 = b2, alpha=0.5)
	plt.scatter(b6, b7, b9 = 'D', s=30)
	plt.title(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	print("\nInspect the cluster plot shown.\nWhen ready, close the plot and the images will be sorted\n"
	      "and copied into subdirectories.")
	plt.show()
	return b2