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
b1 = 'b8.csv'
def fonk1(img_name):
    b2 = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
    b3 = np.reshape(b2, (1, 256*256))
    b4 = centerData(b3)
    print("Subset of centered image data:", b4[0, 40000:40500])
    print("\b5 = ==== Computing b6 matrix through SVD =====\b5")
    b6 = compute_F_Mat(b4)
    a1 = 5
    b7 = b6[:, :a1]
    b8 = np.genfromtxt(b1, delimiter=',')
    print("b6 shape:", b6.shape)
    print("b6 Reduced shape:", b7.shape)
    print("b6 Reduced:", b7)
    print("Theta shape:", b8.shape)
    b9 = normalizeNewF(b7)
    print("Normalized b6 matrix:", b9)
    print("Theta values:", b8)
    b10 = b9[0] * b8
    print("\b5 = ==== Dimensions of the Result Matrix {} =====\b5".format(b10.shape))
    print("Results Matrix:", b10)
if b11 = = '__main__':
    b12 = argparse.ArgumentParser()
    b12.add_argument("-i", "--img_location", b13 = True, help="Path to the image we want to test")
    b14 = vars(b12.parse_args())
    fonk1(b14["img_location"])