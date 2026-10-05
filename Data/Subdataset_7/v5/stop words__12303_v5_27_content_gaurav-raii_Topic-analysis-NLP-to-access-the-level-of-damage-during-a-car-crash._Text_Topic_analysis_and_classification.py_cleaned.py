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
b2 = CountVectorizer(max_df=0.5, min_df=2, analyzer='word', stop_words='english')
b3 = b2.fit_transform(b1['description'])
b4 = TfidfTransformer(norm=None, use_idf=True)
b3 = b4.fit_transform(b3)
a1 = 8
b5 = LatentDirichletAllocation(n_components=a1, max_iter=10, learning_method='online', learning_offset=10.0, random_state=12345)
b6 = b5.fit_transform(b3)
b7 = b2.get_feature_names()
TextAnalytics.display_topics(b5.components_, b7, b8 = 15, mask=None)
b9 = b1.drop(columns=['crashed_Y', 'crashed_N'])
b10 = b1['crashed_Y'].tolist()
X_train, X_test, Y_train, b11 = train_test_split(b9, b10, test_size=0.3)
b12 = LogisticRegression()
b12.fit(X_train, Y_train)
b13 = b12.predict(X_train)
b14 = b12.predict(X_test)
logreg.display_binary_metrics(b12, X_test, b11)
b15 = pd.DataFrame(b12.predict_log_proba(X_test))
b16 = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 0.99]
for threshold in b16:
    b17 = b15.applymap(lambda x: 1 if x > threshold else 0)
    b18 = metrics.accuracy_score(b11, b17.iloc[:, 1])
    print(f'For threshold {threshold}: Testing accuracy is {b18}')