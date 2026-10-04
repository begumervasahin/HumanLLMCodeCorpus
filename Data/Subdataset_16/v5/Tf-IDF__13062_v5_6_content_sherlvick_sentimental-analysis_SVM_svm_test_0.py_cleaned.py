import pandas as pd
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import svm
np.random.seed(1000)
def fonk1(b3):
    with open(b3, 'rb') as file:
        b1 = pickle.load(file)
    return b1
def fonk2(b1, b4):
    b2 = b1.predict([b4])
    return b2[0]
def fonk3():
    b3 = 'Amz_5000_.sav'
    b4 = "Sample text for classification."
    b1 = fonk1(b3)
    print("Classifier loaded. Classifying the input text...")
    b2 = fonk2(b1, b4)
    print(f"Input text: {b4}")
    print(f"Predicted label: {b2}")
if b5 = = "__main__":
    fonk3()