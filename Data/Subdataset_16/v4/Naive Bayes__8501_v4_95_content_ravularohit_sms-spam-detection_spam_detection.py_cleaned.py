import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn.feature_extraction.text import CountVectorizer
b1 = pd.read_csv("/path/to/your/dataset.csv")
b1['label_num'] = b1.label.map({'ham': 0, 'spam': 1})
b2 = b1["text"]
b3 = b1["label_num"]
sns.countplot(b1["label"])
plt.show()
b5, b6, b7, b4 = train_test_split(b2, b3, test_size=0.1, random_state=42)
b5 = np.array(b5)
b6 = np.array(b6)
b7 = np.array(b7)
b4 = np.array(b4)
b8 = CountVectorizer()
b9 = b8.fit_transform(b5)
b10 = b8.transform(b6)
b11 = MultinomialNB()
b11.fit(b9, b7)
print("\n[+] Training score: ", b11.score(b9, b7))
print("[+] Testing score: ", b11.score(b10, b4))
b12 = b11.predict(b10)
b13 = accuracy_score(b4, b12)
b14 = precision_score(b4, b12)
b15 = recall_score(b4, b12)
b16 = f1_score(b4, b12)
print("\n[+] Accuracy score: ", b13)
print("[+] Precision score: ", b14)
print("[+] Recall score: ", b15)
print("[+] F1 score: ", b16)
b17 = classification_report(b4, b12)
print("\nClassification Report:\n", b17)
def fonk1(b18):
    b18 = np.array([b18])
    b19 = b8.transform(b18)
    b20 = b11.predict(b19)
    if b20 = = 0:
        print("HAM!")
    else:
        print("\033[1;31;40m [+] SPAM!")
print("\n\n[+] Let's test with other unique messages not in the dataset:")
b21 = input("[+] Enter a text b18 to test: ")
fonk1(b21)