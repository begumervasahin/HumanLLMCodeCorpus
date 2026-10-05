import re
import numpy as np
import pandas as pd
from sklearn.model_selection import RandomizedSearchCV
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import scipy.stats as st
import os
def clean_data(text):
    text = re.sub('[\s]+', ' ', text)
    text = re.sub('((www\.[^\s]+)|(https?:
    text = re.sub("[!,?,'\"-]", " ", text)
    text = re.sub(r"<br\s*/><br\s*/>", " ", text)
    text = text.lower()
    return text
def read_and_clean_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
    data_clean = clean_data(data)
    words = data_clean.split()
    stopped_words = set(stopwords.words('english'))
    words_filtered = [word for word in words if word not in stopped_words]
    return ' '.join(words_filtered)
def create_dataframe(all_files_neg, all_files_pos):
    data = {'text': [], 'label': []}
    for file_path in all_files_neg:
        data['text'].append(read_and_clean_data(file_path))
        data['label'].append(0)
    for file_path in all_files_pos:
        data['text'].append(read_and_clean_data(file_path))
        data['label'].append(1)
    return pd.DataFrame(data)
def plot_confusion_matrix(cm, classes, title='Confusion matrix'):
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()
if __name__ == "__main__":
    all_files_neg_train = glob.glob("../aclImdb/train/neg/*.txt")
    all_files_pos_train = glob.glob("../aclImdb/train/pos/*.txt")
    dataframe = create_dataframe(all_files_neg_train, all_files_pos_train)
    vectorizer = CountVectorizer(min_df=0.01)
    X = vectorizer.fit_transform(dataframe['text'])
    Y = dataframe['label']
    logistic_regression = LogisticRegression(solver='liblinear')
    parameters = {"penalty": ['l1', 'l2'], "C": st.expon(scale=100)}
    clf = RandomizedSearchCV(logistic_regression, parameters, n_iter=10, cv=5, random_state=10)
    clf.fit(X, Y)
    print(f"Best parameters: {clf.best_params_}")
    print(f"Best cross-validation score: {clf.best_score_:.2f}")