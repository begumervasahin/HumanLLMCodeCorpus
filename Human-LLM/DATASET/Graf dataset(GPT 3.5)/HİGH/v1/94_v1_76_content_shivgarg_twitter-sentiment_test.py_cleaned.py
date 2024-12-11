import sys
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import cPickle
nltk.download('stopwords')
with open('model/vector/vector.pkl', 'rb') as v:
    b1 = cPickle.load(v)
b2 = sys.argv[1] + '_twt'
b3 = sys.argv[2]
with open(b2, 'r') as f:
    b4 = f.readlines()
b5 = b1.transform(b4)
with open('model/binary_lin.pkl', 'rb') as svm_model_file:
    b6 = cPickle.load(svm_model_file)
b7 = b6.predict(b5)
with open(b3, 'w') as g:
    for pred in b7:
        g.write(str(pred) + '\n')
print("Predictions written to", b3)