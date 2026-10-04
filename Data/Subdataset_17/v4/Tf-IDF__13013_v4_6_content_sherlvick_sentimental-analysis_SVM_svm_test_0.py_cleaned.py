import pandas as pd
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import svm
np.random.seed(1000)
def testing(input_text):
    filename = 'Amz_5000_.sav'
    with open(filename, 'rb') as file:
        classifier = pickle.load(file)
    print("Classifier loaded. Classifying the input text...")
    predicted_label = classifier.predict([input_text])
    print(f"Input text: {input_text}")
    print(f"Predicted label: {predicted_label[0]}")
    return predicted_label[0]
if __name__ == "__main__":
    input_text = "Sample text for classification."
    result = testing(input_text)
    print(f"Classification result: {result}")