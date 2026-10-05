import argparse
import cv2
import imutils
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True, help="path to trained model")
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
orig = image.copy()
image = cv2.resize(image, (28, 28))
image = image.astype("float") / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis=0)
print("[INFO] Loading the network model...")
model = load_model(args["model"])
(not_aesthetic, aesthetic) = model.predict(image)[0]
label = "Aesthetic" if aesthetic > not_aesthetic else "Not Aesthetic"
proba = aesthetic if aesthetic > not_aesthetic else not_aesthetic
label = "{}: {:.2f}%".format(label, proba * 100)
output = imutils.resize(orig, width=400)
cv2.putText(output, label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Output", output)
cv2.waitKey(0)