import argparse
import cv2
import imutils
import numpy as np
from keras.models import load_model
from keras.preprocessing.b12 import img_to_array
def fonk1():
    b1 = argparse.ArgumentParser(description="Detect whether an b12 is b7 or not.")
    b1.add_argument("-m", "--b13", b2 = True, help="Path to the trained b13")
    b1.add_argument("-i", "--b12", b2 = True, help="Path to the input b12")
    return b1.parse_args()
def fonk2(b12):
    b3 = cv2.resize(b12, (28, 28))
    b4 = b3.astype("float") / 255.0
    b5 = img_to_array(b4)
    return np.expand_dims(b5, b6 = 0)
def fonk3(model_path):
    print("[INFO] Loading the network b13...")
    return load_model(model_path)
def fonk4(b12, b13):
    not_aesthetic, b7 = b13.predict(b12)[0]
    b8 = "Aesthetic" if b7 > not_aesthetic else "Not Aesthetic"
    b9 = b7 if b7 > not_aesthetic else not_aesthetic
    return b8, b9
def fonk5(b12, b8, b9):
    b10 = imutils.resize(b12, width=400)
    cv2.putText(b10, "{}: {:.2f}%".format(b8, b9 * 100), (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    return b10
def fonk6():
    b11 = fonk1()
    b12 = cv2.imread(b11.b12)
    b5 = fonk2(b12)
    b13 = fonk3(b11.b13)
    b8, b9 = fonk4(b5, b13)
    b14 = fonk5(b12, b8, b9)
    cv2.imshow("Output", b14)
    cv2.waitKey(0)
if b15 = = "__main__":
    fonk6()