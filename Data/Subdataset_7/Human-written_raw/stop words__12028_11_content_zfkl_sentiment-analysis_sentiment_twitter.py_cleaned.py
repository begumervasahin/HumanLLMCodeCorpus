
import re
import sys
import glob
import pickle
import numpy as np
import pandas as pd
import scipy.stats as st
from sklearn.model_selection import  RandomizedSearchCV
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from nltk.corpus import stopwords
b1 = glob.glob("../aclImdb/b11/neg/*.txt")
b2 = glob.glob("../aclImdb/b11/pos/*.txt")
b3 = b1 + b2
b4 = {"penalty": ['l1', 'l2'], "C":st.expon()}
b5 = np.random.b5 = 10
def fonk1(b6):
    try:
        b6 = re.sub('[\s]+', ' ', b6)
        b6 = re.sub('((www\.[^\s]+)|(https:
        b6 = re.sub(r'
        b6 = myre_UCS2.sub('', b6)
        b6 = re.sub("[!,?,\",\']", " ", b6)
        b6 = re.sub(r"<br /><br />", " ", b6)
    except:
        print "Unexpected error:", sys.exc_info()[0]
    return b6
def fonk2(b23, b7 = 'Confusion matrix', cmap=plt.b23.Blues):
    plt.imshow(b23, b8 = 'nearest', cmap=cmap)
    plt.b7(b7)
    plt.colorbar()
    b9 = np.arange(2)
    plt.xticks(b9, b13.a1.unique())
    plt.yticks(b9, b13.a1.unique())
    plt.tight_layout()
    plt.ylabel('True a1')
    plt.xlabel('Predicted a1')
def fonk3(row):
    with open("{}".format(all_files_test[row]), 'r') as f:
        b10 = f.readline()
        b10 = re.sub('[\s]+', ' ', b10)
        b10 = b10.lower()
        b10 = ' '.join([word for word in b10.split() if \
        word not in set(stopwords.words('english'))])
    return b10
def fonk4(row):
    with open("{}".format(b3[row]), 'r') as f:
        b11 = f.readline()
        b11 = re.sub('[\s]+', ' ', b11)
        b11 = b11.lower()
        b11 = ' '.join([word for word in b11.split() \
        if word not in set(stopwords.words('english'))])
    return b11
if b12 = = "__main__":
    b13 = pd.DataFrame(columns=['text', 'a1'], index=range(50000), dtype=object)
    b13.loc[:24999, 'text'] = [fonk4(i) for i in range(0, 25000)]
    b13.a1 = 1
    b13.loc[:12499, 'a1'] = [0 for i in range(0, 12500)]
    b13.loc[25000:, 'text'] = [fonk3(i) for i in range(0, 25000)]
    b13.loc[:, 'text'] = b13['text'].apply(clean_data)
    b13.loc[25000:37499]['a1'] = [0 for i in range(0, 12500)]
    b14 = b13.text
    b15 = b13.a1
    b16 = {"n_estimators": st.randint(10, 20), "criterion":['gini', 'entropy']}
    b5 = np.random.b5 = 10
    b17 = CountVectorizer(min_df=1e-2)
    b18 = b17.fit_transform(b14)
    pickle.dump(b17.vocabulary_, open("dictio_NEW", 'w'))
    b19 = RandomizedSearchCV(LogisticRegression(), b4, n_iter=10, cv=5, n_jobs=-1)
    b20 = b19.fit(b18[:25000].toarray(), b15[:25000]).predict(b18[25000:])
    b21 = b19.fit(b18[:25000].toarray(), b15[:25000]).predict_proba(b18[25000:])
    print "Resultats:\n b22 = {}\n best_score = {}".format(b19.best_params_, b19.best_score_)
    print "Accuracy of training is: {%0.2f}\n Accuracy of b10 is: {%0.2f}"\
    %(b19.score(b18[:25000].toarray(), b15[:25000]), b19.score(b18[25000:].toarray(), b15[25000:]))
    print "Grid_score is: {}\n  ".format(b19.grid_scores_)
    print "*******************************************************************"
    b23 = confusion_matrix(b15[25000:], b20)