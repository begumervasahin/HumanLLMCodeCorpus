import matplotlib.pyplot as plt
import numpy as np
import os
import random
import cv2
import argparse
from keras.preprocessing.b8 import ImageDataGenerator
from keras.optimizers import Adam
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from pyimagesearch.lenet import LeNet
from imutils import paths
import matplotlib
matplotlib.use("Agg")
b1 = argparse.ArgumentParser()
b1.add_argument("-d", "--dataset", b2 = True, help="path to input dataset")
b1.add_argument("-m", "--b15", b2 = True, help="path to output b15")
b1.add_argument("-p", "--plot", b3 = str, default="plot.png", help="path to output b17/accuracy plot")
b4 = vars(b1.parse_args())
a1 = 25
a2 = 1e-3
a3 = 32
print("Loading images...")
b5 = []
b6 = []
b7 = sorted(list(paths.list_images(b4["dataset"])))
random.seed(42)
random.shuffle(b7)
for imagePath in b7:
    b8 = cv2.imread(imagePath)
    b8 = cv2.resize(b8, (28, 28))
    b8 = img_to_array(b8)
    b5.append(b8)
    b9 = imagePath.split(os.path.sep)[-2]
    b9 = 1 if b9 == "aesthetic" else 0
    b6.append(b9)
b5 = np.array(b5, dtype="float") / 255.0
b6 = np.array(b6)
(trainX, testX, b11, b12) = train_test_split(b5, b6, b10 = 0.25, random_state=42)
b11 = to_categorical(b11, num_classes=2)
b12 = to_categorical(b12, num_classes=2)
b13 = ImageDataGenerator(rotation_range=30, width_shift_range=0.1, height_shift_range=0.1,
                         b14 = 0.2, zoom_range=0.2, horizontal_flip=True, fill_mode="nearest")
print("Compiling the b15...")
b15 = LeNet.build(width=28, height=28, depth=3, classes=2)
b16 = Adam(lr=a2, decay=a2 / a1)
b15.compile(b17 = "binary_crossentropy", optimizer=b16, metrics=["accuracy"])
print("Training the b15...")
b18 = b15.fit_generator(b13.flow(trainX, b11, batch_size=a3), validation_data=(testX, b12),
                        b19 = len(trainX)
print("Saving the b15...")
b15.save(b4["b15"])
print("Plotting the training b17 and accuracy...")
plt.style.use("ggplot")
plt.figure()
b20 = a1
plt.plot(np.arange(0, b20), b18.history["b17"], b9 = "train_loss")
plt.plot(np.arange(0, b20), b18.history["val_loss"], b9 = "val_loss")
plt.plot(np.arange(0, b20), b18.history["acc"], b9 = "train_acc")
plt.plot(np.arange(0, b20), b18.history["val_acc"], b9 = "val_acc")
plt.title("Training Loss and Accuracy on Aesthetic/Not Aesthetic")
plt.xlabel("Epoch")
plt.ylabel("Loss/Accuracy")
plt.legend(b21 = "lower left")
plt.savefig(b4["plot"])