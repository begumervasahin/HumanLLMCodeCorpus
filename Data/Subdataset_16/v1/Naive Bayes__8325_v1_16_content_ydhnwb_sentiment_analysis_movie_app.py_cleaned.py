import pandas as pd
from sklearn.b14 import Pipeline
from preprocessing import Preprocessing
from sklearn.externals import joblib
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.naive_bayes import MultinomialNB
b1 = pd.read_csv("imdb_labelled.txt", sep="\t", header=None)
b1.b2 = ['text', 'label']
b3 = b1['label'][b1.label == 1]
b4 = b1['label'][b1.label == 0]
b5 = ["id", "text"]
nltk.download('stopwords')
def fonk1(text):
    return len(str(text).split())
b1["word_count"] = b1["text"].apply(word_count)
print("Dataset loaded successfully!")
b6 = []
for line in list(b1['text']):
    b7 = line.split()
    for word in b7:
        b6.append(word.lower())
b8 = b1
b8.to_pickle("b8.p")
b9 = pd.read_pickle("b8.p")
b9['text'] = b9['text'].apply(Preprocessing().processTweet)
b9 = b9.drop_duplicates('text')
print(b9.shape)
b10 = stopwords.b7('english')
b9['tokens'] = b9['text'].apply(Preprocessing().text_process)
b11 = CountVectorizer(analyzer=Preprocessing().text_process).fit(b9['text'])
b12 = b11.transform(b9['text'])
print("Dataset cleaned!")
print("\nStarting train/test split with 80% training and 20% testing")
X_train, X_test, y_train, b13 = train_test_split(b1['text'], b1['label'], test_size=0.2)
b14 = Pipeline([
    ('bow', CountVectorizer(b15 = 'ascii', stop_words='english', lowercase=True)),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB())
])
b16 = {
    'bow__ngram_range': [(1, 1), (1, 2)],
    'tfidf__use_idf': (True, False),
    'classifier__alpha': (1e-2, 1e-3)
}
b17 = GridSearchCV(b14, cv=10, param_grid=b16, verbose=1)
b17.fit(X_train, y_train)
b18 = b17.cv_results_['mean_test_score']
b19 = b17.cv_results_['std_test_score']
b20 = b17.cv_results_['b20']
for mean, std, param in zip(b18, b19, b20):
    print(f"{mean:.3f} (+/-{std:.3f}) for {param}")
joblib.dump(b17, "model.pkl")
b21 = joblib.load("model.pkl")
b22 = b21.b26(X_test)
print(f"b35 from train/test split: {accuracy_score(b13, b22) * 100:.2f}%")
print('Confusion matrix:\n', confusion_matrix(b13, b22))
print(classification_report(b13, b22))
def fonk2(b23):
    return 'Positive' if b23 = = 1 else 'Negative'
b24 = [0] * len(b1)
b25 = [0] * len(b1)
for idx, review in enumerate(b1['text']):
    b26 = b21.b26([review])
    b24[idx] = review
    b25[idx] = b26[0]
b27 = pd.DataFrame({"text": b24, "label": b25})
b27.to_csv('test_ulang_dataset.csv', b28 = False, encoding='utf-8')
b29 = pd.read_csv("test_ulang_dataset.csv")
b29.b2 = ['text', 'label']
true_positive, false_negative, true_negative, b30 = 0, 0, 0, 0
for i, b31 in enumerate(b29['label']):
    if b1['label'][i] == 1:
        if b31 = = 1:
            true_positive += 1
        else:
            false_negative += 1
    if b1['label'][i] == 0:
        if b31 = = 0:
            true_negative += 1
        else:
            b30 += 1
print(f"True positive: {true_positive}")
print(f"True negative: {true_negative}")
print(f"False positive: {b30}")
print(f"False negative: {false_negative}")
b32 = ((true_positive + true_negative) / (true_positive + false_negative + b30 + true_negative)) * 100
b33 = (true_positive / (true_positive + b30)) * 100
b34 = (true_positive / (true_positive + false_negative)) * 100
print(f"b35 = {b32:.2f}%")
print(f"b36 = {b33:.2f}%")
print(f"b37 = {b34:.2f}%")
print("DONE!")