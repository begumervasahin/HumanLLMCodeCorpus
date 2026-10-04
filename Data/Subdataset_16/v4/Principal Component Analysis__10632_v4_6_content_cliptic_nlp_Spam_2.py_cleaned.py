from __future__ import print_function, division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from b11 import WordCloud
b1 = pd.read_csv('large_files/spam.csv', encoding='ISO-8859-1')
b1 = b1.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1)
b1.b2 = ['labels', 'data']
b1['b_labels'] = b1['labels'].map({'ham': 0, 'spam': 1})
b3 = b1['data'].values
b4 = b1['b_labels'].values
b7, b8, Y_train, b5 = train_test_split(b3, b4, test_size=0.33)
b6 = CountVectorizer(decode_error='ignore')
b7 = b6.fit_transform(b7)
b8 = b6.transform(b8)
b9 = MultinomialNB()
b9.fit(b7, Y_train)
print("Train score:", b9.score(b7, Y_train))
print("Test score:", b9.score(b8, b5))
def fonk1(label):
    b10 = ' '.join(b1[b1['labels'] == label]['data'].str.lower())
    b11 = WordCloud(width=600, height=400).generate(b10)
    plt.imshow(b11, b12 = 'bilinear')
    plt.axis('off')
    plt.title(f"Word Cloud for {label} messages")
    plt.show()
fonk1('spam')
fonk1('ham')
b13 = b6.transform(b3)
b1['predictions'] = b9.predict(b13)
b14 = b1[(b1['predictions'] == 0) & (b1['b_labels'] == 1)]['data']
print("THESE ARE THE SNEAKY SPAM MESSAGES:\n")
for msg in b14:
    print(msg)
b15 = b1[(b1['predictions'] == 1) & (b1['b_labels'] == 0)]['data']
print("THESE ARE THE NOT SPAM BUT CLASSIFIED AS THEY WERE:\n")
for msg in b15:
    print(msg)