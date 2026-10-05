import numpy as np
import cv2
from SVD_Probaility_Tables import compute_F_Mat, normalizeNewF
from linearRegression import centerData
import argparse
THETA_FILE = 'thetas.csv'
def test_image(img_name):
    cur_img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
    img_row = np.reshape(cur_img, (1, 256*256))
    Xc = centerData(img_row)
    print("Centered Data (Sample):", Xc[0, 40000:40500])
    print("\n===== Computing F matrix through SVD =====\n")
    F = compute_F_Mat(Xc)
    K = 5
    Freduced = F[:, :K]
    thetas = np.genfromtxt(THETA_FILE, delimiter=',')
    print("F shape:", F.shape)
    print("Reduced F shape:", Freduced.shape)
    print("Reduced F:", Freduced)
    print("Theta shape:", thetas.shape)
    FreducesNorm = normalizeNewF(Freduced)
    print("Normalized Reduced F:", FreducesNorm)
    print("Thetas:", thetas)
    resultsMatrix = FreducesNorm[0] * thetas
    print("\n===== Dimensions of the Result Matrix {} =====\n".format(resultsMatrix.shape))
    print("Result Matrix:", resultsMatrix)
if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--img_location", required=True, help="Path to the image to test")
    args = vars(ap.parse_args())
    test_image(args["img_location"])