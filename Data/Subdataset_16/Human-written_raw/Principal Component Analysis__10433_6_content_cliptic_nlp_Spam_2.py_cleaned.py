from __future__ import print_function, division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from b13 import WordCloud
b1 = pd.read_csv('large_files/spam.csv', encoding = 'ISO-8859-1')
b1 = b1.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1)
b1.b2 = ['labels', 'data']
b1['b_labels'] = b1['labels'].map({'ham': 0, 'spam': 1})
b3 = b1['b_labels'].values
b4 = b1["data"].values
print(b1)
b7, b8, Y_train, b5 = train_test_split(b4, b3, test_size = 0.33)
'''
b6 = TfidfVectorizer(decode_error = 'ignore')
b7 = b6.fit_transform(b7)
b8 = b6.transform(b8)
'''
b9 = CountVectorizer(decode_error = 'ignore')
b7 = b9.fit_transform(b7)
b8 = b9.transform(b8)
b10 = MultinomialNB()
b10.fit(b7, Y_train)
print("Train score:", b10.score(b7, Y_train))
print("Test score:", b10.score(b8, b5))
def fonk1(label):
	b11 = ''
	for b12 in b1[b1['labels'] == label]['data']:
		b12 = b12.lower()
		b11 += b12 + ' '
	b13 = WordCloud(width = 600, height = 400).generate(b11)
	plt.imshow(b13)
	plt.axis('off')
	plt.show()
fonk1('spam')
fonk1('ham')
b4 = b9.transform(b4)
b1['predictions'] = b10.predict(b4)
b14 = b1[(b1['predictions'] == 0) & (b1['b_labels'] == 1)]['data']
print("THESE ARE THE SNEAKY SPAM MESSAGES:\n")
for b12 in b14:
	print(b12)
b15 = b1[(b1['predictions'] == 1) & (b1['b_labels'] == 0)]['data']
print("THESE ARE THE NOT SPAM BUT CLASSIFIED AS THEY WERE:\n")
for b12 in b15:
	print(b12)