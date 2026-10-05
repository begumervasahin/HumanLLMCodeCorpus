import matplotlib.pyplot as plt
import numpy as np
import os
import random
import cv2
import argparse
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from pyimagesearch.lenet import LeNet
from imutils import paths
import matplotlib
matplotlib.use("Agg")
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dataset", required=True, help="path to input dataset")
    parser.add_argument("-m", "--model", required=True, help="path to output model")
    parser.add_argument("-p", "--plot", type=str, default="plot.png", help="path to output loss/accuracy plot")
    return parser.parse_args()
EPOCHS = 25
INIT_LR = 1e-3
BS = 32
def load_and_preprocess_data(dataset_path):
    print("Loading images...")
    data = []
    labels = []
    imagePaths = sorted(list(paths.list_images(dataset_path)))
    random.seed(42)
    random.shuffle(imagePaths)
    for imagePath in imagePaths:
        image = cv2.imread(imagePath)
        image = cv2.resize(image, (28, 28))
        image = img_to_array(image)
        data.append(image)
        label = imagePath.split(os.path.sep)[-2]
        label = 1 if label == "aesthetic" else 0
        labels.append(label)
    data = np.array(data, dtype="float") / 255.0
    labels = np.array(labels)
    return data, labels
def split_dataset(data, labels):
    return train_test_split(data, labels, test_size=0.25, random_state=42)
def data_augmentation():
    return ImageDataGenerator(rotation_range=30, width_shift_range=0.1, height_shift_range=0.1,
                              shear_range=0.2, zoom_range=0.2, horizontal_flip=True, fill_mode="nearest")
def compile_model():
    print("Compiling the model...")
    model = LeNet.build(width=28, height=28, depth=3, classes=2)
    opt = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)
    model.compile(loss="binary_crossentropy", optimizer=opt, metrics=["accuracy"])
    return model
def train_model(model, aug, trainX, trainY, testX, testY):
    print("Training the model...")
    H = model.fit_generator(aug.flow(trainX, trainY, batch_size=BS), validation_data=(testX, testY),
                            steps_per_epoch=len(trainX)
    return H
def save_model(model, model_path):
    print("Saving the model...")
    model.save(model_path)
def plot_training_performance(history, plot_path):
    print("Plotting the training loss and accuracy...")
    plt.style.use("ggplot")
    plt.figure()
    N = EPOCHS
    plt.plot(np.arange(0, N), history.history["loss"], label="train_loss")
    plt.plot(np.arange(0, N), history.history["val_loss"], label="val_loss")
    plt.plot(np.arange(0, N), history.history["acc"], label="train_acc")
    plt.plot(np.arange(0, N), history.history["val_acc"], label="val_acc")
    plt.title("Training Loss and Accuracy on Aesthetic/Not Aesthetic")
    plt.xlabel("Epoch")
    plt.ylabel("Loss/Accuracy")
    plt.legend(loc="lower left")
    plt.savefig(plot_path)
def main():
    args = parse_arguments()
    data, labels = load_and_preprocess_data(args.dataset)
    trainX, testX, trainY, testY = split_dataset(data, labels)
    aug = data_augmentation()
    model = compile_model()
    history = train_model(model, aug, trainX, trainY, testX, testY)
    save_model(model, args.model)
    plot_training_performance(history, args.plot)
if __name__ == "__main__":
    main()