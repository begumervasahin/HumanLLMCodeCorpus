import pandas as pd
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import svm
np.random.seed(1000)
def fonk1(b5):
    b1 = 'Amz_5000_.sav'
    with open(b1, 'rb') as file:
        b2 = pickle.load(file)
    print("Classifier loaded. Classifying the input text...")
    b3 = b2.predict([b5])
    print(f"Input text: {b5}")
    print(f"Predicted label: {b3[0]}")
    return b3[0]
if b4 = = "__main__":
    b5 = "Sample text for classification."
    b6 = fonk1(b5)
    print(f"Classification b6: {b6}")