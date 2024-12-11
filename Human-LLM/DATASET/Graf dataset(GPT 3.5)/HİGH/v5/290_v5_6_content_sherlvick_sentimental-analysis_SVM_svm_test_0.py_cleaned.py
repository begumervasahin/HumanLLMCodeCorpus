import pandas as pd
import numpy as np
import pickle
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
np.random.seed(1000)
def fonk1(review):
    b1 = [review]
    print("Test Data:", b1)
    b2 = 'Amz_5000_.sav'
    with open(b2, 'rb') as model_file:
        b3 = pickle.load(model_file)
    print("Model Loaded. Classifying test set...")
    b4 = b3.predict(b1)
    print("Predicted Labels:", b4)
    return b4
