from skimage import io
import numpy as np
import os
def calculate_mean_and_variance(path):
    image_files = os.listdir(path)
    means = []
    variances = []
    for filename in image_files:
        img_path = os.path.join(path, filename)
        image = io.imread(img_path, as_gray=True)
        mean_intensity = np.mean(image)
        variance_intensity = np.std(image)
        means.append(mean_intensity)
        variances.append(variance_intensity)
    return means, variances
def calculate_cluster_center(means, variances):
    total_mean_intensity = np.mean(means)
    total_variance_intensity = np.mean(variances)
    return total_mean_intensity, total_variance_intensity
def calculate_cluster_radius(means, variances, cluster_center):
    total_distance = sum(
        np.linalg.norm([m - cluster_center[0], v - cluster_center[1]]) for m, v in zip(means, variances)
    )
    return total_distance / len(means)
def cluster_center_radius(path):
    means, variances = calculate_mean_and_variance(path)
    cluster_center = calculate_cluster_center(means, variances)
    cluster_radius = calculate_cluster_radius(means, variances, cluster_center)
    return cluster_center, cluster_radius
path_to_images = "path_to_your_images_directory"
cluster_center, cluster_radius = cluster_center_radius(path_to_images)
print("Cluster Center:", cluster_center)
print("Cluster Radius:", cluster_radius)