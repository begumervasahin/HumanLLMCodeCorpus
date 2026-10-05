import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.naive_bayes import MultinomialNB
from preprocessing import Preprocessing
imdb_dataset = pd.read_csv("imdb_labelled.txt", sep="\t", header=None)
imdb_dataset.columns = ['text', 'label']
preprocessor = Preprocessing()
imdb_dataset["text"] = imdb_dataset["text"].apply(preprocessor.process_tweet)
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
grid_search = GridSearchCV(pipeline, cv=10, param_grid=parameters, verbose=1)
grid_search.fit(X_train, y_train)
model_file = "model.pkl"
joblib.dump(grid_search, model_file)
model_NB = joblib.load(model_file)
y_preds = model_NB.predict(X_test)
accuracy = accuracy_score(y_test, y_preds) * 100
conf_matrix = confusion_matrix(y_test, y_preds)
class_report = classification_report(y_test, y_preds)
print('Accuracy: ', accuracy, "%")
print('Confusion Matrix:\n', conf_matrix)
print('Classification Report:\n', class_report)
predictions = pd.DataFrame({'text': X_test, 'label': y_preds})
predictions.to_csv('predictions.csv', index=False)
true_positive = sum((y_test == 1) & (y_preds == 1))
false_negative = sum((y_test == 1) & (y_preds == 0))
true_negative = sum((y_test == 0) & (y_preds == 0))
false_positive = sum((y_test == 0) & (y_preds == 1))
precision = true_positive / (true_positive + false_positive) * 100
recall = true_positive / (true_positive + false_negative) * 100
print("True Positive:", true_positive)
print("False Negative:", false_negative)
print("True Negative:", true_negative)
print("False Positive:", false_positive)
print("Precision:", precision, "%")
print("Recall:", recall, "%")
print("DONE!")