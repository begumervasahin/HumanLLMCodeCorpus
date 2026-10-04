import os
import glob
import cv2
import numpy as np
from sklearn.preprocessing import normalize
os.makedirs("grayimg", exist_ok=True)
os.makedirs("adjusted", exist_ok=True)
problems = []
image_files = glob.glob("img/*.jpg")
num_images = len(image_files)
mu_image = np.zeros((150, 150))
processed_image_count = 0
def process_images(image_files):
    global processed_image_count, mu_image
    for img_path in image_files:
        try:
            image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)[:150, :150]
            cv2.imwrite(f"grayimg/{processed_image_count}.png", image)
            mu_image += image
            processed_image_count += 1
        except Exception as e:
            problems.append(img_path)
            print(f"Error processing {img_path}: {e}")
def compute_mean_image():
    global mu_image
    mu_image /= float(processed_image_count)
def adjust_images():
    for img_index in range(processed_image_count):
        image = cv2.imread(f"grayimg/{img_index}.png", cv2.IMREAD_GRAYSCALE)
        new_image = image.astype(np.float64) - mu_image
        cv2.imwrite(f"adjusted/{img_index}.png", new_image)
def prepare_dataset():
    vectors = []
    for img_path in glob.glob("adjusted/*.png"):
        image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        vectors.append(image.reshape(150 * 150))
    return np.array(vectors)
def compute_eigenfaces(V):
    A = V.T
    L = np.dot(A.T, A)
    eigenValues, eigenVectors = np.linalg.eig(L)
    sorted_indices = np.argsort(eigenValues)[::-1]
    eigenValues = eigenValues[sorted_indices]
    eigenVectors = eigenVectors[:, sorted_indices]
    eigenVectors_ = np.dot(A, eigenVectors)
    return normalize(eigenVectors_, norm='l1', axis=0)
def find_most_similar_image(target_image, U_r):
    smallest_dist = float("inf")
    smallest_img = ""
    for img_path in image_files:
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)[:150, :150]
        img_vector = img.reshape(150 * 150, 1) - mu_image.reshape(150 * 150, 1)
        omega_i = np.dot(U_r.T, img_vector)
        distance = np.linalg.norm(omega - omega_i)
        if distance < smallest_dist:
            smallest_dist = distance
            smallest_img = img_path
    return smallest_img
process_images(image_files)
compute_mean_image()
adjust_images()
V = prepare_dataset()
U = compute_eigenfaces(V)
target_image = cv2.imread("george.jpg", cv2.IMREAD_GRAYSCALE)[:150, :150]
target_vector = target_image.reshape(150 * 150, 1) - mu_image.reshape(150 * 150, 1)
U_r = U[:, :50]
omega = np.dot(U_r.T, target_vector)
most_similar_image = find_most_similar_image(target_image, U_r)
print(f"The image most similar to the target is: {most_similar_image}")