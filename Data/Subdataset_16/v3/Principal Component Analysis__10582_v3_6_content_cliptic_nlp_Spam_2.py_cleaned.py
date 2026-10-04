from __future__ import print_function, division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from b13 import WordCloud
def fonk1(b18):
    b1 = pd.read_csv(b18, encoding='ISO-8859-1')
    b1.drop(b2 = ["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], inplace=True)
    b1.b2 = ['labels', 'data']
    b1['b_labels'] = b1['labels'].map({'ham': 0, 'spam': 1})
    return b1
def fonk2(b1):
    b3 = b1["data"].values
    b4 = b1['b_labels'].values
    return train_test_split(b3, b4, b5 = 0.33, random_state=42)
def fonk3(X_train, Y_train):
    b6 = CountVectorizer(decode_error='ignore')
    b7 = b6.fit_transform(X_train)
    b8 = MultinomialNB()
    b8.fit(b7, Y_train)
    return b8, b6
def fonk4(b8, b6, X_train, X_test, Y_train, b19):
    b7 = b6.transform(X_train)
    b9 = b6.transform(X_test)
    b10 = b8.score(b7, Y_train)
    b11 = b8.score(b9, b19)
    print("Train score:", b10)
    print("Test score:", b11)
def fonk5(b1, label):
    b12 = ' '.join(b1[b1['labels'] == label]['data'].str.lower())
    b13 = WordCloud(width=600, height=400).generate(b12)
    plt.imshow(b13, b14 = 'bilinear')
    plt.axis('off')
    plt.title(f"Word Cloud for {label}")
    plt.show()
def fonk6(b1, b8, b6):
    b15 = b6.transform(b1["data"].values)
    b1['predictions'] = b8.predict(b15)
    b16 = b1[(b1['predictions'] == 0) & (b1['b_labels'] == 1)]['data']
    b17 = b1[(b1['predictions'] == 1) & (b1['b_labels'] == 0)]['data']
    print("THESE ARE THE SNEAKY SPAM MESSAGES:\n")
    for msg in b16:
        print(msg)
    print("\nTHESE ARE THE NOT SPAM BUT CLASSIFIED AS THEY WERE:\n")
    for msg in b17:
        print(msg)
def fonk7():
    b18 = 'large_files/spam.csv'
    b1 = fonk1(b18)
    print(b1.head())
    X_train, X_test, Y_train, b19 = fonk2(b1)
    b8, b6 = fonk3(X_train, Y_train)
    fonk4(b8, b6, X_train, X_test, Y_train, b19)
    fonk5(b1, 'spam')
    fonk5(b1, 'ham')
    fonk6(b1, b8, b6)
if b20 = = "__main__":
    fonk7()