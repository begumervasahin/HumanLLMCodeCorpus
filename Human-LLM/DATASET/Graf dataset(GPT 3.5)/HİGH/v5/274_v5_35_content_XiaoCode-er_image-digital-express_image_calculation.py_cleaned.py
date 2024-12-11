from skimage import io
import math
import numpy as np
class class1(object):
    def fonk1(self, image_path):
        self.b1 = image_path
    def fonk2(self):
        b2 = io.imread(self.b1, as_grey=True)
        row, b3 = b2.shape
        b4 = np.b4(b2)
        b5 = np.std(b2)
        return b4, b5
    def fonk3(self):
        b2 = io.imread(self.b1, as_grey=True)
        b7, b6 = np.histogram(b2, bins=256)
        b7 = b7[b7 != 0] / float(b2.size)
        b8 = -np.sum(b7 * np.log2(b7))
        return b8