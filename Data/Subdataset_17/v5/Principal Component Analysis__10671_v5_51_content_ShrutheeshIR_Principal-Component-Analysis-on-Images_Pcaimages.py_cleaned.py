import cv2
import os
import numpy as np
import scipy.linalg as sl
import matplotlib.pyplot as plt
def read_images(directory, max_images=3000, image_size=(64, 64)):
    images = []
    for i, file in enumerate(os.listdir(directory)):
        if i < max_images:
            img = cv2.imread(os.path.join(directory, file), 0)
            if img is not None:
                img = cv2.resize(img, image_size)
                images.append(img)
    return images
def create_data_matrix(images):
    print("Creating data matrix", end=" ... ")
    num_images = len(images)
    img_shape = images[0].shape
    data_matrix = np.zeros((num_images, img_shape[0] * img_shape[1]), dtype=np.float32)
    for i in range(num_images):
        image = images[i].flatten()
        data_matrix[i, :] = image
    print("DONE")
    return data_matrix
def compute_eigenfaces(data_matrix):
    covariance_matrix = np.cov(data_matrix, rowvar=False)
    print(f"Covariance matrix shape: {covariance_matrix.shape}")
    eigen_values, eigen_vectors = sl.eig(covariance_matrix)
    sorted_indices = eigen_values.argsort()[::-1]
    eigen_values = eigen_values[sorted_indices]
    eigen_vectors = eigen_vectors[:, sorted_indices]
    return eigen_values, eigen_vectors
def reconstruct_image(eigen_vectors, image_vector, num_components=75):
    top_eigen_vectors = eigen_vectors[:, :num_components].real
    projected_image = top_eigen_vectors.T @ image_vector
    reconstructed_image = top_eigen_vectors @ projected_image
    return reconstructed_image
def display_images(original_image, reconstructed_image):
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(original_image, cmap='gray')
    plt.title("Original Image")
    plt.subplot(1, 2, 2)
    plt.imshow(reconstructed_image, cmap='gray')
    plt.title("Reconstructed Image")
    plt.show()
directory_name = "GImagesTrain/GoodImages"
images = read_images(directory_name)
data_matrix = create_data_matrix(images)
eigen_values, eigen_vectors = compute_eigenfaces(data_matrix)
sample_image = data_matrix[250]
original_image = sample_image.reshape(64, 64).astype(np.float32)
reconstructed_image = reconstruct_image(eigen_vectors, sample_image)
original_image /= 255
reconstructed_image = reconstructed_image.reshape(64, 64) / 255
display_images(original_image, reconstructed_image)