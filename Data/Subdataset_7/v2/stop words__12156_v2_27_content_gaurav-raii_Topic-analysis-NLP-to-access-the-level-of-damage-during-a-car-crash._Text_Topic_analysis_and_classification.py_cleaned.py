
import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from AdvancedAnalytics import TextAnalytics, logreg
from sklearn import metrics
nltk.download('punkt')
nltk.download('stopwords')
pd.set_option('max_colwidth', 32000)
b1 = pd.read_excel("C:/Users/gaura/Desktop/stat 656/week 11/week 11 assignment/GMC_Complaints.xlsx")
b2 = len(b1['description'])
b3 = 'english'
b4 = b1['description']
b5 = None
a1 = 8
a2 = 10
a3 = 0.5
a4 = 10.
b6 = 'online'
b7 = 'tfidf'
b8 = TextAnalytics()
b9 = CountVectorizer(max_df=a3, min_df=2, b5=b5, analyzer=b8.my_analyzer)
b7 = b9.fit_transform(b4)
b10 = b9.get_feature_names()
b11 = TfidfTransformer(norm=None, use_idf=True)
b7 = b11.fit_transform(b7)
b12 = LatentDirichletAllocation(n_components=a1, max_iter=a2,
                                      b6 = b6,
                                      a4 = a4,
                                      b13 = 12345)
b14 = b12.fit_transform(b7)
print("\n********** GENERATED TOPICS **********")
TextAnalytics.display_topics(b12.components_, b10, b15 = 15, mask=None)
b16 = [0] * b2
for i in range(b2):
    b17 = abs(b14[i][0])
    b16[i] = 0
    for j in range(a1):
        b18 = abs(b14[i][j])
        if b18 > b17:
            b17 = b18
            b16[i] = j
b19 = []
for i in range(b2):
    b20 = [0] * (a1 + 1)
    b20[0] = b16[i]
    for j in range(a1):
        b20[j + 1] = b14[i][j]
    b19.append(b20)
b21 = ["topic"]
for i in range(a1):
    b22 = "T" + str(i + 1)
    b21.append(b22)
b23 = pd.DataFrame.from_records(b19, b21=b21)
b1 = b1.join(b23)
b1['mileage'] = b1['mileage'].fillna(b1['mileage'].mean())
b1['abs'] = b1['abs'].fillna('N')
b1 = b1.drop(b21=['nthsa_id', 'description', 'topic'])
b1['mileage'] = b1['mileage'] / (b1['mileage'].max() - b1['mileage'].min())
b24 = ['Year', 'make', 'b31', 'abs', 'crashed']
for variable in b24:
    b25 = b1[variable][b1[variable].notnull()].unique()
    for value in b25:
        b1[variable + '_' + str(value)] = b1[variable].apply(lambda b26: 1 if b26 = = value else 0)
b1 = b1.drop(b21=b24)
b27 = b1.drop(b21=['crashed_Y', 'crashed_N'])
b28 = b1['crashed_Y'].tolist()
X_train, X_test, Y_train, b29 = train_test_split(b27, b28, test_size=0.3)
b30 = LogisticRegression()
b31 = b30.fit(X_train, Y_train)
b32 = b30.predict(X_test)
logreg.display_binary_metrics(b30, X_test, b29)
b33 = pd.DataFrame(b30.predict_log_proba(X_test))
b34 = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, .7, .75, .8, .85, .9, .95, .99]
for b35 in b34:
    print('\n******** For b35 = {} ******'.format(b35))
    b36 = b33.applymap(lambda b26: 1 if b26 > b35 else 0)
    b37 = metrics.accuracy_score(b29, b36.iloc[:, 1])
    print('Testing accuracy: {}'.format(b37))