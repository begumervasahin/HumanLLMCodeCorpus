from __future__ import print_function, division
from builtins import range
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from b10 import WordCloud
b1 = pd.read_csv('large_files/spam.csv', encoding='ISO-8859-1')
b1 = b1.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1)
b1.b2 = ['labels', 'data']
b1['b_labels'] = b1['labels'].map({'ham': 0, 'spam': 1})
b3 = b1['b_labels'].values
df_train, df_test, Ytrain, b4 = train_test_split(b1['data'], b3, test_size=0.33, random_state=42)
b5 = TfidfVectorizer(decode_error='ignore')
b6 = b5.fit_transform(df_train)
b7 = b5.transform(df_test)
b8 = MultinomialNB()
b8.fit(b6, Ytrain)
print("Train score:", b8.score(b6, Ytrain))
print("Test score:", b8.score(b7, b4))
def fonk1(label):
    b9 = ' '.join(b1[b1['labels'] == label]['data'].str.lower())
    b10 = WordCloud(width=600, height=400).generate(b9)
    plt.imshow(b10, b11 = 'bilinear')
    plt.axis('off')
    plt.title(f'Word Cloud for {label}')
    plt.show()
fonk1('spam')
fonk1('ham')
b12 = b5.transform(b1['data'])
b1['predictions'] = b8.predict(b12)
b13 = b1[(b1['predictions'] == 0) & (b1['b_labels'] == 1)]['data']
print("\nSneaky Spam Messages (False Negatives):")
for msg in b13:
    print(msg)
b14 = b1[(b1['predictions'] == 1) & (b1['b_labels'] == 0)]['data']
print("\nNot Actually Spam Messages (False Positives):")
for msg in b14:
    print(msg)