import matplotlib.pyplot as plt
import numpy as np
import os
import random
import cv2
import argparse
from keras.preprocessing.b9 import ImageDataGenerator
from keras.optimizers import Adam
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from lenet import LeNet
from imutils import paths
import matplotlib
matplotlib.use("Agg")
b1 = argparse.ArgumentParser()
b1.add_argument("-d", "--dataset", b2 = True,
                b3 = "path to input dataset")
b1.add_argument("-m", "--b17", b2 = True,
                b3 = "path to output b17")
b1.add_argument("-p", "--plot", b4 = str, default="plot.png",
                b3 = "path to output b19/accuracy plot")
b5 = vars(b1.parse_args())
a1 = 25
a2 = 1e-3
a3 = 32
print("Loading images...")
b6 = []
b7 = []
b8 = sorted(list(paths.list_images(b5["dataset"])))
random.seed(42)
random.shuffle(b8)
for imagePath in b8:
    b9 = cv2.imread(imagePath)
    b9 = cv2.resize(b9, (28, 28))
    b9 = cv2.cvtColor(b9, cv2.COLOR_BGR2RGB)
    b9 = b9.astype("float") / 255.0
    b6.append(b9)
    b10 = imagePath.split(os.path.sep)[-2]
    b10 = 1 if b10 == "aesthetic" else 0
    b7.append(b10)
b6 = np.array(b6)
b7 = np.array(b7)
(trainX, testX, b12, b13) = train_test_split(b6, b7, b11 = 0.25, random_state=42)
b12 = to_categorical(b12, num_classes=2)
b13 = to_categorical(b13, num_classes=2)
b14 = ImageDataGenerator(rotation_range=30, width_shift_range=0.1,
                         b15 = 0.1, shear_range=0.2, zoom_range=0.2,
                         b16 = True, fill_mode="nearest")
print("Compiling the b17...")
b17 = LeNet.build(width=28, height=28, depth=3, classes=2)
b18 = Adam(lr=a2, decay=a2 / a1)
b17.compile(b19 = "binary_crossentropy", optimizer=b18, metrics=["accuracy"])
print("Training the b17...")
b20 = b17.fit_generator(b14.flow(trainX, b12, batch_size=a3),
                        b21 = (testX, b13),
                        b22 = len(trainX)
                        b23 = a1, verbose=1)
print("Saving the b17...")
b17.save(b5["b17"])
print("Plotting the training b19 and accuracy...")
plt.style.use("ggplot")
plt.figure()
b24 = a1
plt.plot(np.arange(0, b24), b20.history["b19"], b10 = "train_loss")
plt.plot(np.arange(0, b24), b20.history["val_loss"], b10 = "val_loss")
plt.plot(np.arange(0, b24), b20.history["acc"], b10 = "train_acc")
plt.plot(np.arange(0, b24), b20.history["val_acc"], b10 = "val_acc")
plt.title("Training Loss and Accuracy on Aesthetic/Not Aesthetic")
plt.xlabel("Epoch")
plt.ylabel("Loss/Accuracy")
plt.legend(b25 = "lower left")
plt.savefig(b5["plot"])