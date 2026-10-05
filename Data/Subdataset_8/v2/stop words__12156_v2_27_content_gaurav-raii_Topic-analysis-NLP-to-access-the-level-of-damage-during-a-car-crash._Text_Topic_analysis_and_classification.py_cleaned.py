
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
data_frame = pd.read_excel("C:/Users/gaura/Desktop/stat 656/week 11/week 11 assignment/GMC_Complaints.xlsx")
num_reviews = len(data_frame['description'])
stop_words = 'english'
reviews = data_frame['description']
max_features = None
num_topics = 8
max_iterations = 10
max_document_frequency = 0.5
learning_offset = 10.
learning_method = 'online'
term_frequency_matrix = 'tfidf'
text_analytics = TextAnalytics()
count_vectorizer = CountVectorizer(max_df=max_document_frequency, min_df=2, max_features=max_features, analyzer=text_analytics.my_analyzer)
term_frequency_matrix = count_vectorizer.fit_transform(reviews)
terms = count_vectorizer.get_feature_names()
tfidf_transformer = TfidfTransformer(norm=None, use_idf=True)
term_frequency_matrix = tfidf_transformer.fit_transform(term_frequency_matrix)
lda_model = LatentDirichletAllocation(n_components=num_topics, max_iter=max_iterations,
                                      learning_method=learning_method,
                                      learning_offset=learning_offset,
                                      random_state=12345)
topic_distribution = lda_model.fit_transform(term_frequency_matrix)
print("\n********** GENERATED TOPICS **********")
TextAnalytics.display_topics(lda_model.components_, terms, n_terms=15, mask=None)
review_topics = [0] * num_reviews
for i in range(num_reviews):
    max_val = abs(topic_distribution[i][0])
    review_topics[i] = 0
    for j in range(num_topics):
        val = abs(topic_distribution[i][j])
        if val > max_val:
            max_val = val
            review_topics[i] = j
review_scores = []
for i in range(num_reviews):
    topic_score = [0] * (num_topics + 1)
    topic_score[0] = review_topics[i]
    for j in range(num_topics):
        topic_score[j + 1] = topic_distribution[i][j]
    review_scores.append(topic_score)
columns = ["topic"]
for i in range(num_topics):
    column_name = "T" + str(i + 1)
    columns.append(column_name)
topic_df = pd.DataFrame.from_records(review_scores, columns=columns)
data_frame = data_frame.join(topic_df)
data_frame['mileage'] = data_frame['mileage'].fillna(data_frame['mileage'].mean())
data_frame['abs'] = data_frame['abs'].fillna('N')
data_frame = data_frame.drop(columns=['nthsa_id', 'description', 'topic'])
data_frame['mileage'] = data_frame['mileage'] / (data_frame['mileage'].max() - data_frame['mileage'].min())
categorical_variables = ['Year', 'make', 'model', 'abs', 'crashed']
for variable in categorical_variables:
    unique_values = data_frame[variable][data_frame[variable].notnull()].unique()
    for value in unique_values:
        data_frame[variable + '_' + str(value)] = data_frame[variable].apply(lambda x: 1 if x == value else 0)
data_frame = data_frame.drop(columns=categorical_variables)
X = data_frame.drop(columns=['crashed_Y', 'crashed_N'])
Y = data_frame['crashed_Y'].tolist()
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)
logistic_regression_model = LogisticRegression()
model = logistic_regression_model.fit(X_train, Y_train)
predictions_test = logistic_regression_model.predict(X_test)
logreg.display_binary_metrics(logistic_regression_model, X_test, Y_test)
predicted_probabilities_df = pd.DataFrame(logistic_regression_model.predict_log_proba(X_test))
threshold_list = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, .7, .75, .8, .85, .9, .95, .99]
for threshold in threshold_list:
    print('\n******** For threshold = {} ******'.format(threshold))
    Y_test_predictions = predicted_probabilities_df.applymap(lambda x: 1 if x > threshold else 0)
    test_accuracy = metrics.accuracy_score(Y_test, Y_test_predictions.iloc[:, 1])
    print('Testing accuracy: {}'.format(test_accuracy))