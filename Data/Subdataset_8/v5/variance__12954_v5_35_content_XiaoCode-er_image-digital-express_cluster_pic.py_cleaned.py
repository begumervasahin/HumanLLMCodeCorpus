import os
import math
import matplotlib.pyplot as plt
from skimage import io
def calculate_image_statistics(image):
    mean_intensity = image.mean()
    variance = math.sqrt(((image - mean_intensity) ** 2).mean())
    return mean_intensity, variance
def cluster_images(directory):
    mean_intensity_list = []
    variance_list = []
    for image_name in os.listdir(directory):
        image_path = os.path.join(directory, image_name)
        image = io.imread(image_path, as_gray=True)
        mean_intensity, variance = calculate_image_statistics(image)
        mean_intensity_list.append(mean_intensity)
        variance_list.append(variance)
    return mean_intensity_list, variance_list
class_directories = ['D:/fonts/class/0/', 'D:/fonts/class/1/', 'D:/fonts/class/2/']
class_clusters = [cluster_images(directory) for directory in class_directories]
colors = ['r', 'b', 'y']
labels = ['Class 0', 'Class 1', 'Class 2']
for cluster, color, label in zip(class_clusters, colors, labels):
    plt.scatter(cluster[0], cluster[1], c=color, label=label)
plt.xlabel('Mean Intensity')
plt.ylabel('Variance')
plt.legend()
plt.show()