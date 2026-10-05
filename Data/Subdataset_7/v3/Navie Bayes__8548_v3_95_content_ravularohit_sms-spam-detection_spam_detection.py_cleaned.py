import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score, classification_report
from sklearn.feature_extraction.text import CountVectorizer
b1 = pd.read_csv("/..../enter your path of dataset/...csv")
b1['label_num'] = b1.label.map({'ham': 0, 'spam': 1})
b2 = b1["text"]
b3 = b1["label_num"]
sns.countplot(b1["label"])
plt.show()
f_train, f_test, l_train, b4 = train_test_split(b2, b3, test_size=0.1, random_state=42)
b5 = CountVectorizer()
b6 = b5.fit_transform(f_train)
b7 = b5.transform(f_test)
b8 = MultinomialNB()
b8.fit(b6, l_train)
b9 = b8.b16(b6, l_train)
b10 = b8.b16(b7, b4)
print("\n\n\033[1;32;40m [+]train b16: ", b9)
print("\n\n[+]test b16:  ", b10)
b11 = b8.predict(b7)
b12 = accuracy_score(b4, b11)
b13 = precision_score(b4, b11)
b14 = recall_score(b4, b11)
b15 = f1_score(b4, b11)
print("\n\n[+]b12 b16 = ", b12)
print("\n\n[+]b13 b16 = ", b13)
print("\n\n[+]b14 b16 = ", b14)
print("\n\n[+]b15 b16 = ", b15)
b17 = classification_report(b11, b4)
print("\n", b17)
print("\n\n[+] Let's test with other unique messages other than the datasets used:")
b18 = [input("[+] Enter a text message to test: ")]
b18 = np.array(b18)
b18 = b5.transform(b18)
b19 = b8.predict(b18)
if b19 = = 0:
    print("HAAM!")
else:
    print("\033[1;31;40m [+]SPAAAM!")