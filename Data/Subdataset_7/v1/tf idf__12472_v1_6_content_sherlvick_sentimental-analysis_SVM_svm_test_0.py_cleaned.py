import pandas as pd
import sys
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import svm
np.random.seed(1000)
def fonk1(anal1):
    b1 = []
    b1.append(anal1)
    print(b1, '\n')
    b2 = 'Amz_5000_.sav'
    b3 = pickle.load(open(b2, 'rb'))
    print("Done! \nClassifying test set...")
    b4 = b3.predict(b1)
    print(b4, '\n')
    return b4
if b5 = = "__main__":
    b6 = input("Enter the text for classification: ")
    b7 = fonk2(b6)
import pandas as pd
import sys
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import svm
np.random.seed(1000)
def fonk2(anal1):
    b1 = []
    b1.append(anal1)
    print(b1, '\n')
    b2 = 'Amz_5000_.sav'
    b3 = pickle.load(open(b2, 'rb'))
    print("Done! \nClassifying test set...")
    b4 = b3.predict(b1)
    print(b4, '\n')
    return b4
if b5 = = "__main__":
    b6 = input("Enter the text for classification: ")
    b7 = fonk2(b6)