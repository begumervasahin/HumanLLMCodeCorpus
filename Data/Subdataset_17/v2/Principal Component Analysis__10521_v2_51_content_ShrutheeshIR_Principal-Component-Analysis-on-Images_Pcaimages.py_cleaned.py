import cv2
import os
import numpy as np
import scipy.linalg as sl
import matplotlib.pyplot as plt
def read_images(dir_name):
    images = []
    for i, file in enumerate(os.listdir(dir_name)):
        if i < 3000:
            img = cv2.imread(os.path.join(dir_name, file), 0)
            img = cv2.resize(img, (64, 64))
            images.append(img)
    return images
def create_data_matrix(images):
    print("Creating data matrix", end=" ... ")
    num_images = len(images)
    image_shape = images[0].shape
    data_matrix = np.zeros((num_images, image_shape[0] * image_shape[1]), dtype=np.float32)
    for i, image in enumerate(images):
        data_matrix[i, :] = image.flatten()
    print("DONE")
    return data_matrix
dir_name = "GImagesTrain/GoodImages"
images = read_images(dir_name)
data_matrix = create_data_matrix(images)
covariance_matrix = np.cov(data_matrix, rowvar=False)
print(f"Covariance matrix shape: {covariance_matrix.shape}")
eigenvalues, eigenvectors = sl.eig(covariance_matrix)
sorted_indices = eigenvalues.argsort()[::-1]
eigenvalues = eigenvalues[sorted_indices]
eigenvectors = eigenvectors[:, sorted_indices]
selected_image = data_matrix[250]
selected_image_matrix = np.matrix(selected_image).transpose()
original_image = selected_image_matrix.reshape(64, 64)
original_image = np.array(original_image)
print(f"Original image shape: {original_image.shape}")
eigenvectors = eigenvectors.transpose()
top_eigenvectors = eigenvectors[:75].real
print(f"Eigenvectors shape: {top_eigenvectors.shape}")
projected_image = top_eigenvectors @ selected_image_matrix
print(f"Projected shape: {projected_image.shape}")
reconstructed_image = np.matmul(top_eigenvectors.transpose(), projected_image)
reconstructed_image = reconstructed_image.reshape(64, 64)
print(f"Reconstructed shape: {reconstructed_image.shape}")
reconstructed_image /= 255
original_image /= 255
plt.imshow(reconstructed_image, cmap='gray')
plt.title('Reconstructed Image')
plt.show()
plt.imshow(original_image, cmap='gray')
plt.title('Original Image')
plt.show()