import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score, classification_report
from sklearn.feature_extraction.text import CountVectorizer
b1 = pd.read_csv("/..../enter your path of dataset/...csv")
b1['label_num'] = b1.label.map({'ham': 0, 'spam': 1})
b2 = b1["text"]
b3 = b1["label_num"]
sn.countplot(b1["label"])
plt.show()
b5, b6, b7, b4 = train_test_split(b2, b3, test_size=0.1)
b5 = np.array(b5)
b6 = np.array(b6)
b7 = np.array(b7)
b4 = np.array(b4)
b8 = CountVectorizer()
b9 = b8.fit_transform(b5)
b10 = b8.transform(b6)
b11 = MultinomialNB()
b11.fit(b9, b7)
b12 = b11.b19(b9, b7)
b13 = b11.b19(b10, b4)
print("\n\n\033[1;32;40m [+]train b19: ", b12)
print("\n\n[+]test b19:  ", b13)
b14 = b11.predict(b10)
b15 = accuracy_score(b4, b14)
b16 = precision_score(b4, b14)
b17 = recall_score(b4, b14)
b18 = f1_score(b4, b14)
print("\n\n[+]b15 b19 = ", b15)
print("\n\n[+]b16 b19 = ", b16)
print("\n\n[+]b17 b19 = ", b17)
print("\n\n[+]b18 b19 = ", b18)
b20 = classification_report(b14, b4)
print("\n", b20)
print("\n\n[+] Let's test with other unique messages other than the datasets used:")
b21 = [input("[+] Enter a text message to test: ")]
b21 = np.array(b21)
b21 = b8.transform(b21)
b22 = b11.predict(b21)
if b22 = = 0:
    print("HAAM!")
else:
    print("\033[1;31;40m [+]SPAAAM!")