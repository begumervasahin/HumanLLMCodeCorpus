import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score, classification_report
from sklearn.feature_extraction.text import CountVectorizer
b1 = pd.read_csv("/path/to/your/dataset.csv")
b1['label_num'] = b1.label.map({'ham': 0, 'spam': 1})
sn.countplot(b1["label"])
plt.show()
b2 = b1["text"]
b3 = b1["label_num"]
f_train, f_test, l_train, b4 = train_test_split(b2, b3, test_size=0.1)
b5 = CountVectorizer()
b6 = b5.fit_transform(f_train)
b7 = b5.transform(f_test)
b8 = MultinomialNB()
b8.fit(b6, l_train)
b9 = b8.score(b6, l_train)
b10 = b8.score(b7, b4)
b11 = b8.predict(b7)
b12 = accuracy_score(b4, b11)
b13 = precision_score(b4, b11)
b14 = recall_score(b4, b11)
b15 = f1_score(b4, b11)
b16 = classification_report(b11, b4)
print("\n\nTrain score:", b9)
print("\n\nTest score:", b10)
print("\n\nAccuracy score:", b12)
print("\n\nPrecision score:", b13)
print("\n\nRecall score:", b14)
print("\n\nF1 score:", b15)
print("\n\nClassification report:\n", b16)
b17 = input("[+] Enter a text message to test: ")
b18 = np.array([b17])
b18 = b5.transform(b18)
b19 = b8.predict(b18)
if b19 = = 0:
    print("HAM!")
else:
    print("SPAM!")