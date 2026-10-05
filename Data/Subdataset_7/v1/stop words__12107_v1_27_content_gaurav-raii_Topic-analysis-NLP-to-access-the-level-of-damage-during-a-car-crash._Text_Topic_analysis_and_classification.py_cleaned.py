
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
b9 = CountVectorizer(a3=a3, min_df=2, max_features=b5, analyzer=b8.my_analyzer)
b10 = b9.fit_transform(b4)
b11 = b9.get_feature_names()
b12 = TfidfTransformer(norm=None, use_idf=True)
b10 = b12.fit_transform(b10)
b13 = LatentDirichletAllocation(n_components=a1, a2=a2,
                               b6 = b6,
                               a4 = a4,
                               b14 = 12345)
b15 = b13.fit_transform(b10)
print("\n********** GENERATED TOPICS **********")
TextAnalytics.display_topics(b13.components_, b11, b16 = 15, mask=None)
b17 = [0] * b2
for b36 in range(b2):
    b18 = abs(b15[b36][0])
    b17[b36] = 0
    for j in range(a1):
        b19 = abs(b15[b36][j])
        if b19 > b18:
            b18 = b19
            b17[b36] = j
b20 = []
for b36 in range(b2):
    b21 = [0] * (a1 + 1)
    b21[0] = b17[b36]
    for j in range(a1):
        b21[j + 1] = b15[b36][j]
    b20.append(b21)
b22 = ["topic"]
for b36 in range(a1):
    b23 = "T" + str(b36 + 1)
    b22.append(b23)
b24 = pd.DataFrame.from_records(b20, columns=b22)
b1 = b1.join(b24)
b1['mileage'] = b1['mileage'].fillna(b1['mileage'].mean())
b1['abs'] = b1['abs'].fillna('N')
b1 = b1.drop(columns=['nthsa_id', 'description', 'topic'])
b1['mileage'] = b1['mileage'] / (b1['mileage'].max() - b1['mileage'].min())
b25 = ['Year', 'make', 'b32', 'abs', 'crashed']
for b36 in b25:
    b26 = b1[b36][b1[b36].notnull()].unique()
    for col_name in b26:
        b1[b36 + '_' + str(col_name)] = b1[b36].apply(lambda b27: 1 if b27 = = col_name else 0)
b1 = b1.drop(columns=b25)
b28 = b1.drop(columns=['crashed_Y', 'crashed_N'])
b29 = b1['crashed_Y'].tolist()
X_train, X_test, Y_train, b30 = train_test_split(b28, b29, test_size=0.3)
b31 = LogisticRegression()
b32 = b31.fit(X_train, Y_train)
b33 = b31.predict(X_test)
logreg.display_binary_metrics(b31, X_test, b30)
b34 = pd.DataFrame(b31.predict_log_proba(X_test))
b35 = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, .7, .75, .8, .85, .9, .95, .99]
for b36 in b35:
    print('\n******** For b36 = {} ******'.format(b36))
    b37 = b34.applymap(lambda b27: 1 if b27 > b36 else 0)
    b38 = metrics.accuracy_score(b30, b37.iloc[:, 1])
    print('Our testing accuracy is {}'.format(b38))