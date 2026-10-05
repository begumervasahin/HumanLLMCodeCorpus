from skimage import io
import math
import os
import matplotlib.pyplot as plt
def cluster(path):
    name_list = os.listdir(path)
    mean_list = []
    variance_list = []
    for filename in name_list:
        img_path = os.path.join(path, filename)
        img = io.imread(img_path, as_gray=True)
        row, column = img.shape
        summary = img.sum()
        mean = summary / (row * column)
        mean_list.append(mean)
        diff_sum = ((img - mean) ** 2).sum()
        variance = math.sqrt(diff_sum / (row * column))
        variance_list.append(variance)
    return mean_list, variance_list
des1 = 'D:/fonts/class/0/'
des2 = 'D:/fonts/class/1/'
des3 = 'D:/fonts/class/2/'
cluster1 = cluster(des1)
plt.scatter(cluster1[0], cluster1[1], c='r', label='Class 0')
cluster2 = cluster(des2)
plt.scatter(cluster2[0], cluster2[1], c='b', label='Class 1')
cluster3 = cluster(des3)
plt.scatter(cluster3[0], cluster3[1], c='y', label='Class 2')
plt.xlabel('Mean')
plt.ylabel('Variance')
plt.legend()
plt.title('Scatter plot of Mean vs Variance for Different Classes')
plt.show()