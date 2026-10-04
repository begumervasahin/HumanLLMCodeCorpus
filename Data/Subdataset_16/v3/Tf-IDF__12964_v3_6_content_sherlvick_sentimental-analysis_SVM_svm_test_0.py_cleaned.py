import pickle
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn import svm
np.random.seed(1000)
def fonk1(filename):
    with open(filename, 'rb') as file:
        b1 = pickle.load(file)
    return b1
def fonk2(b1, text):
    b2 = [text]
    print("Test data:", b2, '\n')
    print("Classifying test set...")
    b3 = b1.predict(b2)
    print("Prediction:", b3, '\n')
    return b3
if b4 = = "__main__":
    b5 = 'Amz_5000_.sav'
    print("Loading b1...")
    b1 = fonk1(b5)
    print("Classifier loaded!")
    b6 = input("Enter the text to classify: ")
    b7 = fonk2(b1, b6)
    print("Result:", b7)