import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.b7 import Pipeline
from sklearn.metrics import classification_report, accuracy_score
import string
b1 = pd.read_csv('/Users/dineshmaharana/jup/proj_spam_ham/smsspamcollection/SMSSpamCollection', sep='\t', names=["label", "message"])
b1['length'] = b1['message'].apply(len)
plt.figure(b2 = (10, 6))
b1['length'].plot(b3 = 50, kind='hist', color='blue')
plt.title('Histogram of Message Length')
plt.xlabel('Length')
plt.ylabel('Frequency')
plt.show()
b1.hist(b4 = 'length', by='label', b3=50, b2=(12, 6), color='blue')
plt.show()
def fonk1(mess):
    b5 = [char for char in mess if char not in string.punctuation]
    b5 = ''.join(b5)
    b6 = [word for word in b5.split() if word.lower() not in stopwords.words('english')]
    return b6
b7 = Pipeline([
    ('bow', CountVectorizer(b8 = text_process)),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB()),
])
msg_train, msg_test, label_train, b9 = train_test_split(b1['message'], b1['label'], test_size=0.2)
b7.fit(msg_train, label_train)
b10 = b7.predict(msg_test)
print("CLASSIFICATION REPORT")
print(classification_report(b10, b9))
print("ACCURACY")
print(accuracy_score(b10, b9))