import pandas as pd
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import svm
np.random.seed(1000)
def testing(anal1):
    my_test_data = [anal1]
    print("Test data:", my_test_data, '\n')
    filename = 'Amz_5000_.sav'
    with open(filename, 'rb') as file:
        my_clf = pickle.load(file)
    print("Classifier loaded! \nClassifying test set...")
    predicted = my_clf.predict(my_test_data)
    print("Prediction:", predicted, '\n')
    return predicted
if __name__ == "__main__":
    input_text = input("Enter the text to classify: ")
    result = testing(input_text)
    print("Result:", result)