from __future__ import print_function, division
from builtins import range
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from b4 import WordCloud
def fonk1(file_path):
    b1 = pd.read_csv(file_path, encoding='ISO-8859-1')
    b1 = b1.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1)
    b1.b2 = ['labels', 'data']
    b1['b_labels'] = b1['labels'].map({'ham': 0, 'spam': 1})
    return b1
def fonk2(b1, b14):
    b3 = ' '.join(b1[b1['labels'] == b14]['data'].str.lower())
    b4 = WordCloud(width=600, height=400).generate(b3)
    plt.imshow(b4, b5 = 'bilinear')
    plt.axis('off')
    plt.title(f"Word Cloud for {b14} messages")
    plt.show()
def fonk3(b1, b14, correct_label):
    b6 = b1[(b1['predictions'] == b14) & (b1['b_labels'] == correct_label)]['data']
    for msg in b6:
        print(msg)
def fonk4():
    b1 = fonk1('large_files/spam.csv')
    b7 = b1['b_labels'].values
    df_train, df_test, Ytrain, b8 = train_test_split(b1['data'], b7, test_size=0.33, random_state=42)
    b9 = TfidfVectorizer(decode_error='ignore')
    b10 = b9.fit_transform(df_train)
    b11 = b9.transform(df_test)
    b12 = MultinomialNB()
    b12.fit(b10, Ytrain)
    print("Train score:", b12.score(b10, Ytrain))
    print("Test score:", b12.score(b11, b8))
    fonk2(b1, 'spam')
    fonk2(b1, 'ham')
    b13 = b9.transform(b1['data'])
    b1['predictions'] = b12.predict(b13)
    print("\nSneaky Spam Messages:")
    fonk3(b1, b14 = 0, correct_label=1)
    print("\nNot Actually Spam Messages:")
    fonk3(b1, b14 = 1, correct_label=0)
if b15 = = "__main__":
    fonk4()