import numpy as np
import cv2
import glob, os
from sklearn.preprocessing import normalize
os.mkdir("grayimg")
os.mkdir("adjusted")
problems = []
num_images = len(glob("img/*.jpg"))
image_num = range(num_images * 2)
mu_image = np.zeros((150, 150))
num_images = 0
for img in glob("img/*.jpg"):
    try:
        image = cv2.imread(img, 0)[:150, :150]
        pre, ext = os.path.splitext(img)
        cv2.imwrite("grayimg/{0}.png".format(image_num.pop(0)), image)
        mu_image += image
        num_images += 1
    except:
        problems.append(img)
mu_image = mu_image / float(num_images)
for img in xrange(1, num_images):
    image = cv2.imread("grayimg/{0}.png".format(img))
    new_image = image.astype(np.float64)
    new_image -= mu_image
    cv2.imwrite('adjusted/{0}.png'.format(img), new_image)
vectors = []
for img in glob("adjusted/*.png"):
    image = cv2.imread(img, 0)
    vectors.append(image.reshape((150 * 150,)))
V = np.array(vectors)
A = np.transpose(V)
L = np.dot(np.transpose(A), A)
eigenValues, eigenVectors = np.linalg.eig(L)
idx = eigenValues.argsort()[::-1]
eigenValues = eigenValues[idx]
eigenVectors = eigenVectors[:,idx]
eigenVectors_ = np.dot(A, eigenVectors)
U = normalize(eigenVectors_, norm = 'l1', axis = 0)
smallest_dist = float("inf")
smallest_img = ""
U_r = U[:,:50]
omega = np.dot(np.transpose(U_r), np.reshape(cv2.imread("george.jpg", 0)[:150,:150], (150*150, 1)) - mu)
for img in glob("img/*.jpg"):
    omega_i = np.dot(np.transpose(U_r), np.reshape(cv2.imread(img, 0)[:150,:150], (150*150, 1)) - mu)
    d = np.linalg.norm(omega - omega_i)
    if d  < smallest_dist:
        smallest_dist = d
        smallest_img = img