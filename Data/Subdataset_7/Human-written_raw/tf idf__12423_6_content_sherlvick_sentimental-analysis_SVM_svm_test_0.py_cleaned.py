import pandas as pd
import sys
import pickle
from numpy import loadtxt
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import svm
np.random.seed(1000)
def fonk1(anal1):
    b1 = []
    '''
    b2 = [ ]
    b3 = int(input("1.For GOOD - 1 " + '\n'"2.For BAD - 0 "+'\n'))
    if b3 = = 1:
        b2.append("__label__2 ")
    elif b3 = = 0:
        b2.append("__label__1 ")
    '''
    b1.append(anal1)
    print(b1, '\n')
    b4 = 'Amz_5000_.sav'
    b5 = pickle.load(open(b4, 'rb'))
    print("Done! \nClassifying test set...")
    b6 = b5.predict(b1)
    print(b6, '\n')
    '''
    b7 = np.mean(b6 == b2)*100
    print('accuracy is : ',np.mean(b6 = = b2)*100)
    '''
    return b6