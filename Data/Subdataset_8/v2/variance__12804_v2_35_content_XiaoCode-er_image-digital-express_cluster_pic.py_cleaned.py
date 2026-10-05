from skimage import io
import math
import os
import matplotlib.pyplot as plt
def calculate_mean_variance(directory):
    filenames = os.listdir(directory)
    mean_values = []
    variance_values = []
    for filename in filenames:
        img_path = os.path.join(directory, filename)
        img = io.imread(img_path, as_gray=True)
        rows, cols = img.shape
        pixel_sum = img.sum()
        mean_brightness = pixel_sum / (rows * cols)
        mean_values.append(mean_brightness)
        diff_sum = ((img - mean_brightness) ** 2).sum()
        variance = math.sqrt(diff_sum / (rows * cols))
        variance_values.append(variance)
    return mean_values, variance_values
class_0_dir = 'D:/fonts/class/0/'
class_1_dir = 'D:/fonts/class/1/'
class_2_dir = 'D:/fonts/class/2/'
class_0_mean, class_0_variance = calculate_mean_variance(class_0_dir)
class_1_mean, class_1_variance = calculate_mean_variance(class_1_dir)
class_2_mean, class_2_variance = calculate_mean_variance(class_2_dir)
plt.scatter(class_0_mean, class_0_variance, c='r', label='Class 0')
plt.scatter(class_1_mean, class_1_variance, c='b', label='Class 1')
plt.scatter(class_2_mean, class_2_variance, c='y', label='Class 2')
plt.xlabel('Mean Brightness')
plt.ylabel('Variance of Brightness')
plt.legend()
plt.title('Scatter plot of Mean vs Variance for Different Classes')
plt.show()