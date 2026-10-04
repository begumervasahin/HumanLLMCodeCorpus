import cv2
import os
import numpy as np
import scipy.linalg as sl
import matplotlib.pyplot as plt
def read_images(dir_name, max_images=3000, img_size=(64, 64)):
    images = []
    for i, file in enumerate(os.listdir(dir_name)):
        if i >= max_images:
            break
        img_path = os.path.join(dir_name, file)
        img = cv2.imread(img_path, 0)
        if img is not None:
            img = cv2.resize(img, img_size)
            images.append(img)
    return images
def create_data_matrix(images):
    print("Creating data matrix", end=" ... ")
    num_images = len(images)
    img_shape = images[0].shape
    data_matrix = np.zeros((num_images, img_shape[0] * img_shape[1]), dtype=np.float32)
    for i, image in enumerate(images):
        data_matrix[i, :] = image.flatten()
    print("DONE")
    return data_matrix
def compute_eigenfaces(data_matrix, num_components=75):
    covariance_matrix = np.cov(data_matrix, rowvar=False)
    print(f"Covariance matrix shape: {covariance_matrix.shape}")
    eigenvalues, eigenvectors = sl.eig(covariance_matrix)
    sorted_indices = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[sorted_indices]
    eigenvectors = eigenvectors[:, sorted_indices]
    top_eigenvectors = eigenvectors[:, :num_components].real
    print(f"Eigenvectors shape: {top_eigenvectors.shape}")
    return eigenvalues, top_eigenvectors
def reconstruct_image(eigenvectors, image_vector):
    projected_image = eigenvectors @ image_vector
    reconstructed_image = eigenvectors.T @ projected_image
    return reconstructed_image
def normalize_image(image, max_value=255):
    return image / max_value
def main():
    dir_name = "GImagesTrain/GoodImages"
    images = read_images(dir_name)
    data_matrix = create_data_matrix(images)
    _, eigenvectors = compute_eigenfaces(data_matrix)
    selected_image = data_matrix[250]
    selected_image_matrix = np.matrix(selected_image).transpose()
    original_image = selected_image_matrix.reshape(64, 64)
    print(f"Original image shape: {original_image.shape}")
    reconstructed_image = reconstruct_image(eigenvectors, selected_image_matrix)
    reconstructed_image = reconstructed_image.reshape(64, 64)
    print(f"Reconstructed shape: {reconstructed_image.shape}")
    normalized_reconstructed_image = normalize_image(reconstructed_image)
    normalized_original_image = normalize_image(original_image)
    plt.imshow(normalized_reconstructed_image, cmap='gray')
    plt.title('Reconstructed Image')
    plt.show()
    plt.imshow(normalized_original_image, cmap='gray')
    plt.title('Original Image')
    plt.show()
if __name__ == "__main__":
    main()