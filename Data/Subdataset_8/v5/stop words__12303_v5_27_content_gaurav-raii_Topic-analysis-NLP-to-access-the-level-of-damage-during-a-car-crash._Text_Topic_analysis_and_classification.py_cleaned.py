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
df = pd.read_excel("C:/Users/gaura/Desktop/stat 656/week 11/week 11 assignment/GMC_Complaints.xlsx")
cv = CountVectorizer(max_df=0.5, min_df=2, analyzer='word', stop_words='english')
tf = cv.fit_transform(df['description'])
tfidf_vect = TfidfTransformer(norm=None, use_idf=True)
tf = tfidf_vect.fit_transform(tf)
n_topics = 8
lda = LatentDirichletAllocation(n_components=n_topics, max_iter=10, learning_method='online', learning_offset=10.0, random_state=12345)
topic_matrix = lda.fit_transform(tf)
terms = cv.get_feature_names()
TextAnalytics.display_topics(lda.components_, terms, n_terms=15, mask=None)
X = df.drop(columns=['crashed_Y', 'crashed_N'])
Y = df['crashed_Y'].tolist()
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)
model = LogisticRegression()
model.fit(X_train, Y_train)
predictions_train = model.predict(X_train)
predictions_test = model.predict(X_test)
logreg.display_binary_metrics(model, X_test, Y_test)
pred_proba_df = pd.DataFrame(model.predict_log_proba(X_test))
threshold_list = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 0.99]
for threshold in threshold_list:
    Y_test_pred = pred_proba_df.applymap(lambda x: 1 if x > threshold else 0)
    test_accuracy = metrics.accuracy_score(Y_test, Y_test_pred.iloc[:, 1])
    print(f'For threshold {threshold}: Testing accuracy is {test_accuracy}')