import pandas as pd
import numpy as np
import pickle
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
np.random.seed(1000)
def classify_review(review):
    test_data = [review]
    print("Test Data:", test_data)
    model_filename = 'Amz_5000_.sav'
    with open(model_filename, 'rb') as model_file:
        clf_model = pickle.load(model_file)
    print("Model Loaded. Classifying test set...")
    predicted_labels = clf_model.predict(test_data)
    print("Predicted Labels:", predicted_labels)
    return predicted_labels
