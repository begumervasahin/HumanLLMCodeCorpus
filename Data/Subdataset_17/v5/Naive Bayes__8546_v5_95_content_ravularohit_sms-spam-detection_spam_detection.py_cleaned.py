import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn.feature_extraction.text import CountVectorizer
df = pd.read_csv("/path/to/your/dataset.csv")
df['label_num'] = df.label.map({'ham': 0, 'spam': 1})
features = df["text"]
labels = df["label_num"]
sns.countplot(df["label"])
plt.show()
f_train, f_test, l_train, l_test = train_test_split(features, labels, test_size=0.1, random_state=42)
vectorizer = CountVectorizer()
f_train_count = vectorizer.fit_transform(f_train)
f_test_count = vectorizer.transform(f_test)
model = MultinomialNB()
model.fit(f_train_count, l_train)
print("\n[+] Training score:", model.score(f_train_count, l_train))
print("[+] Testing score:", model.score(f_test_count, l_test))
y_pred = model.predict(f_test_count)
accuracy = accuracy_score(l_test, y_pred)
precision = precision_score(l_test, y_pred)
recall = recall_score(l_test, y_pred)
f1 = f1_score(l_test, y_pred)
print("\n[+] Accuracy score:", accuracy)
print("[+] Precision score:", precision)
print("[+] Recall score:", recall)
print("[+] F1 score:", f1)
report = classification_report(l_test, y_pred)
print("\nClassification Report:\n", report)
def test_custom_message(message):
    message_vectorized = vectorizer.transform([message])
    prediction = model.predict(message_vectorized)
    if prediction == 0:
        print("HAM!")
    else:
        print("\033[1;31;40m[+] SPAM!")
print("\n\n[+] Let's test with other unique messages not in the dataset:")
custom_message = input("[+] Enter a text message to test: ")
test_custom_message(custom_message)