import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import glob
from numpy import linalg as LA
def fonk1(b12):
    b1 = glob.glob(b12)
    b2 = [np.array(Image.open(fname)) for fname in b1]
    return np.array(b2)
def fonk2(data, noise_level):
    b3 = np.random.normal(0, noise_level, data.shape)
    b4 = b3 + data / 255.0
    return b4
def fonk3(data):
    return data.reshape(data.shape[0], -1)
def fonk4(data):
    return np.mean(data, b5 = 0)
def fonk5(data):
    return np.matmul(data.T, data)
def fonk6(data):
    eigenValues, b6 = LA.eigh(data)
    return eigenValues[::-1], b6[:, ::-1]
def fonk7(data, eigenvectors, b17, num_components):
    b7 = np.matmul(data, eigenvectors[:, :num_components])
    b8 = np.matmul(b7, eigenvectors[:, :num_components].T)
    return b8 + b17
def fonk8(eigenvalues, total_components):
    b9 = np.sum(np.square(eigenvalues))
    b10 = np.cumsum(eigenvalues) / b9
    plt.plot(np.arange(1, total_components), b10, b11 = 'number of components')
    plt.xlabel('Number of components (K)')
    plt.ylabel('Ratio of Energy at K components to All components')
    plt.title("Energy Graph")
    plt.legend()
    plt.show()
def fonk9():
    a1 = 101
    a2 = 784
    b12 = "./data/processed/b2/train/0_*"
    b13 = fonk1(b12)
    plt.imshow(b13[a1], b14 = 'gray')
    plt.title('Original Image ({} b6)'.format(a2))
    plt.xlabel('b18 b5')
    plt.ylabel('Y b5')
    plt.savefig("./Results/PCAReconstruct_with_NoisyImages/OriginalImage.jpg")
    b15 = fonk2(b13, noise_level=0.04)
    plt.imshow(b15[a1], b14 = 'gray')
    plt.title('Noisy Image ({} b6)'.format(a2))
    plt.xlabel('b18 b5')
    plt.ylabel('Y b5')
    plt.savefig("./Results/PCAReconstruct_with_NoisyImages/NoisyImage.jpg")
    b16 = fonk3(b15)
    b17 = fonk4(b16)
    b18 = b16 - b17
    b19 = fonk5(b18)
    eigenValues, b6 = fonk6(b19)
    b20 = fonk7(b18, b6, b17, a2)
    plt.imshow(b20[a1].reshape(28, 28), b14 = 'gray')
    plt.title('Reconstructed Image ({} b6)'.format(a2))
    plt.xlabel('b18 b5')
    plt.ylabel('Y b5')
    plt.savefig("./Results/PCAReconstruct_with_NoisyImages/ReconstructImage_all_EVs.jpg")
    fonk8(eigenValues, a2)
    b21 = np.argmax(np.cumsum(eigenValues) / np.sum(eigenValues) >= 0.99) + 1
    b22 = fonk7(b18, b6, b17, b21)
    plt.imshow(b22[a1].reshape(28, 28), b14 = 'gray')
    plt.title('Reconstructed Image ({} b6)'.format(b21))
    plt.xlabel('b18 b5')
    plt.ylabel('Y b5')
    plt.savefig("./Results/PCAReconstruct_with_NoisyImages/ReconstructImage_Effective_EVs.jpg")
if b23 = = "__main__":
    fonk9()