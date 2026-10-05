import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import glob
from numpy import linalg as LA
def load_MNIST_data(data_path):
    files = glob.glob(data_path)
    images = [np.array(Image.open(fname)) for fname in files]
    return np.array(images)
def add_noise(data, noise_level):
    gauss_noise = np.random.normal(0, noise_level, data.shape)
    noisy_data = gauss_noise + data / 255.0
    return noisy_data
def flatten_data(data):
    return data.reshape(data.shape[0], -1)
def calculate_mean(data):
    return np.mean(data, axis=0)
def calculate_covariance_matrix(data):
    return np.matmul(data.T, data)
def calculate_eigen(data):
    eigenValues, eigenVectors = LA.eigh(data)
    return eigenValues[::-1], eigenVectors[:, ::-1]
def reconstruct_data(data, eigenvectors, mean_vector, num_components):
    projected_data = np.matmul(data, eigenvectors[:, :num_components])
    reconstruct_data = np.matmul(projected_data, eigenvectors[:, :num_components].T)
    return reconstruct_data + mean_vector
def plot_energy_graph(eigenvalues, total_components):
    Total_Energy = np.sum(np.square(eigenvalues))
    energy_ratios = np.cumsum(eigenvalues) / Total_Energy
    plt.plot(np.arange(1, total_components), energy_ratios, label='number of components')
    plt.xlabel('Number of components (K)')
    plt.ylabel('Ratio of Energy at K components to All components')
    plt.title("Energy Graph")
    plt.legend()
    plt.show()
def main():
    image_no = 101
    Total_components = 784
    data_path = "./data/processed/images/train/0_*"
    OriginalData = load_MNIST_data(data_path)
    plt.imshow(OriginalData[image_no], cmap='gray')
    plt.title('Original Image ({} eigenVectors)'.format(Total_components))
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.savefig("./Results/PCAReconstruct_with_NoisyImages/OriginalImage.jpg")
    NoisyData = add_noise(OriginalData, noise_level=0.04)
    plt.imshow(NoisyData[image_no], cmap='gray')
    plt.title('Noisy Image ({} eigenVectors)'.format(Total_components))
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.savefig("./Results/PCAReconstruct_with_NoisyImages/NoisyImage.jpg")
    flat_arr = flatten_data(NoisyData)
    mean_vector = calculate_mean(flat_arr)
    X = flat_arr - mean_vector
    cov_mat = calculate_covariance_matrix(X)
    eigenValues, eigenVectors = calculate_eigen(cov_mat)
    reconstruct_data_all_EVs = reconstruct_data(X, eigenVectors, mean_vector, Total_components)
    plt.imshow(reconstruct_data_all_EVs[image_no].reshape(28, 28), cmap='gray')
    plt.title('Reconstructed Image ({} eigenVectors)'.format(Total_components))
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.savefig("./Results/PCAReconstruct_with_NoisyImages/ReconstructImage_all_EVs.jpg")
    plot_energy_graph(eigenValues, Total_components)
    Effective_numberOfComponents = np.argmax(np.cumsum(eigenValues) / np.sum(eigenValues) >= 0.99) + 1
    reconstruct_data_effective_EVs = reconstruct_data(X, eigenVectors, mean_vector, Effective_numberOfComponents)
    plt.imshow(reconstruct_data_effective_EVs[image_no].reshape(28, 28), cmap='gray')
    plt.title('Reconstructed Image ({} eigenVectors)'.format(Effective_numberOfComponents))
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.savefig("./Results/PCAReconstruct_with_NoisyImages/ReconstructImage_Effective_EVs.jpg")
if __name__ == "__main__":
    main()