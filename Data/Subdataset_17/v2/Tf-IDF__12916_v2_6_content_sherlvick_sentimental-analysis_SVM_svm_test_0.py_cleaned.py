import pandas as pd
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import svm
np.random.seed(1000)
def classify_text(text):
    test_data = [text]
    print("Test data:", test_data, '\n')
    model_filename = 'Amz_5000_.sav'
    with open(model_filename, 'rb') as model_file:
        classifier = pickle.load(model_file)
    print("Classifier loaded! \nClassifying test set...")
    prediction = classifier.predict(test_data)
    print("Prediction:", prediction, '\n')
    return prediction
if __name__ == "__main__":
    input_text = input("Enter the text to classify: ")
    result = classify_text(input_text)
    print("Result:", result)