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
def test_image(img_name):
    cur_img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
    img_row = np.reshape(cur_img, (1, 256*256))
    Xc = centerData(img_row)
    print("Subset of centered image data:", Xc[0, 40000:40500])
    print("\n===== Computing F matrix through SVD =====\n")
    F = compute_F_Mat(Xc)
    K = 5
    Freduced = F[:, :K]
    thetas = np.genfromtxt(THETA_FILE, delimiter=',')
    print("F shape:", F.shape)
    print("F Reduced shape:", Freduced.shape)
    print("F Reduced:", Freduced)
    print("Theta shape:", thetas.shape)
    FreducedNorm = normalizeNewF(Freduced)
    print("Normalized F matrix:", FreducedNorm)
    print("Theta values:", thetas)
    resultsMatrix = FreducedNorm[0] * thetas
    print("\n===== Dimensions of the Result Matrix {} =====\n".format(resultsMatrix.shape))
    print("Results Matrix:", resultsMatrix)
if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--img_location", required=True, help="Path to the image we want to test")
    args = vars(ap.parse_args())
    test_image(args["img_location"])