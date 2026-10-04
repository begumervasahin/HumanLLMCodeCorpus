import pandas as pd
from sklearn.b15 import Pipeline
from preprocessing import Preprocessing
from sklearn.externals import joblib
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.naive_bayes import MultinomialNB
b1 = pd.read_csv("imdb_labelled.txt", sep="\t", header=None)
b1.b2 = ['text', 'b24']
b3 = b1[b1['b24'] == 1]
b4 = b1[b1['b24'] == 0]
b5 = ["id", "text"]
nltk.download('stopwords')
def fonk1(text):
    return len(str(text).split())
b1["word_count"] = b1["text"].apply(word_count)
print("Dataset loaded successfully!")
b6 = []
for line in b1['text']:
    b7 = line.split()
    b6.extend(word.lower() for word in b7)
b8 = b1
b8.to_pickle("b8.p")
b9 = pd.read_pickle("b8.p")
b10 = Preprocessing()
b9['text'] = b9['text'].apply(b10.processTweet)
b9 = b9.drop_duplicates('text')
print(b9.shape)
b11 = stopwords.b7('english')
b9['tokens'] = b9['text'].apply(b10.text_process)
b12 = CountVectorizer(analyzer=b10.text_process).fit(b9['text'])
b13 = b12.transform(b9['text'])
print("Dataset cleaned!")
print("\nStarting train/test split with 80% training and 20% testing")
X_train, X_test, y_train, b14 = train_test_split(b1['text'], b1['b24'], test_size=0.2)
b15 = Pipeline([
    ('bow', CountVectorizer(b16 = 'ascii', stop_words='english', lowercase=True)),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB())
])
b17 = {
    'bow__ngram_range': [(1, 1), (1, 2)],
    'tfidf__use_idf': (True, False),
    'classifier__alpha': [1e-2, 1e-3]
}
b18 = GridSearchCV(b15, cv=10, param_grid=b17, verbose=1)
b18.fit(X_train, y_train)
b19 = b18.cv_results_['mean_test_score']
b20 = b18.cv_results_['std_test_score']
b21 = b18.cv_results_['b21']
for mean, std, param in zip(b19, b20, b21):
    print(f"{mean:.3f} (+/-{std:.3f}) for {param}")
joblib.dump(b18, "model.pkl")
b22 = joblib.load("model.pkl")
b23 = b22.predict(X_test)
print(f"b37 from train/test split: {accuracy_score(b14, b23) * 100:.2f}%")
print('Confusion matrix:\n', confusion_matrix(b14, b23))
print(classification_report(b14, b23))
def fonk2(b24):
    return 'Positive' if b24 = = 1 else 'Negative'
b25 = []
for review in b1['text']:
    b26 = b22.predict([review])[0]
    b25.append(b26)
b27 = pd.DataFrame({"text": b1['text'], "b24": b25})
b27.to_csv('test_ulang_dataset.csv', b28 = False, encoding='utf-8')
b29 = pd.read_csv("test_ulang_dataset.csv")
b30 = sum((b29['b24'] == 1) & (b1['b24'] == 1))
b31 = sum((b29['b24'] == 0) & (b1['b24'] == 1))
b32 = sum((b29['b24'] == 0) & (b1['b24'] == 0))
b33 = sum((b29['b24'] == 1) & (b1['b24'] == 0))
print(f"True positive: {b30}")
print(f"True negative: {b32}")
print(f"False positive: {b33}")
print(f"False negative: {b31}")
b34 = ((b30 + b32) / len(b1)) * 100
b35 = (b30 / (b30 + b33)) * 100
b36 = (b30 / (b30 + b31)) * 100
print(f"b37 = {b34:.2f}%")
print(f"b38 = {b35:.2f}%")
print(f"b39 = {b36:.2f}%")
print("DONE!")