import pandas as pd
from sklearn.pipeline import Pipeline
from preprocessing import Preprocessing
from sklearn.externals import joblib
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.naive_bayes import MultinomialNB
imdb_dataset = pd.read_csv("imdb_labelled.txt", sep="\t", header=None)
imdb_dataset.columns = ['text', 'label']
positives = imdb_dataset['label'][imdb_dataset.label == 1]
negatives = imdb_dataset['label'][imdb_dataset.label == 0]
COLNAMES = ["id", "text"]
nltk.download('stopwords')
def word_count(text):
    return len(str(text).split())
imdb_dataset["word_count"] = imdb_dataset["text"].apply(word_count)
print("Dataset loaded successfully!")
all_words = []
for line in list(imdb_dataset['text']):
    words = line.split()
    for word in words:
        all_words.append(word.lower())
dataset = imdb_dataset
dataset.to_pickle("dataset.p")
dataset_pickle = pd.read_pickle("dataset.p")
dataset_pickle['text'] = dataset_pickle['text'].apply(Preprocessing().processTweet)
dataset_pickle = dataset_pickle.drop_duplicates('text')
print(dataset_pickle.shape)
eng_stop_words = stopwords.words('english')
dataset_pickle['tokens'] = dataset_pickle['text'].apply(Preprocessing().text_process)
bow_transformer = CountVectorizer(analyzer=Preprocessing().text_process).fit(dataset_pickle['text'])
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
    'classifier__alpha': (1e-2, 1e-3)
}
grid = GridSearchCV(pipeline, cv=10, param_grid=parameters, verbose=1)
grid.fit(X_train, y_train)
means = grid.cv_results_['mean_test_score']
stds = grid.cv_results_['std_test_score']
params = grid.cv_results_['params']
for mean, std, param in zip(means, stds, params):
    print(f"{mean:.3f} (+/-{std:.3f}) for {param}")
joblib.dump(grid, "model.pkl")
model_NB = joblib.load("model.pkl")
y_preds = model_NB.predict(X_test)
print(f"Accuracy from train/test split: {accuracy_score(y_test, y_preds) * 100:.2f}%")
print('Confusion matrix:\n', confusion_matrix(y_test, y_preds))
print(classification_report(y_test, y_preds))
def label_to_str(x):
    return 'Positive' if x == 1 else 'Negative'
text_ = [0] * len(imdb_dataset)
label_ = [0] * len(imdb_dataset)
for idx, review in enumerate(imdb_dataset['text']):
    predict = model_NB.predict([review])
    text_[idx] = review
    label_[idx] = predict[0]
output_df = pd.DataFrame({"text": text_, "label": label_})
output_df.to_csv('test_ulang_dataset.csv', index=False, encoding='utf-8')
hasil_test_ulang = pd.read_csv("test_ulang_dataset.csv")
hasil_test_ulang.columns = ['text', 'label']
true_positive, false_negative, true_negative, false_positive = 0, 0, 0, 0
for i, predicted_label in enumerate(hasil_test_ulang['label']):
    if imdb_dataset['label'][i] == 1:
        if predicted_label == 1:
            true_positive += 1
        else:
            false_negative += 1
    if imdb_dataset['label'][i] == 0:
        if predicted_label == 0:
            true_negative += 1
        else:
            false_positive += 1
print(f"True positive: {true_positive}")
print(f"True negative: {true_negative}")
print(f"False positive: {false_positive}")
print(f"False negative: {false_negative}")
accuracy = ((true_positive + true_negative) / (true_positive + false_negative + false_positive + true_negative)) * 100
precision = (true_positive / (true_positive + false_positive)) * 100
recall = (true_positive / (true_positive + false_negative)) * 100
print(f"Accuracy = {accuracy:.2f}%")
print(f"Precision = {precision:.2f}%")
print(f"Recall = {recall:.2f}%")
print("DONE!")