import pandas as pd
from sklearn.pipeline import Pipeline
from preprocessing import Preprocessing
from sklearn.externals import joblib
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.naive_bayes import MultinomialNB
imdb_dataset = pd.read_csv("imdb_labelled.txt", sep="\t", header=None)
imdb_dataset.columns = ['text', 'label']
positives = imdb_dataset[imdb_dataset['label'] == 1]
negatives = imdb_dataset[imdb_dataset['label'] == 0]
COLNAMES = ["id", "text"]
nltk.download('stopwords')
def word_count(text):
    return len(str(text).split())
imdb_dataset["word_count"] = imdb_dataset["text"].apply(word_count)
print("Dataset loaded successfully!")
all_words = []
for line in imdb_dataset['text']:
    words = line.split()
    all_words.extend(word.lower() for word in words)
dataset = imdb_dataset
dataset.to_pickle("dataset.p")
dataset_pickle = pd.read_pickle("dataset.p")
preprocessor = Preprocessing()
dataset_pickle['text'] = dataset_pickle['text'].apply(preprocessor.processTweet)
dataset_pickle = dataset_pickle.drop_duplicates('text')
print(dataset_pickle.shape)
eng_stop_words = stopwords.words('english')
dataset_pickle['tokens'] = dataset_pickle['text'].apply(preprocessor.text_process)
bow_transformer = CountVectorizer(analyzer=preprocessor.text_process).fit(dataset_pickle['text'])
messages_bow = bow_transformer.transform(dataset_pickle['text'])
print("Dataset cleaned!")
print("\nStarting train/test split with 80% training and 20% testing")
X_train, X_test, y_train, y_test = train_test_split(imdb_dataset['text'], imdb_dataset['label'], test_size=0.2)
pipeline = Pipeline([
    ('bow', CountVectorizer(strip_accents='ascii', stop_words='english', lowercase=True)),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB())
])
parameters = {
    'bow__ngram_range': [(1, 1), (1, 2)],
    'tfidf__use_idf': (True, False),
    'classifier__alpha': [1e-2, 1e-3]
}
grid_search = GridSearchCV(pipeline, cv=10, param_grid=parameters, verbose=1)
grid_search.fit(X_train, y_train)
means = grid_search.cv_results_['mean_test_score']
stds = grid_search.cv_results_['std_test_score']
params = grid_search.cv_results_['params']
for mean, std, param in zip(means, stds, params):
    print(f"{mean:.3f} (+/-{std:.3f}) for {param}")
joblib.dump(grid_search, "model.pkl")
model_NB = joblib.load("model.pkl")
y_preds = model_NB.predict(X_test)
print(f"Accuracy from train/test split: {accuracy_score(y_test, y_preds) * 100:.2f}%")
print('Confusion matrix:\n', confusion_matrix(y_test, y_preds))
print(classification_report(y_test, y_preds))
def label_to_str(label):
    return 'Positive' if label == 1 else 'Negative'
predicted_labels = []
for review in imdb_dataset['text']:
    predicted_label = model_NB.predict([review])[0]
    predicted_labels.append(predicted_label)
output_df = pd.DataFrame({"text": imdb_dataset['text'], "label": predicted_labels})
output_df.to_csv('test_ulang_dataset.csv', index=False, encoding='utf-8')
hasil_test_ulang = pd.read_csv("test_ulang_dataset.csv")
true_positive = sum((hasil_test_ulang['label'] == 1) & (imdb_dataset['label'] == 1))
false_negative = sum((hasil_test_ulang['label'] == 0) & (imdb_dataset['label'] == 1))
true_negative = sum((hasil_test_ulang['label'] == 0) & (imdb_dataset['label'] == 0))
false_positive = sum((hasil_test_ulang['label'] == 1) & (imdb_dataset['label'] == 0))
print(f"True positive: {true_positive}")
print(f"True negative: {true_negative}")
print(f"False positive: {false_positive}")
print(f"False negative: {false_negative}")
accuracy = ((true_positive + true_negative) / len(imdb_dataset)) * 100
precision = (true_positive / (true_positive + false_positive)) * 100
recall = (true_positive / (true_positive + false_negative)) * 100
print(f"Accuracy = {accuracy:.2f}%")
print(f"Precision = {precision:.2f}%")
print(f"Recall = {recall:.2f}%")
print("DONE!")