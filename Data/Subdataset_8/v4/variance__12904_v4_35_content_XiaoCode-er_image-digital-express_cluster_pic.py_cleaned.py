import os
import math
import matplotlib.pyplot as plt
from skimage import io
def calculate_image_statistics(image_path):
    image = io.imread(image_path, as_gray=True)
    rows, cols = image.shape
    total_intensity = 0
    for i in range(rows):
        for j in range(cols):
            total_intensity += image[i][j]
    mean_intensity = total_intensity / (rows * cols)
    variance_sum = 0
    for i in range(rows):
        for j in range(cols):
            variance_sum += (image[i][j] - mean_intensity) ** 2
    variance = math.sqrt(variance_sum / (rows * cols))
    return mean_intensity, variance
def cluster_images(directory):
    image_names = os.listdir(directory)
    mean_intensity_list = []
    variance_list = []
    for image_name in image_names:
        image_path = os.path.join(directory, image_name)
        mean_intensity, variance = calculate_image_statistics(image_path)
        mean_intensity_list.append(mean_intensity)
        variance_list.append(variance)
    return mean_intensity_list, variance_list
class1_directory = 'D:/fonts/class/0/'
class2_directory = 'D:/fonts/class/1/'
class3_directory = 'D:/fonts/class/2/'
class1_cluster = cluster_images(class1_directory)
class2_cluster = cluster_images(class2_directory)
class3_cluster = cluster_images(class3_directory)
plt.scatter(class1_cluster[0], class1_cluster[1], c='r', label='Class 0')
plt.scatter(class2_cluster[0], class2_cluster[1], c='b', label='Class 1')
plt.scatter(class3_cluster[0], class3_cluster[1], c='y', label='Class 2')
plt.xlabel('Mean Intensity')
plt.ylabel('Variance')
plt.legend()
plt.show()