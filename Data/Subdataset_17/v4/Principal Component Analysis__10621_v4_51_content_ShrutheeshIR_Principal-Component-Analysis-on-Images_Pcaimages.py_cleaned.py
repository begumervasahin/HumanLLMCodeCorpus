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
directory_name = "GImagesTrain/GoodImages"
images = read_images(directory_name)
image_shape = images[0].shape
data_matrix = create_data_matrix(images)
covariance_matrix = np.cov(data_matrix, rowvar=False)
print(f"Covariance matrix shape: {covariance_matrix.shape}")
eigen_values, eigen_vectors = sl.eig(covariance_matrix)
sorted_indices = eigen_values.argsort()[::-1]
eigen_values = eigen_values[sorted_indices]
eigen_vectors = eigen_vectors[:, sorted_indices]
sample_image = data_matrix[250]
sample_image = np.matrix(sample_image).transpose()
original_image = sample_image.reshape(64, 64).astype(np.float32)
print(f"Original image shape: {original_image.shape}")
eigen_vectors = eigen_vectors.transpose()
top_eigen_vectors = eigen_vectors[:75].real
print(f"Top eigenvectors shape: {top_eigen_vectors.shape}")
projected_image = top_eigen_vectors @ sample_image
print(f"Projected image shape: {projected_image.shape}")
reconstructed_image = (top_eigen_vectors.transpose() @ projected_image).reshape(64, 64)
print(f"Reconstructed image shape: {reconstructed_image.shape}")
reconstructed_image /= 255
original_image /= 255
plt.imshow(reconstructed_image, cmap='gray')
plt.title("Reconstructed Image")
plt.show()
plt.imshow(original_image, cmap='gray')
plt.title("Original Image")
plt.show()