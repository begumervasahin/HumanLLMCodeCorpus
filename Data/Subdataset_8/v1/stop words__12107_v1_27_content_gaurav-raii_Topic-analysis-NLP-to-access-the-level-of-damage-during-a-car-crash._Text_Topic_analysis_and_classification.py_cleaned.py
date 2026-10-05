
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
n_reviews = len(df['description'])
s_words = 'english'
reviews = df['description']
m_features = None
n_topics = 8
max_iter = 10
max_df = 0.5
learning_offset = 10.
learning_method = 'online'
tf_matrix = 'tfidf'
ta = TextAnalytics()
cv = CountVectorizer(max_df=max_df, min_df=2, max_features=m_features, analyzer=ta.my_analyzer)
tf = cv.fit_transform(reviews)
terms = cv.get_feature_names()
tfidf_vect = TfidfTransformer(norm=None, use_idf=True)
tf = tfidf_vect.fit_transform(tf)
uv = LatentDirichletAllocation(n_components=n_topics, max_iter=max_iter,
                               learning_method=learning_method,
                               learning_offset=learning_offset,
                               random_state=12345)
U = uv.fit_transform(tf)
print("\n********** GENERATED TOPICS **********")
TextAnalytics.display_topics(uv.components_, terms, n_terms=15, mask=None)
topics = [0] * n_reviews
for i in range(n_reviews):
    max_val = abs(U[i][0])
    topics[i] = 0
    for j in range(n_topics):
        val = abs(U[i][j])
        if val > max_val:
            max_val = val
            topics[i] = j
rev_scores = []
for i in range(n_reviews):
    u = [0] * (n_topics + 1)
    u[0] = topics[i]
    for j in range(n_topics):
        u[j + 1] = U[i][j]
    rev_scores.append(u)
cols = ["topic"]
for i in range(n_topics):
    s = "T" + str(i + 1)
    cols.append(s)
df_rev = pd.DataFrame.from_records(rev_scores, columns=cols)
df = df.join(df_rev)
df['mileage'] = df['mileage'].fillna(df['mileage'].mean())
df['abs'] = df['abs'].fillna('N')
df = df.drop(columns=['nthsa_id', 'description', 'topic'])
df['mileage'] = df['mileage'] / (df['mileage'].max() - df['mileage'].min())
categorical = ['Year', 'make', 'model', 'abs', 'crashed']
for i in categorical:
    a = df[i][df[i].notnull()].unique()
    for col_name in a:
        df[i + '_' + str(col_name)] = df[i].apply(lambda x: 1 if x == col_name else 0)
df = df.drop(columns=categorical)
X = df.drop(columns=['crashed_Y', 'crashed_N'])
Y = df['crashed_Y'].tolist()
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)
lm = LogisticRegression()
model = lm.fit(X_train, Y_train)
predictions_test = lm.predict(X_test)
logreg.display_binary_metrics(lm, X_test, Y_test)
pred_proba_df = pd.DataFrame(lm.predict_log_proba(X_test))
threshold_list = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, .7, .75, .8, .85, .9, .95, .99]
for i in threshold_list:
    print('\n******** For i = {} ******'.format(i))
    Y_test_pred = pred_proba_df.applymap(lambda x: 1 if x > i else 0)
    test_accuracy = metrics.accuracy_score(Y_test, Y_test_pred.iloc[:, 1])
    print('Our testing accuracy is {}'.format(test_accuracy))