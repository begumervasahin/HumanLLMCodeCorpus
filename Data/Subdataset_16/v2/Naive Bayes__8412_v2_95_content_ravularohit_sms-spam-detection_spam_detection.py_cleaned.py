import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score, classification_report
from sklearn.feature_extraction.text import CountVectorizer
b1 = pd.read_csv("path/to/your/dataset.csv")
b1['label_num'] = b1['label'].map({'ham': 0, 'spam': 1})
b2 = b1["text"]
b3 = b1["label_num"]
sns.countplot(b4 = "label", data=b1)
plt.show()
b6, b7, b8, b5 = train_test_split(b2, b3, test_size=0.1, random_state=42)
b6 = np.array(b6)
b7 = np.array(b7)
b8 = np.array(b8)
b5 = np.array(b5)
b9 = CountVectorizer()
b10 = b9.fit_transform(b6)
b11 = b9.transform(b7)
b12 = MultinomialNB()
b12.fit(b10, b8)
print("\n[+] Train b18: ", b12.b18(b10, b8))
print("\n[+] Test b18: ", b12.b18(b11, b5))
b13 = b12.predict(b11)
b14 = accuracy_score(b5, b13)
b15 = precision_score(b5, b13)
b16 = recall_score(b5, b13)
b17 = f1_score(b5, b13)
print("\n[+] Accuracy b18 = ", b14)
print("\n[+] Precision b18 = ", b15)
print("\n[+] Recall b18 = ", b16)
print("\n[+] F1 b18 = ", b17)
b19 = classification_report(b5, b13)
print("\n", b19)
print("\n[+] Let's test with other unique messages other than the datasets used:")
b20 = input("[+] Enter a text message to test: ")
b21 = b9.transform([b20])
b22 = b12.predict(b21)
if b22 = = 0:
    print("HAM!")
else:
    print("\033[1;31;40m[+] SPAM!")