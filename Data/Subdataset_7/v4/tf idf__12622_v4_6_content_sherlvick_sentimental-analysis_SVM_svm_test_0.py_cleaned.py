import pandas as pd
import sys
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import svm
np.random.seed(1000)
def fonk1(anal1):
    b1 = [anal1]
    print("Test Data:", b1)
    b2 = 'Amz_5000_.sav'
    with open(b2, 'rb') as file:
        b3 = pickle.load(file)
    print("Model Loaded. Classifying test set...")
    b4 = b3.predict(b1)
    print("Predicted Labels:", b4)
    return b4
