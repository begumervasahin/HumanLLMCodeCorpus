import re
import numpy as np
import pandas as pd
import scipy.stats as st
import pickle
from sklearn.model_selection import RandomizedSearchCV
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from nltk.corpus import stopwords
b1 = glob.glob("../aclImdb/b7/neg/*.txt")
b2 = glob.glob("../aclImdb/b7/pos/*.txt")
b3 = b1 + b2
b4 = {"penalty": ['l1', 'l2'], "C": st.expon()}
np.random.a1 = 10
def fonk1(b5):
    try:
        b5 = re.sub('[\s]+', ' ', b5)
        b5 = re.sub('((www\.[^\s]+)|(https:
        b5 = re.sub(r'<.*?>', '', b5)
        b5 = re.sub("[!,?,\",\']", " ", b5)
        b5 = re.sub(r"<br /><br />", " ", b5)
    except:
        pass
    return b5
def fonk2(row):
    with open("{}".format(all_files_test[row]), 'r') as f:
        b6 = f.readline()
        b6 = re.sub('[\s]+', ' ', b6)
        b6 = b6.lower()
        b6 = ' '.join([word for word in b6.split() if word not in set(stopwords.words('english'))])
    return b6
def fonk3(row):
    with open("{}".format(b3[row]), 'r') as f:
        b7 = f.readline()
        b7 = re.sub('[\s]+', ' ', b7)
        b7 = b7.lower()
        b7 = ' '.join([word for word in b7.split() if word not in set(stopwords.words('english'))])
    return b7
if b8 = = "__main__":
    b9 = pd.DataFrame(columns=['text', 'label'], index=range(50000), dtype=object)
    b9['text'][:25000] = [fonk3(i) for i in range(25000)]
    b9['label'][:12500] = 0
    b9['label'][25000:37500] = 0
    b9['text'][25000:] = [fonk2(i) for i in range(25000)]
    b9['text'] = b9['text'].apply(clean_tweet)
    b10 = b9['text']
    b11 = b9['label']
    b12 = CountVectorizer(min_df=1e-2)
    b13 = b12.fit_transform(b10)
    pickle.dump(b12.vocabulary_, open("dictio_NEW", 'wb'))
    b14 = RandomizedSearchCV(LogisticRegression(), b4, n_iter=10, cv=5, n_jobs=-1)
    b14.fit(b13[:25000], b11[:25000])
    b15 = b14.predict(b13[25000:])
    b16 = b14.predict_proba(b13[25000:])
    print("Results:")
    print("Best estimator:", b14.best_params_)
    print("Best score:", b14.best_score_)
    print("Accuracy of training is: {%0.2f}" % b14.score(b13[:25000], b11[:25000]))
    print("Accuracy of b6 is: {%0.2f}" % b14.score(b13[25000:], b11[25000:]))
    print("Grid score is:", b14.grid_scores_)
    print("*******************************************************************")
    b17 = confusion_matrix(b11[25000:], b15)