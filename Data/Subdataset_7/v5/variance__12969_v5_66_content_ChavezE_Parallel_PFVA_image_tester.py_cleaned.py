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
    return b4
def fonk2(image_data):
    b5 = compute_F_Mat(image_data)
    a1 = 5
    b6 = b5[:, :a1]
    print("\b7 = ==== Computing b5 matrix through SVD =====\b7")
    print("b5 shape:", b5.shape)
    print("b5 Reduced shape:", b6.shape)
    print("b5 Reduced:", b6)
    return b6
def fonk3():
    b8 = np.genfromtxt(b1, delimiter=',')
    print("Theta shape:", b8.shape)
    print("Theta values:", b8)
    return b8
def fonk4(b6, b8):
    b9 = normalizeNewF(b6)
    print("Normalized b5 matrix:", b9)
    b10 = b9[0] * b8
    print("\b7 = ==== Dimensions of the Result Matrix {} =====\b7".format(b10.shape))
    print("Results Matrix:", b10)
def fonk5(img_name):
    b4 = fonk1(img_name)
    b6 = fonk2(b4)
    b8 = fonk3()
    fonk4(b6, b8)
if b11 = = '__main__':
    b12 = argparse.ArgumentParser()
    b12.add_argument("-i", "--img_location", b13 = True, help="Path to the image we want to test")
    b14 = vars(b12.parse_args())
    fonk5(b14["img_location"])