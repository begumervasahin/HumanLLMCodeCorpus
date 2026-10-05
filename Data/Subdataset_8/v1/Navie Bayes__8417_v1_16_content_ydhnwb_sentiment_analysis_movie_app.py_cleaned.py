import pandas as pd
from sklearn.pipeline import Pipeline
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
imdb_dataset = pd.read_csv("imdb_labelled.txt", sep="\t", header=None)
imdb_dataset.columns = ['text', 'label']
imdb_dataset["text"] = imdb_dataset["text"].apply(Preprocessing().processTweet)
imdb_dataset = imdb_dataset.drop_duplicates('text')
X = imdb_dataset['text']
y = imdb_dataset['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
pipeline = Pipeline([
    ('bow', CountVectorizer(strip_accents='ascii', stop_words='english', lowercase=True)),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB()),
])
parameters = {
    'bow__ngram_range': [(1, 1), (1, 2)],
    'tfidf__use_idf': (True, False),
    'classifier__alpha': (1e-2, 1e-3),
}
grid = GridSearchCV(pipeline, cv=10, param_grid=parameters, verbose=1)
grid.fit(X_train, y_train)
joblib.dump(grid, "model.pkl")
model_NB = joblib.load("model.pkl")
y_preds = model_NB.predict(X_test)
print('Accuracy: ', accuracy_score(y_test, y_preds) * 100, "%")
print('Confusion Matrix:\n', confusion_matrix(y_test, y_preds))
print('Classification Report:\n', classification_report(y_test, y_preds))
predictions = pd.DataFrame({'text': X_test, 'label': y_preds})
predictions.to_csv('predictions.csv', index=False)
true_positive = sum((y_test == 1) & (y_preds == 1))
false_negative = sum((y_test == 1) & (y_preds == 0))
true_negative = sum((y_test == 0) & (y_preds == 0))
false_positive = sum((y_test == 0) & (y_preds == 1))
accuracy = (true_positive + true_negative) / len(y_test) * 100
precision = true_positive / (true_positive + false_positive) * 100
recall = true_positive / (true_positive + false_negative) * 100
print("True Positive:", true_positive)
print("False Negative:", false_negative)
print("True Negative:", true_negative)
print("False Positive:", false_positive)
print("Accuracy:", accuracy, "%")
print("Precision:", precision, "%")
print("Recall:", recall, "%")
print("DONE!")