import cv2
import numpy as np
from PIL import Image
from sklearn.feature_extraction import image
import matplotlib.pyplot as plt
def fonk1(image_path):
    return cv2.imread(image_path).astype(np.float64)
def fonk2(image_channel, b1 = (16, 16), b5=1000):
    return image.extract_patches_2d(image_channel, b1 = b1, max_patches=b5)
def fonk3(b13):
    b2 = np.zeros((256, 256))
    for b6 in b13:
        b3 = b6.reshape(256, 1)
        b4 = b3.dot(b3.T)
        b2 += b4
    return b2
def fonk4(b14, b5 = 64, b1=(16, 16)):
    for i in range(b5):
        b6 = np.reshape(b14[:, i], b1)
        plt.imsave(f"Result{i}.png", b6.real, b7 = 'Greys')
def fonk5(b16, b8 = (142, 142), patch_offset=18):
    b9 = Image.new('RGB', b8, "white")
    a1 = 0
    for _ in range(8):
        a2 = 0
        for filename in b16:
            b10 = Image.open(filename)
            b9.paste(b10, (a2, a1))
            a2 += patch_offset
        a1 += patch_offset
    return b9
b11 = fonk1('clockwork-angels.jpg')
blue_channel, green_channel, b12 = cv2.split(b11)
b13 = fonk2(b12)
b2 = fonk3(b13)
eigenvalues, b14 = np.linalg.eig(b2)
b15 = np.argsort(eigenvalues)[::-1]
fonk4(b14, b5 = 64)
b16 = [f"Result{i}.png" for i in range(64)]
b9 = fonk5(b16)
b9.show()