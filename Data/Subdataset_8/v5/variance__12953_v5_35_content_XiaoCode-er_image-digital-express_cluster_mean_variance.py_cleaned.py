import os
import math
import numpy as np
from skimage import io
def compute_mean_variance(img):
    mean = np.mean(img)
    variance = np.std(img)
    return mean, variance
def compute_cluster_center_radius(path):
    file_names = os.listdir(path)
    mean_list = []
    variance_list = []
    for file_name in file_names:
        img_path = os.path.join(path, file_name)
        img = io.imread(img_path, as_gray=True)
        mean, variance = compute_mean_variance(img)
        mean_list.append(mean)
        variance_list.append(variance)
    cluster_center = np.mean(mean_list), np.mean(variance_list)
    euclidean_distances = [
        math.sqrt((mean - cluster_center[0]) ** 2 + (variance - cluster_center[1]) ** 2)
        for mean, variance in zip(mean_list, variance_list)
    ]
    cluster_radius = np.mean(euclidean_distances)
    return cluster_center, cluster_radius
