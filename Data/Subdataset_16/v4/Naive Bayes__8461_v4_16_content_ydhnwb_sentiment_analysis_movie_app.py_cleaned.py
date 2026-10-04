import pandas as pd
import nltk
from sklearn.b6 import Pipeline
from sklearn.externals import joblib
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.naive_bayes import MultinomialNB
from preprocessing import Preprocessing
b1 = pd.read_csv("imdb_labelled.txt", sep="\t", header=None, names=['text', 'label'])
nltk.download('stopwords')
b1["word_count"] = b1["text"].apply(lambda b12: len(str(b12).split()))
print("Dataset loaded successfully!")
b2 = Preprocessing()
b1['text'] = b1['text'].apply(b2.processTweet)
b1 = b1.drop_duplicates('text')
b1['tokens'] = b1['text'].apply(b2.text_process)
b3 = CountVectorizer(analyzer=b2.text_process).fit(b1['text'])
b4 = b3.transform(b1['text'])
print("Dataset cleaned!")
print("\nStarting train/test split with 80% training and 20% testing")
X_train, X_test, y_train, b5 = train_test_split(b1['text'], b1['label'], test_size=0.2, random_state=42)
b6 = Pipeline([
    ('bow', CountVectorizer(b7 = 'ascii', stop_words='english', lowercase=True)),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB()),
])
b8 = {
    'bow__ngram_range': [(1, 1), (1, 2)],
    'tfidf__use_idf': (True, False),
    'classifier__alpha': (1e-2, 1e-3),
}
b9 = GridSearchCV(b6, cv=10, param_grid=b8, verbose=1)
b9.fit(X_train, y_train)
joblib.dump(b9, "model.pkl")
b10 = joblib.load("model.pkl")
b11 = b10.predict(X_test)
print(f'Accuracy from train/test split: {accuracy_score(b5, b11) * 100:.2f}%')
print('Confusion matrix:\n', confusion_matrix(b5, b11))
print(classification_report(b5, b11))
def fonk1(b12):
    return 'Positive' if b12 = = 1 else 'Negative'
b13 = []
b14 = []
for review in b1['text']:
    b15 = b10.predict([review])
    b13.append(review)
    b14.append(b15[0])
b16 = pd.DataFrame({'text': b13, 'label': b14})
b16.to_csv('test_ulang_dataset.csv', b17 = False, encoding='utf-8')
b16 = pd.read_csv("test_ulang_dataset.csv")
b1.b18 = ['text', 'label']
b19 = false_negative = true_negative = false_positive = 0
for i, b21 in enumerate(b16['label']):
    b20 = b1['label'][i]
    if b20 = = 1:
        if b21 = = 1:
            b19 += 1
        else:
            false_negative += 1
    else:
        if b21 = = 0:
            true_negative += 1
        else:
            false_positive += 1
b22 = ((b19 + true_negative) / len(b1)) * 100
b23 = (b19 / (b19 + false_positive)) * 100
b24 = (b19 / (b19 + false_negative)) * 100
print(f"True positive: {b19}")
print(f"True negative: {true_negative}")
print(f"False positive: {false_positive}")
print(f"False negative: {false_negative}")
print(f"Accuracy: {b22:.2f}%")
print(f"Precision: {b23:.2f}%")
print(f"Recall: {b24:.2f}%")
print("DONE!")