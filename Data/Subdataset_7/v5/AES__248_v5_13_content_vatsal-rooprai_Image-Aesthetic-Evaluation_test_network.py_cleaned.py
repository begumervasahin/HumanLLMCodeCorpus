import argparse
import cv2
import imutils
import numpy as np
from keras.models import load_model
from keras.preprocessing.b11 import img_to_array
def fonk1():
    b1 = argparse.ArgumentParser()
    b1.add_argument("-m", "--b13", b2 = True, help="Path to the trained b13")
    b1.add_argument("-i", "--b11", b2 = True, help="Path to the input b11")
    return b1.parse_args()
def fonk2(b11):
    b3 = cv2.resize(b11, (28, 28))
    b4 = b3.astype("float") / 255.0
    return np.expand_dims(img_to_array(b4), b5 = 0)
def fonk3(model_path):
    print("[INFO] Loading the network b13...")
    return load_model(model_path)
def fonk4(b11, b13):
    aesthetic_score, b6 = b13.predict(b11)[0]
    b7 = "Aesthetic" if aesthetic_score > b6 else "Not Aesthetic"
    b8 = aesthetic_score if aesthetic_score > b6 else b6
    return b7, b8
def fonk5(b11, b7, b8):
    b9 = imutils.resize(b11, width=400)
    cv2.putText(b9, "{}: {:.2f}%".format(b7, b8 * 100), (10, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    return b9
def fonk6():
    b10 = fonk1()
    b11 = cv2.imread(b10.b11)
    b12 = fonk2(b11)
    b13 = fonk3(b10.b13)
    b7, b8 = fonk4(b12, b13)
    b9 = fonk5(b11, b7, b8)
    cv2.imshow("Output", b9)
    cv2.waitKey(0)
if b14 = = "__main__":
    fonk6()