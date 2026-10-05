import sys
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import skimage.filters as filt
from numpy import linalg as LA
from sklearn.preprocessing import StandardScaler
def expectation_maximization(Y, initial_Ps, initial_p, initial_q):
    max_iterations = 20
    N = Y.shape[0]
    mu0 = (initial_Ps * (1 - initial_p)) / ((initial_Ps * (1 - initial_p)) + (1 - initial_Ps) * (1 - initial_q))
    mu1 = (initial_Ps * initial_p) / ((initial_Ps * initial_p) + (1 - initial_Ps) * initial_q)
    mean_mu = np.mean([mu0 if y == 0 else mu1 for y in Y])
    print("\nInitial values:")
    print("Pie(0) =", initial_Ps)
    print("p(0) =", initial_p)
    print("q(0) =", initial_q)
    print("\nFor observable data = 0:")
    print("mu(1) =", mu0)
    print("For observable data = 1:")
    print("mu(1) =", mu1)
    print("Mean mu(1) =", mean_mu)
    for iteration in range(1, max_iterations + 1):
        Ps_sum = sum(mu0 if y == 0 else mu1 for y in Y)
        Ps = Ps_sum / 10
        print(f"\nIteration number: {iteration}")
        print(f"Pie({iteration}) = {Ps}")
        p_num = sum(mu1 for y in Y if y == 1)
        p_den = sum(mu1 for y in Y)
        p = p_num / p_den
        print(f"p({iteration}) = {p}")
        q_num = sum(1 - mu1 for y in Y if y == 1)
        q_den = sum(1 - mu1 for y in Y)
        q = q_num / q_den
        print(f"q({iteration}) = {q}")
        mu0 = (Ps * (1 - p)) / ((Ps * (1 - p)) + (1 - Ps) * (1 - q))
        mu1 = (Ps * p) / ((Ps * p) + (1 - Ps) * q)
        mean_mu = np.mean([mu0 if y == 0 else mu1 for y in Y])
        print("\nFor observable data = 0:")
        print(f"mu({iteration + 1}) = {mu0}")
        print("For observable data = 1:")
        print(f"mu({iteration + 1}) = {mu1}")
        print(f"Mean mu({iteration + 1}) = {mean_mu}")
def process_image(input_filename, debug=False):
    image = np.array(Image.open(input_filename))
    grayscale_image = 1.0 - rgb2gray(image)
    if debug:
        plt.figure(1)
        plt.imshow(grayscale_image)
        plt.title('Original Grayscale Image')
        plt.show()
    threshold = filt.threshold_minimum(grayscale_image)
    binary_image = grayscale_image > threshold
    if debug:
        plt.figure(2)
        plt.imshow(binary_image)
        plt.title('Binarized Image')
        plt.show()
    non_zero_rows, non_zero_cols = binary_image.nonzero()
    n_rows, n_cols = binary_image.shape
    left, right = max(0, min(non_zero_cols) - 1), min(n_cols - 1, max(non_zero_cols) + 1) + 1
    top, bottom = max(0, min(non_zero_rows) - 1), min(n_rows - 1, max(non_zero_rows) + 1) + 1
    windowed_image = binary_image[top:bottom, left:right]
    if debug:
        plt.figure(3)
        plt.imshow(windowed_image)
        plt.title('Windowed Image')
        plt.show()
    max_dim = max(windowed_image.shape)
    new_height = int(round(windowed_image.shape[0] / max_dim * 48))
    new_width = int(round(windowed_image.shape[1] / max_dim * 48))
    window_image = Image.fromarray(windowed_image.astype(np.uint8) * 255)
    resized_image = window_image.resize((new_width, new_height))
    resized_window = np.array(resized_image).astype(bool)
    output_window = np.zeros((resized_window.shape[0] + 2, resized_window.shape[1] + 2), dtype=bool)
    output_window[1:-1, 1:-1] = resized_window
    if debug:
        plt.figure(4)
        plt.imshow(output_window, cmap='Greys')
        plt.title('Resized Windowed Image')
        plt.show()
    return output_window
if __name__ == '__main__':
    X = np.array([(2, 3, 3, 4, 5, 7), (2, 4, 5, 5, 6, 8)])
    scaler = StandardScaler()
    X_standardized = scaler.fit_transform(X.T).T
    covariance_X = np.cov(X_standardized)
    eigenvalues, eigenvectors = LA.eig(covariance_X)
    eigen_pairs = [(np.abs(eigenvalues[i]), eigenvectors[:, i]) for i in range(len(eigenvalues))]
    eigen_pairs.sort(reverse=True)
    principal_component = eigen_pairs[0][1][:, np.newaxis]
    X_pca = X_standardized.T.dot(principal_component).T
    print("*****PCA*******\n")
    print("Eigenvalues of X.T@X:")
    print(eigenvalues)
    print("\nEigenvalues of X@X.T:")
    print(LA.eig(X @ X.T)[0])
    print("\nEigenvectors of X@X.T:")
    print(LA.eig(X @ X.T)[1])
    print("\nShape of transformed data:")
    print(X_pca.shape)
    print("\nTransformed data after dimension reduction:")
    print(X_pca)
    print("\n*****EM*******")
    Y = np.array([1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1])
    expectation_maximization(Y, 0.4, 0.6, 0.7)
    print("\n\n")
    expectation_maximization(Y, 0.5, 0.5, 0.5)