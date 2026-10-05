from skimage import io
import math
import numpy as np
import os
def cluster_center_radius(path):
    name_list = os.listdir(path)
    mean_list = []
    variance_list = []
    cluster_center_x = 0
    cluster_center_y = 0
    eu_dist_sum = 0
    for name in name_list:
        img_path = os.path.join(path, name)
        img = io.imread(img_path, as_gray=True)
        row, column = img.shape
        mean = np.mean(img)
        mean_list.append(mean)
        variance = np.std(img)
        variance_list.append(variance)
    for i in range(len(name_list)):
        cluster_center_x += mean_list[i]
        cluster_center_y += variance_list[i]
    x_mean = cluster_center_x / len(name_list)
    y_mean = cluster_center_y / len(name_list)
    cluster_center = np.array([x_mean, y_mean])
    for p in range(len(name_list)):
        eu_dist = math.sqrt((mean_list[p] - x_mean) ** 2 + (variance_list[p] - y_mean) ** 2)
        eu_dist_sum += eu_dist
    cluster_r = eu_dist_sum / len(name_list)
    return cluster_center, cluster_r
path_to_images = "path_to_your_images_directory"
cluster_center, cluster_radius = cluster_center_radius(path_to_images)
print("Cluster Center:", cluster_center)
print("Cluster Radius:", cluster_radius)