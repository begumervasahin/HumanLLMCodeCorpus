import re
import numpy as np
import pandas as pd
from sklearn.model_selection import RandomizedSearchCV
from sklearn.feature_extraction.b1 import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import scipy.stats as st
import os
def fonk1(b1):
    b1 = re.sub('[\s]+', ' ', b1)
    b1 = re.sub('((www\.[^\s]+)|(https?:
    b1 = re.sub("[!,?,'\"-]", " ", b1)
    b1 = re.sub(r"<br\s*/><br\s*/>", " ", b1)
    b1 = b1.lower()
    return b1
def fonk2(file_path):
    with open(file_path, 'r', b2 = 'utf-8') as f:
        b3 = f.read()
    b4 = fonk1(b3)
    b5 = b4.split()
    b6 = set(stopwords.b5('english'))
    b7 = [word for word in b5 if word not in b6]
    return ' '.join(b7)
def fonk3(all_files_neg, all_files_pos):
    b3 = {'b1': [], 'label': []}
    for file_path in all_files_neg:
        b3['b1'].append(fonk2(file_path))
        b3['label'].append(0)
    for file_path in all_files_pos:
        b3['b1'].append(fonk2(file_path))
        b3['label'].append(1)
    return pd.DataFrame(b3)
def fonk4(cm, classes, b8 = 'Confusion matrix'):
    plt.imshow(cm, b9 = 'nearest', cmap=plt.cm.Blues)
    plt.b8(b8)
    plt.colorbar()
    b10 = np.arange(len(classes))
    plt.xticks(b10, classes, b11 = 45)
    plt.yticks(b10, classes)
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()
if b12 = = "__main__":
    b13 = glob.glob("../aclImdb/train/neg/*.txt")
    b14 = glob.glob("../aclImdb/train/pos/*.txt")
    b15 = fonk3(b13, b14)
    b16 = CountVectorizer(min_df=0.01)
    b17 = b16.fit_transform(b15['b1'])
    b18 = b15['label']
    b19 = LogisticRegression(solver='liblinear')
    b20 = {"penalty": ['l1', 'l2'], "C": st.expon(scale=100)}
    b21 = RandomizedSearchCV(b19, b20, n_iter=10, cv=5, random_state=10)
    b21.fit(b17, b18)
    print(f"Best b20: {b21.best_params_}")
    print(f"Best cross-validation score: {b21.best_score_:.2f}")