import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.pipeline import Pipeline
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.naive_bayes import MultinomialNB
from preprocessing import Preprocessing
imdb_dataset = pd.read_csv("imdb_labelled.txt", sep="\t", header=None)
imdb_dataset.columns = ['text', 'label']
COLNAMES = ["id", "text"]
nltk.download('stopwords')
def word_count(text):
    return len(str(text).split())
imdb_dataset["word_count"] = imdb_dataset["text"].apply(word_count)
print("Dataset loaded successfully!")
preprocessor = Preprocessing()
imdb_dataset['text'] = imdb_dataset['text'].apply(preprocessor.processTweet)
imdb_dataset = imdb_dataset.drop_duplicates('text')
print("Dataset cleaned!")
eng_stop_words = stopwords.words('english')
bow_transformer = CountVectorizer(analyzer=preprocessor.text_process).fit(imdb_dataset['text'])
messages_bow = bow_transformer.transform(imdb_dataset['text'])
X_train, X_test, y_train, y_test = train_test_split(imdb_dataset['text'], imdb_dataset['label'], test_size=0.2)
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
model_NB = grid.best_estimator_
y_preds = model_NB.predict(X_test)
print('Accuracy from train/test split:', str(accuracy_score(y_test, y_preds) * 100) + "%")
print('Confusion matrix:\n', confusion_matrix(y_test, y_preds))
print(classification_report(y_test, y_preds))
joblib.dump(model_NB, "model.pkl")
predicted_labels = model_NB.predict(imdb_dataset['text'])
imdb_dataset['predicted_label'] = predicted_labels
imdb_dataset.to_csv('imdb_dataset_with_predictions.csv', header=True, index=False, encoding='utf-8')
true_positive = sum((imdb_dataset['label'] == 1) & (imdb_dataset['predicted_label'] == 1))
false_negative = sum((imdb_dataset['label'] == 1) & (imdb_dataset['predicted_label'] == 0))
true_negative = sum((imdb_dataset['label'] == 0) & (imdb_dataset['predicted_label'] == 0))
false_positive = sum((imdb_dataset['label'] == 0) & (imdb_dataset['predicted_label'] == 1))
print("True positive:", true_positive)
print("True negative:", true_negative)
print("False positive:", false_positive)
print("False negative:", false_negative)
print("Accuracy =", "{:.2f}%".format((true_positive + true_negative) / len(imdb_dataset) * 100))
print("Precision =", "{:.2f}%".format(true_positive / (true_positive + false_positive) * 100))
print("Recall =", "{:.2f}%".format(true_positive / (true_positive + false_negative) * 100))
print("DONE!")