from __future__ import print_function, division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from b11 import WordCloud
def fonk1(filepath):
    b1 = pd.read_csv(filepath, encoding='ISO-8859-1')
    b1 = b1.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1)
    b1.b2 = ['labels', 'data']
    b1['b_labels'] = b1['labels'].map({'ham': 0, 'spam': 1})
    return b1
def fonk2(b1):
    b3 = b1['data'].values
    b4 = b1['b_labels'].values
    return train_test_split(b3, b4, b5 = 0.33)
def fonk3(X_train, X_test):
    b6 = CountVectorizer(decode_error='ignore')
    b7 = b6.fit_transform(X_train)
    b8 = b6.transform(X_test)
    return b7, b8, b6
def fonk4(X_train, Y_train):
    b9 = MultinomialNB()
    b9.fit(X_train, Y_train)
    return b9
def fonk5(b9, X_train, Y_train, X_test, b15):
    print("Train score:", b9.score(X_train, Y_train))
    print("Test score:", b9.score(X_test, b15))
def fonk6(b1, label):
    b10 = ' '.join(b1[b1['labels'] == label]['data'].str.lower())
    b11 = WordCloud(width=600, height=400).generate(b10)
    plt.imshow(b11, b12 = 'bilinear')
    plt.axis('off')
    plt.title(f"Word Cloud for {label} messages")
    plt.show()
def fonk7(b1):
    b13 = b1[(b1['predictions'] == 0) & (b1['b_labels'] == 1)]['data']
    print("THESE ARE THE SNEAKY SPAM MESSAGES:\n")
    for msg in b13:
        print(msg)
    b14 = b1[(b1['predictions'] == 1) & (b1['b_labels'] == 0)]['data']
    print("THESE ARE THE NOT SPAM BUT CLASSIFIED AS THEY WERE:\n")
    for msg in b14:
        print(msg)
def fonk8(filepath):
    b1 = fonk1(filepath)
    X_train, X_test, Y_train, b15 = fonk2(b1)
    b7, b8, b6 = fonk3(X_train, X_test)
    b9 = fonk4(b7, Y_train)
    fonk5(b9, b7, Y_train, b8, b15)
    fonk6(b1, 'spam')
    fonk6(b1, 'ham')
    b16 = b6.transform(b1['data'].values)
    b1['predictions'] = b9.predict(b16)
    fonk7(b1)
if b17 = = "__main__":
    fonk8('large_files/spam.csv')