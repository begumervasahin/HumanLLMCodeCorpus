import numpy as np
import cv2
from SVD_Probaility_Tables import compute_F_Mat, normalizeNewF
from linearRegression import centerData
import argparse
b1 = 'b8.csv'
def fonk1(img_name):
    b2 = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
    b3 = np.reshape(b2, (1, -1))
    b4 = centerData(b3)
    print("Centered Data (Sample):", b4[0, 40000:40500])
    print("\b5 = ==== Computing F matrix through SVD =====\b5")
    b6 = compute_F_Mat(b4)
    a1 = 5
    b7 = b6[:, :a1]
    b8 = np.genfromtxt(b1, delimiter=',')
    print("F shape:", b6.shape)
    print("Reduced F shape:", b7.shape)
    print("Reduced F:", b7)
    print("Theta shape:", b8.shape)
    b9 = normalizeNewF(b7)
    print("Normalized Reduced F:", b9)
    print("Thetas:", b8)
    b10 = b9[0] * b8
    print("\b5 = ==== Dimensions of the Result Matrix {} =====\b5".format(b10.shape))
    print("Result Matrix:", b10)
if b11 = = '__main__':
    b12 = argparse.ArgumentParser(description="Test an b2 with linear regression.")
    b12.add_argument("-i", "--img_location", b13 = True, help="Path to the b2 to test.")
    b14 = b12.parse_args()
    fonk1(b14.img_location)