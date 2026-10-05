import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score, classification_report
from sklearn.feature_extraction.text import CountVectorizer
df = pd.read_csv("/..../enter your path of dataset/...csv")
df['label_num'] = df.label.map({'ham': 0, 'spam': 1})
features = df["text"]
labels = df["label_num"]
sn.countplot(df["label"])
plt.show()
f_train, f_test, l_train, l_test = train_test_split(features, labels, test_size=0.1)
f_train = np.array(f_train)
f_test = np.array(f_test)
l_train = np.array(l_train)
l_test = np.array(l_test)
vect = CountVectorizer()
f_train_count = vect.fit_transform(f_train)
f_test_count = vect.transform(f_test)
nb_classifier = MultinomialNB()
nb_classifier.fit(f_train_count, l_train)
train_score = nb_classifier.score(f_train_count, l_train)
test_score = nb_classifier.score(f_test_count, l_test)
print("\n\n\033[1;32;40m [+]train score: ", train_score)
print("\n\n[+]test score:  ", test_score)
y_class = nb_classifier.predict(f_test_count)
accuracy = accuracy_score(l_test, y_class)
precision = precision_score(l_test, y_class)
recall = recall_score(l_test, y_class)
f1 = f1_score(l_test, y_class)
print("\n\n[+]accuracy score = ", accuracy)
print("\n\n[+]precision score = ", precision)
print("\n\n[+]recall score = ", recall)
print("\n\n[+]f1 score = ", f1)
report = classification_report(y_class, l_test)
print("\n", report)
print("\n\n[+] Let's test with other unique messages other than the datasets used:")
t = [input("[+] Enter a text message to test: ")]
t = np.array(t)
t = vect.transform(t)
prediction = nb_classifier.predict(t)
if prediction == 0:
    print("HAAM!")
else:
    print("\033[1;31;40m [+]SPAAAM!")