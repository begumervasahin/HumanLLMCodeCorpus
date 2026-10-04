import pickle
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn import svm
np.random.seed(1000)
def load_classifier(filename):
    with open(filename, 'rb') as file:
        classifier = pickle.load(file)
    return classifier
def classify_text(classifier, text):
    test_data = [text]
    print("Test data:", test_data, '\n')
    print("Classifying test set...")
    prediction = classifier.predict(test_data)
    print("Prediction:", prediction, '\n')
    return prediction
if __name__ == "__main__":
    model_filename = 'Amz_5000_.sav'
    print("Loading classifier...")
    classifier = load_classifier(model_filename)
    print("Classifier loaded!")
    input_text = input("Enter the text to classify: ")
    result = classify_text(classifier, input_text)
    print("Result:", result)