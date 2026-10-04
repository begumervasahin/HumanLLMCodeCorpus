import pandas as pd
import matplotlib.pyplot as plt
import string
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.b6 import Pipeline
from sklearn.metrics import classification_report, accuracy_score
nltk.download('stopwords')
b1 = pd.read_csv('/Users/dineshmaharana/jup/proj_spam_ham/smsspamcollection/SMSSpamCollection', sep='\t', names=["label", "message"])
b1['length'] = b1['message'].apply(len)
b1['length'].plot(b2 = 50, kind='hist')
plt.title('Message Length Distribution')
plt.xlabel('Message Length')
plt.ylabel('Frequency')
plt.show()
b1.hist(b3 = 'length', by='label', b2=50, figsize=(12, 6))
plt.show()
def fonk1(mess):
    b4 = [char for char in mess if char not in string.punctuation]
    b4 = ''.join(b4)
    b5 = [word for word in b4.split() if word.lower() not in stopwords.words('english')]
    return b5
b6 = Pipeline([
    ('bow', CountVectorizer(b7 = text_process)),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB()),
])
msg_train, msg_test, label_train, b8 = train_test_split(b1['message'], b1['label'], test_size=0.2)
b6.fit(msg_train, label_train)
b9 = b6.predict(msg_test)
print("CLASSIFICATION REPORT")
print(classification_report(b9, b8))
print("ACCURACY")
print(accuracy_score(b9, b8))