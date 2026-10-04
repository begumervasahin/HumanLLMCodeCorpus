import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import string
import sklearn
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.b6 import Pipeline
b1 = pd.read_csv('/Users/dineshmaharana/jup/proj_spam_ham/smsspamcollection/SMSSpamCollection',sep = '\t',names = ["label","message"])
b1['length']= b1['message'].apply(len)
b1['length'].plot(b2 = 50,kind = 'hist')
b1.hist(b3 = 'length',by ='label',b2 =50,figsize = (12,6))
def fonk1(mess):
    b4 = [char for char in mess if char not in string.punctuation]
    b4 = ''.join(b4)
    b5 = [word for word in b4.split() if word.lower() not in stopwords.words('english')]
    return b5
b6 = Pipeline([('bow',CountVectorizer(analyzer = text_process)),
                     ('tfidf',TfidfTransformer()),
                     ('classifier',MultinomialNB()),
                     ])
msg_train,msg_test,label_train,b7 = train_test_split(b1['message'],b1['label'],test_size = 0.2)
b6.fit(msg_train,label_train)
b8 = b6.predict(msg_test)
print("CLASSIFICATION REPORT")
from sklearn.metrics import classification_report
print(classification_report(b8,b7))
from sklearn.metrics import accuracy_score
print("ACCURACY")
print(sklearn.metrics.accuracy_score(b8,b7))