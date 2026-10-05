import pandas as pd
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import svm
np.random.seed(1000)
def fonk1(text):
    b1 = [text]
    b2 = 'Amz_5000_.sav'
    with open(b2, 'rb') as model_file:
        b3 = pickle.load(model_file)
    print("Classifying the input text...")
    b4 = b3.predict(b1)
    return b4
if b5 = = "__main__":
    b6 = input("Enter the text you want to classify: ")
    b4 = fonk1(b6)
    print("Predicted label:", b4)