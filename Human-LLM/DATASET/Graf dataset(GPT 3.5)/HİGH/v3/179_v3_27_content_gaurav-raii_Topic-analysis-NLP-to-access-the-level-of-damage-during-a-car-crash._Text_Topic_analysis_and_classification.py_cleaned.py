
import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
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
b2 = len(b1)
a1 = 0.5
a2 = 2
b3 = None
a3 = 8
a4 = 10
b4 = None
b5 = True
b6 = TextAnalytics()
b7 = CountVectorizer(a1=a1, a2=a2, b3=b3, analyzer=b6.my_analyzer)
b8 = b7.fit_transform(b1['description'])
b9 = b7.get_feature_names()
b10 = TfidfTransformer(b4=b4, b5=b5)
b11 = b10.fit_transform(b8)
b12 = LatentDirichletAllocation(n_components=a3, a4=a4, random_state=12345)
b13 = b12.fit_transform(b11)
print("\n********** GENERATED TOPICS **********")
TextAnalytics.display_topics(b12.components_, b9, b14 = 15, mask=None)
b15 = [np.argmax(topic) for topic in b13]
b16 = ["topic"] + [f"T{i}" for i in range(1, a3 + 1)]
b17 = np.column_stack((b15, b13))
b18 = pd.DataFrame(b17, columns=b16)
b1 = pd.concat([b1, b18], axis=1)
b1['mileage'] = b1['mileage'].fillna(b1['mileage'].mean())
b1['abs'] = b1['abs'].fillna('N')
b1 = b1.drop(columns=['nthsa_id', 'description'])
b19 = ['Year', 'make', 'model', 'abs', 'crashed']
for var in b19:
    b1 = pd.get_dummies(b1, columns=[var], prefix=[var])
b20 = b1.drop(columns=['crashed_Y', 'crashed_N'])
b21 = b1['crashed_Y']
X_train, X_test, Y_train, b22 = train_test_split(b20, b21, test_size=0.3)
b23 = LogisticRegression()
b23.fit(X_train, Y_train)
logreg.display_binary_metrics(b23, X_test, b22)
b24 = b23.predict_log_proba(X_test)
b25 = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 0.99]
for b26 in b25:
    print(f'\n******** For b26 = {b26} ******')
    b27 = (b24[:, 1] > b26).astype(int)
    b28 = metrics.accuracy_score(b22, b27)
    print(f'Testing accuracy: {b28}')