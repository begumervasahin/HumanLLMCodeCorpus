import numpy as np
import cv2
from SVD_Probaility_Tables import compute_F_Mat, normalizeNewF
from linearRegression import centerData
import argparse
THETA_FILE = 'thetas.csv'
def test_image(img_name):
    image = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
    flattened_image = np.reshape(image, (1, -1))
    centered_image = centerData(flattened_image)
    print("Centered Data (Sample):", centered_image[0, 40000:40500])
    print("\n===== Computing F matrix through SVD =====\n")
    F_matrix = compute_F_Mat(centered_image)
    K = 5
    Freduced = F_matrix[:, :K]
    thetas = np.genfromtxt(THETA_FILE, delimiter=',')
    print("F shape:", F_matrix.shape)
    print("Reduced F shape:", Freduced.shape)
    print("Reduced F:", Freduced)
    print("Theta shape:", thetas.shape)
    normalized_Freduced = normalizeNewF(Freduced)
    print("Normalized Reduced F:", normalized_Freduced)
    print("Thetas:", thetas)
    results_matrix = normalized_Freduced[0] * thetas
    print("\n===== Dimensions of the Result Matrix {} =====\n".format(results_matrix.shape))
    print("Result Matrix:", results_matrix)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Test an image with linear regression.")
    parser.add_argument("-i", "--img_location", required=True, help="Path to the image to test.")
    args = parser.parse_args()
    test_image(args.img_location)