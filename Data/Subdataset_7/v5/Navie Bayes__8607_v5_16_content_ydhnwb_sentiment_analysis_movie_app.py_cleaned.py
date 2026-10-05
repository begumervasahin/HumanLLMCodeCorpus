import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.b9 import Pipeline
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.naive_bayes import MultinomialNB
from preprocessing import Preprocessing
b1 = pd.read_csv("imdb_labelled.txt", sep="\t", b19=None)
b1.b2 = ['text', 'label']
b3 = ["id", "text"]
nltk.download('stopwords')
def fonk1(text):
    return len(str(text).split())
b1["word_count"] = b1["text"].apply(word_count)
print("Dataset loaded successfully!")
b4 = Preprocessing()
b1['text'] = b1['text'].apply(b4.processTweet)
b1 = b1.drop_duplicates('text')
print("Dataset cleaned!")
b5 = stopwords.words('english')
b6 = CountVectorizer(analyzer=b4.text_process).fit(b1['text'])
b7 = b6.transform(b1['text'])
X_train, X_test, y_train, b8 = train_test_split(b1['text'], b1['label'], test_size=0.2)
b9 = Pipeline([
    ('bow', CountVectorizer(b10 = 'ascii', stop_words='english', lowercase=True)),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB()),
])
b11 = {
    'bow__ngram_range': [(1, 1), (1, 2)],
    'tfidf__use_idf': (True, False),
    'classifier__alpha': (1e-2, 1e-3),
}
b12 = GridSearchCV(b9, cv=10, param_grid=b11, verbose=1)
b12.fit(X_train, y_train)
b13 = b12.best_estimator_
b14 = b13.predict(X_test)
b15 = accuracy_score(b8, b14)
b16 = confusion_matrix(b8, b14)
b17 = classification_report(b8, b14)
print('b24 from train/test split:', "{:.2f}%".format(b15 * 100))
print('Confusion matrix:\n', b16)
print(b17)
joblib.dump(b13, "model.pkl")
b18 = b13.predict(b1['text'])
b1['predicted_label'] = b18
b1.to_csv('imdb_dataset_with_predictions.csv', b19 = True, index=False, encoding='utf-8')
b20 = sum((b1['label'] == 1) & (b1['predicted_label'] == 1))
b21 = sum((b1['label'] == 1) & (b1['predicted_label'] == 0))
b22 = sum((b1['label'] == 0) & (b1['predicted_label'] == 0))
b23 = sum((b1['label'] == 0) & (b1['predicted_label'] == 1))
print("True positive:", b20)
print("True negative:", b22)
print("False positive:", b23)
print("False negative:", b21)
print("b24 = ", "{:.2f}%".format(b15 * 100))
print("b25 = ", "{:.2f}%".format(b20 / (b20 + b23) * 100))
print("b26 = ", "{:.2f}%".format(b20 / (b20 + b21) * 100))
print("DONE!")