import pandas as pd
import matplotlib.pyplot as plt
import string
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score
nltk.download('stopwords')
data_path = '/Users/dineshmaharana/jup/proj_spam_ham/smsspamcollection/SMSSpamCollection'
messages = pd.read_csv(data_path, sep='\t', names=["label", "message"])
messages['length'] = messages['message'].apply(len)
plt.figure(figsize=(10, 6))
messages['length'].plot(bins=50, kind='hist')
plt.title('Message Length Distribution')
plt.xlabel('Message Length')
plt.ylabel('Frequency')
plt.show()
messages.hist(column='length', by='label', bins=50, figsize=(12, 6))
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
msg_train, msg_test, label_train, label_test = train_test_split(
    messages['message'], messages['label'], test_size=0.2, random_state=42)
pipeline.fit(msg_train, label_train)
predictions = pipeline.predict(msg_test)
print("CLASSIFICATION REPORT")
print(classification_report(label_test, predictions))
print("ACCURACY")
print(accuracy_score(label_test, predictions))