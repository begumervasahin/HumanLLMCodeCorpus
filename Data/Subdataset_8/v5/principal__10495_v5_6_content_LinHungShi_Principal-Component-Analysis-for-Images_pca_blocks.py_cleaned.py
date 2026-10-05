import os
import numpy as np
import matplotlib.pyplot as plt
import theano
import theano.tensor as T
import theano.tensor.nnet.neighbours as nbs
from PIL import Image
import matplotlib.image as mpimg
import numpy.linalg as linalg
IMG_SIZE = 256
CWD = os.getcwd()
def load_images_from_directory(directory_path):
    os.chdir(directory_path)
    image_files = [f for f in os.listdir('.') if f.endswith('.jpg')]
    images = np.array([mpimg.imread(f) for f in image_files])
    return images
def extract_image_patches(images, patch_size):
    image_tensor = T.tensor4('Image')
    neibs = nbs.images2neibs(image_tensor, neib_shape=(patch_size, patch_size))
    window_function = theano.function([image_tensor], neibs)
    images = images.reshape((1, images.shape[0], images.shape[1], images.shape[2]))
    patches = window_function(images)
    return patches
def reconstruct_image(D, coeffs, num_coeffs, mean_patch, n_blocks, image_index):
    coeffs_image = coeffs[:num_coeffs, n_blocks * n_blocks * image_index:n_blocks * n_blocks * (image_index + 1)]
    D_image = D[:, :num_coeffs]
    mean_adjustment = np.dot(D_image.T, mean_patch.T)
    adjusted_coeffs = coeffs_image - np.repeat(mean_adjustment.reshape(-1, 1), n_blocks ** 2, axis=1)
    patches = np.dot(D_image, adjusted_coeffs) + np.repeat(mean_patch.reshape(-1, 1), n_blocks ** 2, axis=1)
    patches = patches.T
    slide_window = int(mean_patch.size ** 0.5)
    image_tensor = T.tensor4('image')
    neibs = nbs.images2neibs(image_tensor, neib_shape=(slide_window, slide_window))
    transToImage = nbs.neibs2images(neibs, neib_shape=(slide_window, slide_window), original_shape=(1, 1, IMG_SIZE, IMG_SIZE))
    trans_func = theano.function([neibs], transToImage)
    reconstructed_img = trans_func(patches)
    return reconstructed_img[0, 0]
def plot_reconstructed_images(D, coeffs, num_coefficients, mean_patch, n_blocks, image_index, save_path='output'):
    f, axarr = plt.subplots(3, 3)
    for i in range(3):
        for j in range(3):
            num_coeffs = num_coefficients[i * 3 + j]
            ax = axarr[i, j]
            ax.imshow(reconstruct_image(D, coeffs, num_coeffs, mean_patch, n_blocks, image_index), cmap='gray')
            ax.axis('off')
    plt.tight_layout()
    os.makedirs(save_path, exist_ok=True)
    f.savefig(os.path.join(save_path, f'reconstruction_{n_blocks}_im{image_index}.png'))
    plt.close(f)
def plot_top_16_components(D, component_size, save_path='output'):
    f, axarr = plt.subplots(4, 4)
    for i in range(4):
        for j in range(4):
            component = D[:, [i * 4 + j]].T
            ax = axarr[i, j]
            ax.imshow(component.reshape((component_size, component_size)), cmap='gray')
            ax.axis('off')
    plt.tight_layout()
    os.makedirs(save_path, exist_ok=True)
    f.savefig(os.path.join(save_path, 'top_16_components.png'))
    plt.close(f)
def main():
    images_path = os.path.join(CWD, 'Fei_256')
    images = load_images_from_directory(images_path)
    patch_sizes = [8, 32, 64]
    num_coefficients = [list(range(1, 10)), list(range(3, 30, 3)), list(range(5, 50, 5))]
    for patch_size, coeffs_range in zip(patch_sizes, num_coefficients):
        patches = extract_image_patches(images, patch_size)
        mean_patch = np.mean(patches, axis=0)
        adjusted_patches = patches - np.repeat(mean_patch.reshape(1, -1), patches.shape[0], axis=0)
        correlation_matrix = np.dot(adjusted_patches.T, adjusted_patches) / adjusted_patches.shape[0]
        eigenvalues, eigenvectors = linalg.eigh(correlation_matrix)
        basis_matrix = eigenvectors[:, ::-1]
        coefficients = np.dot(basis_matrix.T, adjusted_patches.T)
        for image_index in range(0, 200, 10):
            plot_reconstructed_images(basis_matrix, coefficients, coeffs_range, mean_patch, int(IMG_SIZE / patch_size), image_index)
        plot_top_16_components(basis_matrix, patch_size)
if __name__ == '__main__':
    main()