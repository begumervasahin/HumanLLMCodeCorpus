from __future__ import print_function, division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from wordcloud import WordCloud
df = pd.read_csv('large_files/spam.csv', encoding='ISO-8859-1')
df = df.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1)
df.columns = ['labels', 'data']
df['b_labels'] = df['labels'].map({'ham': 0, 'spam': 1})
Y = df['b_labels'].values
X = df["data"].values
print(df.head())
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33)
countV = CountVectorizer(decode_error='ignore')
X_train = countV.fit_transform(X_train)
X_test = countV.transform(X_test)
model = MultinomialNB()
model.fit(X_train, Y_train)
print("Train score:", model.score(X_train, Y_train))
print("Test score:", model.score(X_test, Y_test))
def visualize(label):
    words = ''
    for msg in df[df['labels'] == label]['data']:
        msg = msg.lower()
        words += msg + ' '
    wordcloud = WordCloud(width=600, height=400).generate(words)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
visualize('spam')
visualize('ham')
X = countV.transform(X)
df['predictions'] = model.predict(X)
sneaky_spam = df[(df['predictions'] == 0) & (df['b_labels'] == 1)]['data']
print("THESE ARE THE SNEAKY SPAM MESSAGES:\n")
for msg in sneaky_spam:
    print(msg)
not_actually_spam = df[(df['predictions'] == 1) & (df['b_labels'] == 0)]['data']
print("THESE ARE THE NOT SPAM BUT CLASSIFIED AS THEY WERE:\n")
for msg in not_actually_spam:
    print(msg)