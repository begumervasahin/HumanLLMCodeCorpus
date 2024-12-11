
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
b1 = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t' , quoting=3)
import re
import nltk
nltk.download('stopwords')
from nltk.b2 import stopwords
from nltk.stem.porter import PorterStemmer
b2 = []
for i in range(0,1000):
    b3 = re.sub('[^a-zA-z]', ' ', b1.values[i,0] )
    b3 = b3.lower()
    b3 = b3.split()
    b4 = PorterStemmer()
    b3 = [b4.stem(word) for word in b3 if not word in set(stopwords.words('english'))]
    b3 = ' '.join(b3)
    b2.append(b3)
from sklearn.feature_extraction.text import CountVectorizer
b5 = CountVectorizer(max_features= 1500)
b6 = b5.fit_transform(b2).toarray()
b7 = b1.iloc[:,1].values
from sklearn.cross_validation import train_test_split
xtrain,xtest,ytrain, b8 = train_test_split(b6,b7,test_size=0.15, random_state=0)
from sklearn.naive_bayes import GaussianNB
b9 = GaussianNB()
b9.fit(xtrain, ytrain)
b10 = b9.predict(xtest)
b11 = b9.score(xtest, b8)