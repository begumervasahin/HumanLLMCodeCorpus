import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score, classification_report
from sklearn.feature_extraction.text import CountVectorizer
df = pd.read_csv("path/to/your/dataset.csv")
df['label_num'] = df['label'].map({'ham': 0, 'spam': 1})
features = df["text"]
labels = df["label_num"]
sns.countplot(x="label", data=df)
plt.show()
f_train, f_test, l_train, l_test = train_test_split(features, labels, test_size=0.1, random_state=42)
f_train = np.array(f_train)
f_test = np.array(f_test)
l_train = np.array(l_train)
l_test = np.array(l_test)
vect = CountVectorizer()
f_train_count = vect.fit_transform(f_train)
f_test_count = vect.transform(f_test)
model = MultinomialNB()
model.fit(f_train_count, l_train)
print("\n[+] Train score: ", model.score(f_train_count, l_train))
print("\n[+] Test score: ", model.score(f_test_count, l_test))
y_pred = model.predict(f_test_count)
accuracy = accuracy_score(l_test, y_pred)
precision = precision_score(l_test, y_pred)
recall = recall_score(l_test, y_pred)
f1 = f1_score(l_test, y_pred)
print("\n[+] Accuracy score = ", accuracy)
print("\n[+] Precision score = ", precision)
print("\n[+] Recall score = ", recall)
print("\n[+] F1 score = ", f1)
report = classification_report(l_test, y_pred)
print("\n", report)
print("\n[+] Let's test with other unique messages other than the datasets used:")
test_message = input("[+] Enter a text message to test: ")
test_message_vectorized = vect.transform([test_message])
prediction = model.predict(test_message_vectorized)
if prediction == 0:
    print("HAM!")
else:
    print("\033[1;31;40m[+] SPAM!")