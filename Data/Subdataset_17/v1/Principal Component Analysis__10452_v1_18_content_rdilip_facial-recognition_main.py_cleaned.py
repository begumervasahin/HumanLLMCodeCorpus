import numpy as np
import cv2
import glob, os
from sklearn.preprocessing import normalize
os.makedirs("grayimg", exist_ok=True)
os.makedirs("adjusted", exist_ok=True)
problems = []
image_paths = glob.glob("img/*.jpg")
image_num = iter(range(len(image_paths) * 2))
mu_image = np.zeros((150, 150))
num_images = 0
for img_path in image_paths:
    try:
        image = cv2.imread(img_path, 0)[:150, :150]
        if image is None:
            raise ValueError(f"Image {img_path} not loaded properly.")
        image_index = next(image_num)
        cv2.imwrite(f"grayimg/{image_index}.png", image)
        mu_image += image
        num_images += 1
    except Exception as e:
        problems.append((img_path, str(e)))
mu_image = mu_image / float(num_images)
for img_index in range(num_images):
    image = cv2.imread(f"grayimg/{img_index}.png", 0)
    if image is None:
        problems.append((f"grayimg/{img_index}.png", "Image not loaded properly."))
        continue
    new_image = image.astype(np.float64) - mu_image
    cv2.imwrite(f'adjusted/{img_index}.png', new_image)
vectors = []
for img_path in glob.glob("adjusted/*.png"):
    image = cv2.imread(img_path, 0)
    if image is not None:
        vectors.append(image.reshape((150 * 150,)))
V = np.array(vectors)
A = np.transpose(V)
L = np.dot(np.transpose(A), A)
eigenValues, eigenVectors = np.linalg.eig(L)
idx = eigenValues.argsort()[::-1]
eigenValues = eigenValues[idx]
eigenVectors = eigenVectors[:, idx]
eigenVectors_ = np.dot(A, eigenVectors)
U = normalize(eigenVectors_, norm='l1', axis=0)
target_image = cv2.imread("george.jpg", 0)[:150, :150]
if target_image is None:
    raise ValueError("Target image 'george.jpg' not loaded properly.")
U_r = U[:, :50]
omega = np.dot(np.transpose(U_r), target_image.reshape((150 * 150, 1)) - mu_image.reshape((150 * 150, 1)))
smallest_dist = float("inf")
smallest_img = ""
for img_path in image_paths:
    img = cv2.imread(img_path, 0)[:150, :150]
    if img is None:
        problems.append((img_path, "Image not loaded properly."))
        continue
    omega_i = np.dot(np.transpose(U_r), img.reshape((150 * 150, 1)) - mu_image.reshape((150 * 150, 1)))
    d = np.linalg.norm(omega - omega_i)
    if d < smallest_dist:
        smallest_dist = d
        smallest_img = img_path
print(f"The closest image is: {smallest_img}")
print(f"Problems encountered: {problems}")