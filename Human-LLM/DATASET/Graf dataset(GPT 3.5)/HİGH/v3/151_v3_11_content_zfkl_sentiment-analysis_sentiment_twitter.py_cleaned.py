import re
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import RandomizedSearchCV
from sklearn.feature_extraction.b1 import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from nltk.corpus import stopwords
import scipy.stats as st
def fonk1(b1):
    b1 = re.sub(r'\s+', ' ', b1)
    b1 = re.sub(r'www\.\S+|https?:
    b1 = re.sub(r'[!?,\'"-]', ' ', b1)
    b1 = re.sub(r'<br\s*/><br\s*/>', ' ', b1)
    b1 = b1.lower()
    return b1
def fonk2(file_path):
    with open(file_path, 'r', b2 = 'utf-8') as file:
        b3 = file.read()
    b4 = fonk1(b3)
    b5 = b4.split()
    b6 = [word for word in b5 if word not in set(stopwords.b5('english'))]
    return ' '.join(b6)
def fonk3(neg_files, pos_files):
    b7 = []
    b8 = []
    for file_path in neg_files:
        b7.append(fonk2(file_path))
        b8.append(0)
    for file_path in pos_files:
        b7.append(fonk2(file_path))
        b8.append(1)
    return pd.DataFrame({'b1': b7, 'label': b8})
def fonk4(cm, class_names):
    plt.imshow(cm, b9 = 'nearest', cmap=plt.cm.Blues)
    plt.title('Confusion Matrix')
    plt.colorbar()
    b10 = np.arange(len(class_names))
    plt.xticks(b10, class_names, b11 = 45)
    plt.yticks(b10, class_names)
    plt.tight_layout()
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.show()
if b12 = = "__main__":
    b13 = glob.glob("../aclImdb/train/neg/*.txt")
    b14 = glob.glob("../aclImdb/train/pos/*.txt")
    b15 = fonk3(b13, b14)
    b16 = CountVectorizer(min_df=0.01)
    b17 = b16.fit_transform(b15['b1'])
    b18 = b15['label']
    b19 = {
        "penalty": ['l1', 'l2'],
        "C": st.expon(b20 = 100)
    }
    b21 = RandomizedSearchCV(LogisticRegression(solver='liblinear'), b19, n_iter=10, cv=5, random_state=10)
    b21.fit(b17, b18)
    print(f"Best parameters: {b21.best_params_}")
    print(f"Best cross-validation score: {b21.best_score_:.2f}")