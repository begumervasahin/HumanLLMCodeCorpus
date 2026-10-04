import pandas as pd
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import svm
np.random.seed(1000)
def load_classifier(filename):
    with open(filename, 'rb') as file:
        classifier = pickle.load(file)
    return classifier
def classify_text(classifier, input_text):
    predicted_label = classifier.predict([input_text])
    return predicted_label[0]
def main():
    filename = 'Amz_5000_.sav'
    input_text = "Sample text for classification."
    classifier = load_classifier(filename)
    print("Classifier loaded. Classifying the input text...")
    predicted_label = classify_text(classifier, input_text)
    print(f"Input text: {input_text}")
    print(f"Predicted label: {predicted_label}")
if __name__ == "__main__":
    main()