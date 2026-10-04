import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score,f1_score,recall_score,classification_report
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
b1 = pd.read_csv("/..../enter your path of dataset/...csv")
b1['label_num'] = b1.label.map({'ham':0,'spam':1})
b2 = b1["text"]
b3 = b1["label_num"]
sn.countplot(b1["label"])
print(plt.show())
b5,b6,b7,b4 = train_test_split(b2,b3,test_size=.1)
b5 = np.array(b5)
b6 = np.array(b6)
b7 = np.array(b7)
b4 = np.array(b4)
b8 = CountVectorizer()
b9 = b8.fit_transform(b5)
b10 = b8.transform(b6)
b11 = MultinomialNB()
b11.fit(b9,b7)
print("\n\n\033[1;32;40m [+]train b17: ",b11.b17(b9,b7))
print("\n\n[+]test b17:  ",b11.b17(b10,b4))
b12 = b11.predict(b10)
b13 = accuracy_score(b4,b12)
b14 = precision_score(b4,b12)
b15 = recall_score(b4,b12)
b16 = f1_score(b4,b12)
print("\n\n[+]accuracy b17 = " ,b13)
print("\n\n[+]precision b17 = ",b14)
print("\n\n[+]recall b17 = ", b15)
print("\n\n[+]f1 b17 = ", b16)
b18 = classification_report(b12,b4)
print("\n",b18)
print("\n\n[+] lets test with other unique msgs other than the datasets used: ")
b19 = [input("[+]enter b13 text msg to test : ")]
b19 = np.array(b19)
b19 = b8.transform(b19)
b20 = b11.predict(b19)
if b20 = = 0:
    print("HAAM!")
else:
    print("\033[1;31;40m [+]SPAAAM!")