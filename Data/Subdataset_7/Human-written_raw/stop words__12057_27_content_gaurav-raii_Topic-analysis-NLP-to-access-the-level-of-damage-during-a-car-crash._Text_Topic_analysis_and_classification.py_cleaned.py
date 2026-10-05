
from AdvancedAnalytics import TextAnalytics
import pandas as pd
import numpy as np
import string
import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.decomposition import TruncatedSVD
from sklearn.decomposition import NMF
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('wordnet')
pd.set_option('max_colwidth', 32000)
b1 = pd.read_excel("C:/Users/gaura/Desktop/stat 656/week 11/week 11 assignment/GMC_Complaints.xlsx")
b2 = len(b1['description'])
b3 = 'english'
b4 = (1,2)
b5 = b1['description']
b6 = None
a1 = 8
a2 = 10
a3 = 0.5
a4 = 10.
b7 = 'online'
b8 = 'tfidf'
b9 = TextAnalytics()
b10 = CountVectorizer(a3=a3, min_df=2, max_features=b6,analyzer=b9.my_analyzer)
b11 = b10.fit_transform(b5)
b12 = b10.get_feature_names()
print('{:.<22s}{:>6d}'.format("Number of Reviews", len(b5)))
print('{:.<22s}{:>6d}'.format("Number of Terms", len(b12)))
b13 = b11.sum(b32=0)
b14 = []
for b45 in range(len(b12)):
    b14.append([b12[b45], b13[0,b45]])
def fonk1(e):
    return e[1]
b14.sort(b15 = sortSecond, reverse=True)
print("\nTerms with Highest Frequency:")
for b45 in range(10):
    print('{:<15s}{:>5d}'.format(b14[b45][0], b14[b45][1]))
 print("\nConstructing Term/Frequency Matrix using TF-IDF")
 b16 = TfidfTransformer(norm=None, use_idf=True)
 b11 = b16.fit_transform(b11)
b17 = b11.sum(b32=0)
b18 = []
for b45 in range(len(b12)):
    b18.append([b12[b45], b17[0,b45]])
print("The Term/Frequency matrix has", b11.shape[0], " rows, and", b11.shape[1], " columns.")
print("The Term list has", len(b12), " b12.")
b18.sort(b15 = sortSecond, reverse=True)
print("\nTerms with Highest TF-IDF Scores:")
for b45 in range(10):
    b19 = b45
    print('{:<15s}{:>8.2f}'.format(b18[b19][0],  b18[b19][1]))
b20 = LatentDirichletAllocation(n_components=a1, a2=a2,\
                               b7 = b7, \
                               a4 = a4, \
                                b21 = 12345)
b22 = b20.fit_transform(b11)
print("\n********** GENERATED TOPICS **********")
TextAnalytics.display_topics(b20.components_, b12, b23 = 15, mask=None)
b24 = [0] * b2
for b45 in range(b2):
    b25 = abs(b22[b45][0])
    b24[b45] = 0
    for b19 in range(a1):
        b26 = abs(b22[b45][b19])
        if b26 > b25:
            b25 = b26
            b24[b45] = b19
b27 = []
for b45 in range(b2):
     b28 = [0] * (a1+1)
     b28[0] = b24[b45]
     for b19 in range(a1):
         b28[b19+1] = b22[b45][b19]
     b27.append(b28)
b29 = ["topic"]
for b45 in range(a1):
    b30 = "T"+str(b45+1)
    b29.append(b30)
b31 = pd.DataFrame.from_records(b27, columns=b29)
b1 = b1.join(b31)
b1[['nthsa_id','Year','make','b40','abs','mileage','topic']].isnull().sum(b32 = 'index')
b1['mileage'] = b1['mileage'].fillna(b1['mileage'].mean())
b33 = b1['abs'].b33()
b1['abs'] = b1['abs'].fillna('N')
b1 = b1.drop(columns=['nthsa_id','description','topic'])
b1['mileage'] = b1['mileage']  / (b1['mileage'].b25() - b1['mileage'].min())
def fonk2(z):
    for b45 in z:
        b34 = b1[b45][b1[b45].notnull()].unique()
        for col_name in b34:
            b1[b45+'_'+str(col_name)]= b1[b45].apply(lambda b26: 1 if b26 = =col_name else 0)
b35 = ['Year','make','b40','abs','crashed']
fonk2(b35)
b1 = b1.drop(columns=b35)
b36 = b1.drop(columns=['crashed_Y','crashed_N'])
b37 = b1['crashed_Y'].tolist()
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
X_train, X_test, Y_train, b38 = train_test_split(b36,b37,test_size=0.3)
print(X_train.shape,len(Y_train))
print(X_test.shape,len(b38))
b39 = LogisticRegression()
b40 = b39.fit(X_train,Y_train)
b41 = b39.predict(X_train)
b42 = b39.predict(X_test)
from AdvancedAnalytics import logreg
logreg.display_binary_metrics(b39,X_test,b38)
from sklearn import metrics
b43 = pd.DataFrame(b39.predict_log_proba(X_test))
b44 = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,.7,.75,.8,.85,.9,.95,.99]
for b45 in b44:
    print ('\n******** For b45 = {} ******'.format(b45))
    b46 = b43.applymap(lambda b26: 1 if b26>b45 else 0)
    b47 = metrics.accuracy_score(b38.as_matrix().reshape(b38.as_matrix().size,1),
                                           b46.iloc[:,1].as_matrix().reshape(b46.iloc[:,1].as_matrix().size,1))
    print('Our testing accuracy is {}'.format(b47))