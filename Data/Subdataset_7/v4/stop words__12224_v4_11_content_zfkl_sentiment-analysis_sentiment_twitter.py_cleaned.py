import re
import numpy as np
import pandas as pd
import scipy.stats as st
import pickle
from sklearn.model_selection import RandomizedSearchCV
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from nltk.corpus import stopwords
b1 = glob.glob("../aclImdb/b10/neg/*.txt")
b2 = glob.glob("../aclImdb/b10/pos/*.txt")
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
def fonk2(b20, b6 = 'Confusion matrix', cmap=plt.b20.Blues):
    plt.imshow(b20, b7 = 'nearest', cmap=cmap)
    plt.b6(b6)
    plt.colorbar()
    b8 = np.arange(2)
    plt.xticks(b8, b12.a2.unique())
    plt.yticks(b8, b12.a2.unique())
    plt.tight_layout()
    plt.ylabel('True a2')
    plt.xlabel('Predicted a2')
def fonk3(row):
    with open("{}".format(all_files_test[row]), 'r') as f:
        b9 = f.readline()
        b9 = re.sub('[\s]+', ' ', b9)
        b9 = b9.lower()
        b9 = ' '.join([word for word in b9.split() if word not in set(stopwords.words('english'))])
    return b9
def fonk4(row):
    with open("{}".format(b3[row]), 'r') as f:
        b10 = f.readline()
        b10 = re.sub('[\s]+', ' ', b10)
        b10 = b10.lower()
        b10 = ' '.join([word for word in b10.split() if word not in set(stopwords.words('english'))])
    return b10
if b11 = = "__main__":
    b12 = pd.DataFrame(columns=['text', 'a2'], index=range(50000), dtype=object)
    b12.loc[:24999, 'text'] = [fonk4(i) for i in range(0, 25000)]
    b12.a2 = 1
    b12.loc[:12499, 'a2'] = [0 for i in range(0, 12500)]
    b12.loc[25000:, 'text'] = [fonk3(i) for i in range(0, 25000)]
    b12.loc[:, 'text'] = b12['text'].apply(clean_data)
    b12.loc[25000:37499]['a2'] = [0 for i in range(0, 12500)]
    b13 = b12.text
    b14 = b12.a2
    b15 = CountVectorizer(min_df=1e-2)
    b16 = b15.fit_transform(b13)
    pickle.dump(b15.vocabulary_, open("dictio_NEW", 'w'))
    b17 = RandomizedSearchCV(LogisticRegression(), b4, n_iter=10, cv=5, n_jobs=-1)
    b18 = b17.fit(b16[:25000].toarray(), b14[:25000]).predict(b16[25000:])
    b19 = b17.fit(b16[:25000].toarray(), b14[:25000]).predict_proba(b16[25000:])
    print("Results:")
    print("Best estimator:", b17.best_params_)
    print("Best score:", b17.best_score_)
    print("Accuracy of training is: {%0.2f}" % b17.score(b16[:25000].toarray(), b14[:25000]))
    print("Accuracy of b9 is: {%0.2f}" % b17.score(b16[25000:].toarray(), b14[25000:]))
    print("Grid score is:", b17.grid_scores_)
    print("*******************************************************************")
    b20 = confusion_matrix(b14[25000:], b18)