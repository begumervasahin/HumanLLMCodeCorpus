import numpy as np
import cv2
import glob, os
from sklearn.preprocessing import normalize
os.mkdir("grayimg")
os.mkdir("adjusted")
b1 = []
b2 = len(glob("img/*.jpg"))
b3 = range(b2 * 2)
b4 = np.zeros((150, 150))
b2 = 0
for img in glob("img/*.jpg"):
    try:
        b5 = cv2.imread(img, 0)[:150, :150]
        pre, b6 = os.path.splitext(img)
        cv2.imwrite("grayimg/{0}.png".format(b3.pop(0)), b5)
        b4 += b5
        b2 += 1
    except:
        b1.append(img)
b4 = b4 / float(b2)
for img in xrange(1, b2):
    b5 = cv2.imread("grayimg/{0}.png".format(img))
    b7 = b5.astype(np.float64)
    b7 -= b4
    cv2.imwrite('adjusted/{0}.png'.format(img), b7)
b8 = []
for img in glob("adjusted/*.png"):
    b5 = cv2.imread(img, 0)
    b8.append(b5.reshape((150 * 150,)))
b9 = np.array(b8)
b10 = np.transpose(b9)
b11 = np.dot(np.transpose(b10), b10)
b14, b12 = np.linalg.eig(b11)
b13 = b14.argsort()[::-1]
b14 = b14[b13]
b12 = b12[:,b13]
b15 = np.dot(b10, b12)
b16 = normalize(b15, norm = 'l1', axis = 0)
b17 = float("inf")
b18 = ""
b19 = b16[:,:50]
b20 = np.dot(np.transpose(b19), np.reshape(cv2.imread("george.jpg", 0)[:150,:150], (150*150, 1)) - mu)
for img in glob("img/*.jpg"):
    b21 = np.dot(np.transpose(b19), np.reshape(cv2.imread(img, 0)[:150,:150], (150*150, 1)) - mu)
    b22 = np.linalg.norm(b20 - b21)
    if b22  < b17:
        b17 = b22
        b18 = img