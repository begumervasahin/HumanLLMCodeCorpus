import pandas as pd
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import svm
np.random.seed(1000)
def fonk1(anal1):
    b1 = [anal1]
    print("Test data:", b1, '\n')
    b2 = 'Amz_5000_.sav'
    with open(b2, 'rb') as file:
        b3 = pickle.load(file)
    print("Classifier loaded! \nClassifying test set...")
    b4 = b3.predict(b1)
    print("Prediction:", b4, '\n')
    return b4
if b5 = = "__main__":
    b6 = input("Enter the text to classify: ")
    b7 = fonk1(b6)
    print("Result:", b7)