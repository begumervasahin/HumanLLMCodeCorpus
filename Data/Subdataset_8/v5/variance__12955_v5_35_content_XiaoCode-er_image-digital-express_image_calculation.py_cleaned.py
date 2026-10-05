from skimage import io
import math
import numpy as np
class ImageDigitalExpress(object):
    def __init__(self, image_path):
        self._image_path = image_path
    def image_mean_variance(self):
        img = io.imread(self._image_path, as_grey=True)
        row, column = img.shape
        mean = np.mean(img)
        variance = np.std(img)
        return mean, variance
    def image_infoentropy(self):
        img = io.imread(self._image_path, as_grey=True)
        hist, _ = np.histogram(img, bins=256)
        hist = hist[hist != 0] / float(img.size)
        img_entropy = -np.sum(hist * np.log2(hist))
        return img_entropy