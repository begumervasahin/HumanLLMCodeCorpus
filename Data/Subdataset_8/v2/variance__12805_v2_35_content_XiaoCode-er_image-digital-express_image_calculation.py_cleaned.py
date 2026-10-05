import math
import numpy as np
from skimage import io
class ImageDigitalExpress(object):
    def __init__(self, image_path):
        self._image_path = image_path
    def image_mean_variance(self):
        summary = 0
        diff_sum = 0
        img = io.imread(self._image_path, as_gray=True)
        rows, columns = img.shape
        for i in range(rows):
            for j in range(columns):
                summary += img[i][j]
        mean = summary / (rows * columns)
        for i in range(rows):
            for j in range(columns):
                diff_sum += (img[i][j] - mean) ** 2
        variance = math.sqrt(diff_sum / (rows * columns))
        return mean, variance
    def image_infoentropy(self):
        img = io.imread(self._image_path, as_gray=True)
        img_size = img.size
        hist = np.histogram(img, bins=256)[0] / img_size
        hist_list = list(hist)
        num_zeros = hist_list.count(0)
        hist_list = [x for x in hist_list if x != 0]
        sum_num = len(hist_list)
        entropy_sum = 0
        for k in range(sum_num):
            entropy_sum += hist_list[k] * math.log(hist_list[k], 2)
        img_entropy = -entropy_sum
        return img_entropy
if __name__ == "__main__":
    image_path = "path_to_your_image.jpg"
    image_processor = ImageDigitalExpress(image_path)
    mean, variance = image_processor.image_mean_variance()
    entropy = image_processor.image_infoentropy()
    print("Mean:", mean)
    print("Variance:", variance)
    print("Entropy:", entropy)