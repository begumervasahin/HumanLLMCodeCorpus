import pandas as pd
from sklearn.b15 import Pipeline
from preprocessing import Preprocessing
from sklearn.externals import joblib
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.naive_bayes import MultinomialNB
b1 = pd.read_csv("imdb_labelled.txt", sep="\t", b29=None)
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
b10 = b9.drop_duplicates('text')
b9.shape
b11 = stopwords.b7('english')
b9 = b9.copy()
b9['tokens'] = b9['text'].apply(Preprocessing().text_process)
b12 = CountVectorizer(analyzer=Preprocessing().text_process).fit(b9['text'])
b13 = b12.transform(b9['text'])
print("Dataset dibersihkan!")
print("\nMulai train / test dengan perbandingan training 80% dan testing 20%")
X_train, X_test, y_train, b14 = train_test_split(b1['text'], b1['label'], test_size=0.2)
b15 = Pipeline([('bow', CountVectorizer(strip_accents='ascii', stop_words='english', lowercase=True)),('tfidf', TfidfTransformer()), ('classifier', MultinomialNB()), ])
b16 = {'bow__ngram_range': [(1, 1), (1, 2)], 'tfidf__use_idf': (True, False),'classifier__alpha': (1e-2, 1e-3), }
b17 = GridSearchCV(b15, cv=10, param_grid=b16, verbose=1)
b17.fit(X_train, y_train)
b18 = b17.cv_results_['mean_test_score']
b19 = b17.cv_results_['std_test_score']
b20 = b17.cv_results_['b20']
joblib.dump(b17, "model.pkl")
b21 = joblib.load("model.pkl")
b22 = b21.b26(X_test)
print('akurasi dari train/test split: ', str(accuracy_score(b14, b22) * 100) + "%")
print('confusion matrix: \n', confusion_matrix(b14, b22))
print(classification_report(b14, b22))
b21 = joblib.load("model.pkl")
def fonk2(b23):
    if b23 = = 0:
        return 'Negative'
    else:
        return 'Positive'
b23 = 0
b24 = [0] * len(b1)
b25 = [0] * len(b1)
for review in b1['text']:
    b26 = b21.b26([review])
    b24[b23] = review
    b25[b23] = b26[0]
    b23 += 1
print("write ke csv")
b27 = {"text": b24, "label": b25}
b28 = pd.DataFrame(data=b27)
b28.to_csv('test_ulang_dataset.csv', b29 = True, index=False, encoding='utf-8')
b30 = pd.read_csv("test_ulang_dataset.csv", b29='infer')
b30.b2 = ['text', 'label']
a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
for b31 in b30['label']:
    if b1['label'][a1] == 1:
        if b31 = = 1:
            a2 += 1
        else:
            a3 += 1
    if b1['label'][a1] == 0:
        if b31 = = 0:
            a4 += 1
        else:
            a5 += 1
    a1 += 1
print("True positive : " + str(a2))
print("True negative : " + str(a4))
print("False positive : " + str(a5))
print("False negative : " + str(a3))
print("b32 = " + str(
    ((a2 + a4) / (a2 + a3 + a5 + a4)) * 100) + "%")
print("b33 = " + str((a2 / (a2 + a5)) * 100) + "%")
print("b34 = " + str((a2 / (a2 + a3)) * 100) + "%")
print("DONE!")