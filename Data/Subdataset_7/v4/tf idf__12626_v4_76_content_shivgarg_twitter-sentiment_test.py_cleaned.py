import sys
import re
import nltk
import string
import operator
import random
import numpy as np
import cPickle as pickle
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, HashingVectorizer
from sklearn.model_selection import cross_val_score, ShuffleSplit
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, SnowballStemmer
from sklearn.externals import joblib
nltk.download('stopwords')
b1 = set(stopwords.words('english'))
b2 = SnowballStemmer('english')
with open('model/vector/vector.pkl', 'rb') as v:
    b3 = pickle.load(v)
b4 = open(str(sys.argv[1]) + '_twt')
b5 = open(str(sys.argv[2]), 'w')
b6 = b3.transform(b4)
b4.close()
with open('model/binary_lin.pkl', 'rb') as model_file:
    b7 = pickle.load(model_file)
b8 = b7.predict(b6)
for prediction in b8:
    b5.write(str(prediction) + '\n')
b5.close()