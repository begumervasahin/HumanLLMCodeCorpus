import sys
import nltk
import numpy as np
import cPickle as pickle
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
nltk.download('stopwords')
b1 = set(stopwords.words('english'))
b2 = SnowballStemmer('english')
with open('model/vector/vector.pkl', 'rb') as file:
    b3 = pickle.load(file)
b4 = open(str(sys.argv[1]) + '_twt')
b5 = open(str(sys.argv[2]), 'w')
b6 = b3.transform(b4)
b4.close()
with open('model/binary_lin.pkl', 'rb') as file:
    b7 = pickle.load(file)
b8 = b7.predict(b6)
for prediction in b8:
    b5.write(str(prediction) + '\n')
b5.close()