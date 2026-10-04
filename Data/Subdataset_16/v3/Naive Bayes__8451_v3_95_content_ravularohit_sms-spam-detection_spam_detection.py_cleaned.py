import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score, classification_report
from sklearn.feature_extraction.text import CountVectorizer
def fonk1(filepath):
    b1 = pd.read_csv(filepath)
    b1['label_num'] = b1['label'].map({'ham': 0, 'spam': 1})
    b2 = b1["text"]
    b3 = b1["label_num"]
    sns.countplot(b4 = "label", data=b1)
    plt.show()
    f_train, f_test, l_train, b5 = train_test_split(b2, b3, test_size=0.1, random_state=42)
    return f_train, f_test, l_train, b5
def fonk2(f_train, f_test):
    b6 = CountVectorizer()
    b7 = b6.fit_transform(f_train)
    b8 = b6.transform(f_test)
    return b7, b8, b6
def fonk3(b7, l_train, b8, b5):
    b9 = MultinomialNB()
    b9.fit(b7, l_train)
    print("\n[+] Train b15: ", b9.b15(b7, l_train))
    print("\n[+] Test b15: ", b9.b15(b8, b5))
    b10 = b9.predict(b8)
    b11 = accuracy_score(b5, b10)
    b12 = precision_score(b5, b10)
    b13 = recall_score(b5, b10)
    b14 = f1_score(b5, b10)
    print("\n[+] Accuracy b15 = ", b11)
    print("\n[+] Precision b15 = ", b12)
    print("\n[+] Recall b15 = ", b13)
    print("\n[+] F1 b15 = ", b14)
    b16 = classification_report(b5, b10)
    print("\n", b16)
    return b9
def fonk4(b9, b6):
    print("\n[+] Let's test with other unique messages other than the datasets used:")
    b17 = input("[+] Enter a text message to test: ")
    b18 = b6.transform([b17])
    b19 = b9.predict(b18)
    if b19 = = 0:
        print("HAM!")
    else:
        print("\033[1;31;40m[+] SPAM!\033[0m")
def fonk5(filepath):
    f_train, f_test, l_train, b5 = fonk1(filepath)
    b7, b8, b6 = fonk2(f_train, f_test)
    b9 = fonk3(b7, l_train, b8, b5)
    fonk4(b9, b6)
if b20 = = "__main__":
    fonk5("path/to/your/dataset.csv")