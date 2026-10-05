import pandas as pd
import sys
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import svm
np.random.seed(1000)
def testing(anal1):
    my_test_data = []
    my_test_data.append(anal1)
    print(my_test_data, '\n')
    filename = 'Amz_5000_.sav'
    my_clf = pickle.load(open(filename, 'rb'))
    print("Done! \nClassifying test set...")
    predicted = my_clf.predict(my_test_data)
    print(predicted, '\n')
    return predicted
if __name__ == "__main__":
    input_string = input("Enter the text for classification: ")
    result = testing(input_string)
import pandas as pd
import sys
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import svm
np.random.seed(1000)
def testing(anal1):
    my_test_data = []
    my_test_data.append(anal1)
    print(my_test_data, '\n')
    filename = 'Amz_5000_.sav'
    my_clf = pickle.load(open(filename, 'rb'))
    print("Done! \nClassifying test set...")
    predicted = my_clf.predict(my_test_data)
    print(predicted, '\n')
    return predicted
if __name__ == "__main__":
    input_string = input("Enter the text for classification: ")
    result = testing(input_string)