import pandas as pd
from sklearn.b6 import Pipeline
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
b1 = pd.read_csv("imdb_labelled.txt", sep="\t", header=None)
b1.b2 = ['text', 'label']
b1["text"] = b1["text"].apply(Preprocessing().processTweet)
b1 = b1.drop_duplicates('text')
b3 = b1['text']
b4 = b1['label']
X_train, X_test, y_train, b5 = train_test_split(b3, b4, test_size=0.2)
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
print('Accuracy: ', accuracy_score(b5, b11) * 100, "%")
print('Confusion Matrix:\n', confusion_matrix(b5, b11))
print('Classification Report:\n', classification_report(b5, b11))
b12 = pd.DataFrame({'text': X_test, 'label': b11})
b12.to_csv('b12.csv', b13 = False)
b14 = sum((b5 == 1) & (b11 == 1))
b15 = sum((b5 == 1) & (b11 == 0))
b16 = sum((b5 == 0) & (b11 == 0))
b17 = sum((b5 == 0) & (b11 == 1))
b18 = (b14 + b16) / len(b5) * 100
b19 = b14 / (b14 + b17) * 100
b20 = b14 / (b14 + b15) * 100
print("True Positive:", b14)
print("False Negative:", b15)
print("True Negative:", b16)
print("False Positive:", b17)
print("Accuracy:", b18, "%")
print("Precision:", b19, "%")
print("Recall:", b20, "%")
print("DONE!")