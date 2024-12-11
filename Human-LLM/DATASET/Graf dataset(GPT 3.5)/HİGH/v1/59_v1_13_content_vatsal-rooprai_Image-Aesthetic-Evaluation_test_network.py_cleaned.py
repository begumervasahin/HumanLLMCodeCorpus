import argparse
import cv2
import imutils
import numpy as np
from keras.models import load_model
from keras.preprocessing.b4 import img_to_array
b1 = argparse.ArgumentParser()
b1.add_argument("-m", "--b6", b2 = True, help="path to trained b6")
b1.add_argument("-i", "--b4", b2 = True, help="path to input b4")
b3 = vars(b1.parse_args())
b4 = cv2.imread(b3["b4"])
b5 = b4.copy()
b4 = cv2.resize(b4, (28, 28))
b4 = b4.astype("float") / 255.0
b4 = img_to_array(b4)
b4 = np.expand_dims(b4, axis=0)
print("[INFO] Loading the network b6...")
b6 = load_model(b3["b6"])
(not_aesthetic, aesthetic) = b6.predict(b4)[0]
b7 = "Aesthetic" if aesthetic > not_aesthetic else "Not Aesthetic"
b8 = aesthetic if aesthetic > not_aesthetic else not_aesthetic
b7 = "{}: {:.2f}%".format(b7, b8 * 100)
b9 = imutils.resize(b5, width=400)
cv2.putText(b9, b7, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Output", b9)
cv2.waitKey(0)