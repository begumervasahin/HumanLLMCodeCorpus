
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import datetime
def cluster_analysis(data_array, k):
	"""
	Groups (clusters) the input images into "k" groups (user input for k is expected), based on K-Means clustering.
	Outputs a plot of the resulting clusters, including the cluster centers. No data scaling is performed.
	:param data_array, k:
	:return cluster plot, labels:
	"""
	model = KMeans(n_clusters=int(k))
	model.fit(data_array)
	labels = model.predict(data_array)
	xs = data_array[:, 0]
	ys = data_array[:, 1]
	centroids = model.cluster_centers_
	centroids_x = centroids[:, 0]
	centroids_y = centroids[:, 1]
	plt.scatter(xs, ys, c=labels, alpha=0.5)
	plt.scatter(centroids_x, centroids_y, marker='D', s=30)
	plt.title(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	print("\nInspect the cluster plot shown.\nWhen ready, close the plot and the images will be sorted\n"
	      "and copied into subdirectories.")
	plt.show()
	return labels