import numpy as np
import cv2
import argparse
import sys
from SVD_Probaility_Tables import *
from linearRegression import *
try:
    sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
except:
    pass
THETA_FILE = 'thetas.csv'
def preprocess_image(img_name):
    img_gray = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
    img_row = np.reshape(img_gray, (1, 256*256))
    centered_img_data = centerData(img_row)
    print("Subset of centered image data:", centered_img_data[0, 40000:40500])
    return centered_img_data
def compute_and_print_F_matrix(image_data):
    F = compute_F_Mat(image_data)
    K = 5
    Freduced = F[:, :K]
    print("\n===== Computing F matrix through SVD =====\n")
    print("F shape:", F.shape)
    print("F Reduced shape:", Freduced.shape)
    print("F Reduced:", Freduced)
    return Freduced
def load_theta_values():
    thetas = np.genfromtxt(THETA_FILE, delimiter=',')
    print("Theta shape:", thetas.shape)
    print("Theta values:", thetas)
    return thetas
def compute_results_matrix(Freduced, thetas):
    FreducedNorm = normalizeNewF(Freduced)
    print("Normalized F matrix:", FreducedNorm)
    resultsMatrix = FreducedNorm[0] * thetas
    print("\n===== Dimensions of the Result Matrix {} =====\n".format(resultsMatrix.shape))
    print("Results Matrix:", resultsMatrix)
def test_image(img_name):
    centered_img_data = preprocess_image(img_name)
    Freduced = compute_and_print_F_matrix(centered_img_data)
    thetas = load_theta_values()
    compute_results_matrix(Freduced, thetas)
if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--img_location", required=True, help="Path to the image we want to test")
    args = vars(ap.parse_args())
    test_image(args["img_location"])