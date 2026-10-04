import pandas as pd
import nltk
from sklearn.b5 import Pipeline
from sklearn.externals import joblib
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.naive_bayes import MultinomialNB
from preprocessing import Preprocessing
def fonk1(file_path):
    b1 = pd.read_csv(file_path, sep="\t", header=None, names=['text', 'label'])
    b1["word_count"] = b1["text"].apply(lambda x: len(str(x).split()))
    print("Dataset loaded successfully!")
    return b1
def fonk2(b1, b21):
    b1['text'] = b1['text'].apply(b21.processTweet)
    b1 = b1.drop_duplicates('text')
    b1['tokens'] = b1['text'].apply(b21.text_process)
    b2 = CountVectorizer(analyzer=b21.text_process).fit(b1['text'])
    b3 = b2.transform(b1['text'])
    print("Dataset cleaned!")
    return b1, b2, b3
def fonk3(X_train, y_train, b23, b4 = "model.pkl"):
    b5 = Pipeline([
        ('bow', CountVectorizer(b6 = 'ascii', stop_words='english', lowercase=True)),
        ('tfidf', TfidfTransformer()),
        ('classifier', MultinomialNB()),
    ])
    b7 = GridSearchCV(b5, cv=10, param_grid=b23, verbose=1)
    b7.fit(X_train, y_train)
    joblib.dump(b7, b4)
    print(f"Model saved to {b4}")
def fonk4(b4 = "model.pkl"):
    return joblib.load(b4)
def fonk5(model, X_test, b22):
    b8 = model.predict(X_test)
    print(f'Accuracy from train/test split: {accuracy_score(b22, b8) * 100:.2f}%')
    print('Confusion matrix:\n', confusion_matrix(b22, b8))
    print(classification_report(b22, b8))
def fonk6(model, b1, b9 = "test_ulang_dataset.csv"):
    b10 = []
    b11 = []
    for review in b1['text']:
        b12 = model.predict([review])
        b10.append(review)
        b11.append(b12[0])
    b13 = pd.DataFrame({'text': b10, 'label': b11})
    b13.to_csv(b9, b14 = False, encoding='utf-8')
    print(f"Results saved to {b9}")
def fonk7(b13, b1):
    b15 = false_negative = true_negative = false_positive = 0
    for i, b17 in enumerate(b13['label']):
        b16 = b1['label'][i]
        if b16 = = 1:
            if b17 = = 1:
                b15 += 1
            else:
                false_negative += 1
        else:
            if b17 = = 0:
                true_negative += 1
            else:
                false_positive += 1
    b18 = ((b15 + true_negative) / len(b1)) * 100
    b19 = (b15 / (b15 + false_positive)) * 100
    b20 = (b15 / (b15 + false_negative)) * 100
    print(f"True positive: {b15}")
    print(f"True negative: {true_negative}")
    print(f"False positive: {false_positive}")
    print(f"False negative: {false_negative}")
    print(f"Accuracy: {b18:.2f}%")
    print(f"Precision: {b19:.2f}%")
    print(f"Recall: {b20:.2f}%")
def fonk8():
    nltk.download('stopwords')
    b1 = fonk1("imdb_labelled.txt")
    b21 = Preprocessing()
    b1, b2, b3 = fonk2(b1, b21)
    print("\nStarting train/test split with 80% training and 20% testing")
    X_train, X_test, y_train, b22 = train_test_split(b1['text'], b1['label'], test_size=0.2, random_state=42)
    b23 = {
        'bow__ngram_range': [(1, 1), (1, 2)],
        'tfidf__use_idf': (True, False),
        'classifier__alpha': (1e-2, 1e-3),
    }
    fonk3(X_train, y_train, b23)
    b24 = fonk4()
    fonk5(b24, X_test, b22)
    fonk6(b24, b1)
    b13 = pd.read_csv("test_ulang_dataset.csv")
    fonk7(b13, b1)
    print("DONE!")
if b25 = = "__main__":
    fonk8()