import numpy as np
import cv2
import glob
import os
from sklearn.preprocessing import normalize
IMAGE_SIZE = 150
GRAY_IMG_DIR = "grayimg"
ADJUSTED_IMG_DIR = "adjusted"
os.makedirs(GRAY_IMG_DIR, exist_ok=True)
os.makedirs(ADJUSTED_IMG_DIR, exist_ok=True)
def process_and_save_images(image_paths):
    mu_image = np.zeros((IMAGE_SIZE, IMAGE_SIZE))
    num_images = 0
    problems = []
    for img_path in image_paths:
        try:
            image = cv2.imread(img_path, 0)[:IMAGE_SIZE, :IMAGE_SIZE]
            if image is None:
                raise ValueError(f"Image {img_path} not loaded properly.")
            image_index = num_images
            cv2.imwrite(f"{GRAY_IMG_DIR}/{image_index}.png", image)
            mu_image += image
            num_images += 1
        except Exception as e:
            problems.append((img_path, str(e)))
    mu_image /= float(num_images)
    return mu_image, num_images, problems
def adjust_images(mu_image, num_images):
    problems = []
    for img_index in range(num_images):
        try:
            image = cv2.imread(f"{GRAY_IMG_DIR}/{img_index}.png", 0)
            if image is None:
                raise ValueError(f"Image {GRAY_IMG_DIR}/{img_index}.png not loaded properly.")
            new_image = image.astype(np.float64) - mu_image
            cv2.imwrite(f"{ADJUSTED_IMG_DIR}/{img_index}.png", new_image)
        except Exception as e:
            problems.append((f"{GRAY_IMG_DIR}/{img_index}.png", str(e)))
    return problems
def collect_image_vectors():
    vectors = []
    for img_path in glob.glob(f"{ADJUSTED_IMG_DIR}/*.png"):
        image = cv2.imread(img_path, 0)
        if image is not None:
            vectors.append(image.reshape((IMAGE_SIZE * IMAGE_SIZE,)))
    return np.array(vectors)
def compute_eigenvectors(V):
    A = np.transpose(V)
    L = np.dot(np.transpose(A), A)
    eigenValues, eigenVectors = np.linalg.eig(L)
    idx = eigenValues.argsort()[::-1]
    eigenValues = eigenValues[idx]
    eigenVectors = eigenVectors[:, idx]
    eigenVectors_ = np.dot(A, eigenVectors)
    return normalize(eigenVectors_, norm='l1', axis=0)
def compute_feature_vector(image, mu_image, U_r):
    return np.dot(np.transpose(U_r), image.reshape((IMAGE_SIZE * IMAGE_SIZE, 1)) - mu_image.reshape((IMAGE_SIZE * IMAGE_SIZE, 1)))
def find_closest_image(image_paths, mu_image, U_r, target_image_path):
    target_image = cv2.imread(target_image_path, 0)[:IMAGE_SIZE, :IMAGE_SIZE]
    if target_image is None:
        raise ValueError(f"Target image '{target_image_path}' not loaded properly.")
    omega = compute_feature_vector(target_image, mu_image, U_r)
    smallest_dist = float("inf")
    smallest_img = ""
    problems = []
    for img_path in image_paths:
        try:
            img = cv2.imread(img_path, 0)[:IMAGE_SIZE, :IMAGE_SIZE]
            if img is None:
                raise ValueError(f"Image {img_path} not loaded properly.")
            omega_i = compute_feature_vector(img, mu_image, U_r)
            d = np.linalg.norm(omega - omega_i)
            if d < smallest_dist:
                smallest_dist = d
                smallest_img = img_path
        except Exception as e:
            problems.append((img_path, str(e)))
    return smallest_img, problems
if __name__ == "__main__":
    image_paths = glob.glob("img/*.jpg")
    mu_image, num_images, problems_processing = process_and_save_images(image_paths)
    problems_adjusting = adjust_images(mu_image, num_images)
    vectors = collect_image_vectors()
    U = compute_eigenvectors(vectors)
    U_r = U[:, :50]
    closest_image, problems_finding = find_closest_image(image_paths, mu_image, U_r, "george.jpg")
    print(f"The closest image is: {closest_image}")
    all_problems = problems_processing + problems_adjusting + problems_finding
    print(f"Problems encountered: {all_problems}")