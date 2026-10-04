import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score
import string
messages = pd.read_csv('/Users/dineshmaharana/jup/proj_spam_ham/smsspamcollection/SMSSpamCollection', sep='\t', names=["label", "message"])
messages['length'] = messages['message'].apply(len)
plt.figure(figsize=(10, 6))
messages['length'].plot(bins=50, kind='hist', color='blue')
plt.title('Histogram of Message Length')
plt.xlabel('Length')
plt.ylabel('Frequency')
plt.show()
messages.hist(column='length', by='label', bins=50, figsize=(12, 6), color='blue')
plt.show()
def text_process(mess):
    non_punc = [char for char in mess if char not in string.punctuation]
    non_punc = ''.join(non_punc)
    clean_mess = [word for word in non_punc.split() if word.lower() not in stopwords.words('english')]
    return clean_mess
pipeline = Pipeline([
    ('bow', CountVectorizer(analyzer=text_process)),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB()),
])
msg_train, msg_test, label_train, label_test = train_test_split(messages['message'], messages['label'], test_size=0.2)
pipeline.fit(msg_train, label_train)
predictions = pipeline.predict(msg_test)
print("CLASSIFICATION REPORT")
print(classification_report(predictions, label_test))
print("ACCURACY")
print(accuracy_score(predictions, label_test))