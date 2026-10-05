from keras.preprocessing.b5 import img_to_array
import keras
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2
b1 = argparse.ArgumentParser()
b1.add_argument("-m", "--b7", b2 = True,
	b3 = "path to trained b7 b7")
b1.add_argument("-i", "--b5", b2 = True,
	b3 = "path to input b5")
b4 = vars(b1.parse_args())
b5 = cv2.imread(b4["b5"])
b6 = b5.copy()
b5 = cv2.resize(b5, (28, 28))
b5 = b5.astype("float") / 255.0
b5 = img_to_array(b5)
b5 = np.expand_dims(b5, axis=0)
print("[Loading the network b7...")
b7 = load_model(b4["b7"])
(notaesthetic, aesthetic) = b7.predict(b5)[0]
b8 = "Aesthetic" if aesthetic > notaesthetic else "Not Aesthetic"
b9 = aesthetic if aesthetic > notaesthetic else notaesthetic
b8 = "{}: {:.2f}%".format(b8, b9 * 100)
b10 = imutils.resize(b6, width=400)
cv2.putText(b10, b8, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
	0.7, (0, 255, 0), 2)
cv2.imshow("Output", b10)
cv2.waitKey(0)