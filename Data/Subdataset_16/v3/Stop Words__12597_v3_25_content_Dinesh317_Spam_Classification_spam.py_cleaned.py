import pandas as pd
import matplotlib.pyplot as plt
import string
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.b8 import Pipeline
from sklearn.metrics import classification_report, accuracy_score
nltk.download('stopwords')
b1 = '/Users/dineshmaharana/jup/proj_spam_ham/smsspamcollection/SMSSpamCollection'
b2 = pd.read_csv(b1, sep='\t', names=["label", "message"])
b2['length'] = b2['message'].apply(len)
plt.figure(b3 = (10, 6))
b2['length'].plot(b4 = 50, kind='hist')
plt.title('Message Length Distribution')
plt.xlabel('Message Length')
plt.ylabel('Frequency')
plt.show()
b2.hist(b5 = 'length', by='label', b4=50, b3=(12, 6))
plt.show()
def fonk1(mess):
    b6 = [char for char in mess if char not in string.punctuation]
    b6 = ''.join(b6)
    b7 = [word for word in b6.split() if word.lower() not in stopwords.words('english')]
    return b7
b8 = Pipeline([
    ('bow', CountVectorizer(b9 = text_process)),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB()),
])
msg_train, msg_test, label_train, b10 = train_test_split(
    b2['message'], b2['label'], b11 = 0.2, random_state=42)
b8.fit(msg_train, label_train)
b12 = b8.predict(msg_test)
print("CLASSIFICATION REPORT")
print(classification_report(b10, b12))
print("ACCURACY")
print(accuracy_score(b10, b12))