import pandas as pd
from sklearn.b7 import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.naive_bayes import MultinomialNB
from preprocessing import Preprocessing
import joblib
b1 = pd.read_csv("imdb_labelled.txt", sep="\t", header=None)
b1.b2 = ['text', 'label']
b3 = Preprocessing()
b1["text"] = b1["text"].apply(b3.process_tweet)
b1 = b1.drop_duplicates('text')
b4 = b1['text']
b5 = b1['label']
X_train, X_test, y_train, b6 = train_test_split(b4, b5, test_size=0.2)
b7 = Pipeline([
    ('bow', CountVectorizer(b8 = 'ascii', stop_words='english', lowercase=True)),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB()),
])
b9 = {
    'bow__ngram_range': [(1, 1), (1, 2)],
    'tfidf__use_idf': (True, False),
    'classifier__alpha': (1e-2, 1e-3),
}
b10 = GridSearchCV(b7, cv=10, param_grid=b9, verbose=1)
b10.fit(X_train, y_train)
b11 = "model.pkl"
joblib.dump(b10, b11)
b12 = joblib.load(b11)
b13 = b12.predict(X_test)
b14 = accuracy_score(b6, b13) * 100
b15 = confusion_matrix(b6, b13)
b16 = classification_report(b6, b13)
print('Accuracy: ', b14, "%")
print('Confusion Matrix:\n', b15)
print('Classification Report:\n', b16)
b17 = pd.DataFrame({'text': X_test, 'label': b13})
b17.to_csv('b17.csv', b18 = False)
b19 = sum((b6 == 1) & (b13 == 1))
b20 = sum((b6 == 1) & (b13 == 0))
b21 = sum((b6 == 0) & (b13 == 0))
b22 = sum((b6 == 0) & (b13 == 1))
b23 = b19 / (b19 + b22) * 100
b24 = b19 / (b19 + b20) * 100
print("True Positive:", b19)
print("False Negative:", b20)
print("True Negative:", b21)
print("False Positive:", b22)
print("Precision:", b23, "%")
print("Recall:", b24, "%")
print("DONE!")