import re
import numpy as np
import pandas as pd
import scipy.stats as st
import pickle
from sklearn.model_selection import RandomizedSearchCV
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from nltk.corpus import stopwords
ALL_FILES_NEG_TRAIN = glob.glob("../aclImdb/train/neg/*.txt")
ALL_FILES_POS_TRAIN = glob.glob("../aclImdb/train/pos/*.txt")
ALL_FILES_TRAIN = ALL_FILES_NEG_TRAIN + ALL_FILES_POS_TRAIN
params_logit = {"penalty": ['l1', 'l2'], "C": st.expon()}
np.random.seed = 10
def clean_tweet(tweet):
    try:
        tweet = re.sub('[\s]+', ' ', tweet)
        tweet = re.sub('((www\.[^\s]+)|(https:
        tweet = re.sub(r'<.*?>', '', tweet)
        tweet = re.sub("[!,?,\",\']", " ", tweet)
        tweet = re.sub(r"<br /><br />", " ", tweet)
    except:
        pass
    return tweet
def clean_and_preprocess_test_data(row):
    with open("{}".format(all_files_test[row]), 'r') as f:
        test = f.readline()
        test = re.sub('[\s]+', ' ', test)
        test = test.lower()
        test = ' '.join([word for word in test.split() if word not in set(stopwords.words('english'))])
    return test
def clean_and_preprocess_train_data(row):
    with open("{}".format(ALL_FILES_TRAIN[row]), 'r') as f:
        train = f.readline()
        train = re.sub('[\s]+', ' ', train)
        train = train.lower()
        train = ' '.join([word for word in train.split() if word not in set(stopwords.words('english'))])
    return train
if __name__ == "__main__":
    dataframe = pd.DataFrame(columns=['text', 'label'], index=range(50000), dtype=object)
    dataframe['text'][:25000] = [clean_and_preprocess_train_data(i) for i in range(25000)]
    dataframe['label'][:12500] = 0
    dataframe['label'][25000:37500] = 0
    dataframe['text'][25000:] = [clean_and_preprocess_test_data(i) for i in range(25000)]
    dataframe['text'] = dataframe['text'].apply(clean_tweet)
    text_data = dataframe['text']
    labels = dataframe['label']
    vectorizer = CountVectorizer(min_df=1e-2)
    X = vectorizer.fit_transform(text_data)
    pickle.dump(vectorizer.vocabulary_, open("dictio_NEW", 'wb'))
    clf = RandomizedSearchCV(LogisticRegression(), params_logit, n_iter=10, cv=5, n_jobs=-1)
    clf.fit(X[:25000], labels[:25000])
    predictions = clf.predict(X[25000:])
    probabilities = clf.predict_proba(X[25000:])
    print("Results:")
    print("Best estimator:", clf.best_params_)
    print("Best score:", clf.best_score_)
    print("Accuracy of training is: {%0.2f}" % clf.score(X[:25000], labels[:25000]))
    print("Accuracy of test is: {%0.2f}" % clf.score(X[25000:], labels[25000:]))
    print("Grid score is:", clf.grid_scores_)
    print("*******************************************************************")
    cm = confusion_matrix(labels[25000:], predictions)