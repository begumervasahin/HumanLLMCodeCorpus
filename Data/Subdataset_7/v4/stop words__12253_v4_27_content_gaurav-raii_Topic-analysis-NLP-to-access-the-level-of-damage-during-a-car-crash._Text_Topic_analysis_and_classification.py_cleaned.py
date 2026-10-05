
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
b4 = CountVectorizer(max_df=0.5, min_df=2, analyzer='word', stop_words=b3)
b5 = b4.fit_transform(b1['description'])
b6 = TfidfTransformer(norm=None, use_idf=True)
b5 = b6.fit_transform(b5)
a1 = 8
b7 = LatentDirichletAllocation(n_components=a1, max_iter=10, learning_method='online', learning_offset=10.0, random_state=12345)
b8 = b7.fit_transform(b5)
TextAnalytics.display_topics(b7.components_, b4.get_feature_names(), b9 = 15, mask=None)
b10 = b1.drop(columns=['crashed_Y', 'crashed_N'])
b11 = b1['crashed_Y'].tolist()
X_train, X_test, Y_train, b12 = train_test_split(b10, b11, test_size=0.3)
b13 = LogisticRegression()
b14 = b13.fit(X_train, Y_train)
b15 = b13.predict(X_train)
b16 = b13.predict(X_test)
logreg.display_binary_metrics(b13, X_test, b12)
b17 = pd.DataFrame(b13.predict_log_proba(X_test))
b18 = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 0.99]
for i in b18:
    b19 = b17.applymap(lambda x: 1 if x > i else 0)
    b20 = metrics.accuracy_score(b12, b19.iloc[:, 1])
    print('For threshold {}: Testing accuracy is {}'.format(i, b20))