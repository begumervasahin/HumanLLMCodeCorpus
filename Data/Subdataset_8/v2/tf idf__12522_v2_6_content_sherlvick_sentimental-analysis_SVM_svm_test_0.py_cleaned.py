import pandas as pd
import sys
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import svm
np.random.seed(1000)
def classify_text(text):
    test_data = [text]
    model_filename = 'Amz_5000_.sav'
    loaded_model = pickle.load(open(model_filename, 'rb'))
    print("Classifying the input text...")
    predicted_label = loaded_model.predict(test_data)
    return predicted_label
if __name__ == "__main__":
    input_text = input("Enter the text you want to classify: ")
    predicted_label = classify_text(input_text)
    print("Predicted label:", predicted_label)