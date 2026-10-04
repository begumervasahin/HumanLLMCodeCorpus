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
f_train, f_test, l_train, b4 = train_test_split(b2, b3, test_size=0.1, random_state=42)
b5 = CountVectorizer()
b6 = b5.fit_transform(f_train)
b7 = b5.transform(f_test)
b8 = MultinomialNB()
b8.fit(b6, l_train)
print("\n[+] Training score:", b8.score(b6, l_train))
print("[+] Testing score:", b8.score(b7, b4))
b9 = b8.predict(b7)
b10 = accuracy_score(b4, b9)
b11 = precision_score(b4, b9)
b12 = recall_score(b4, b9)
b13 = f1_score(b4, b9)
print("\n[+] Accuracy score:", b10)
print("[+] Precision score:", b11)
print("[+] Recall score:", b12)
print("[+] F1 score:", b13)
b14 = classification_report(b4, b9)
print("\nClassification Report:\n", b14)
def fonk1(message):
    b15 = b5.transform([message])
    b16 = b8.predict(b15)
    if b16 = = 0:
        print("HAM!")
    else:
        print("\033[1;31;40m[+] SPAM!")
print("\n\n[+] Let's test with other unique messages not in the dataset:")
b17 = input("[+] Enter a text message to test: ")
fonk1(b17)