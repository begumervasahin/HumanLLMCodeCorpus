import pandas as pd
import nltk
from sklearn.pipeline import Pipeline
from sklearn.externals import joblib
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.naive_bayes import MultinomialNB
from preprocessing import Preprocessing
def load_and_prepare_data(file_path):
    imdb_dataset = pd.read_csv(file_path, sep="\t", header=None, names=['text', 'label'])
    imdb_dataset["word_count"] = imdb_dataset["text"].apply(lambda x: len(str(x).split()))
    print("Dataset loaded successfully!")
    return imdb_dataset
def preprocess_data(imdb_dataset, preprocessor):
    imdb_dataset['text'] = imdb_dataset['text'].apply(preprocessor.processTweet)
    imdb_dataset = imdb_dataset.drop_duplicates('text')
    imdb_dataset['tokens'] = imdb_dataset['text'].apply(preprocessor.text_process)
    bow_transformer = CountVectorizer(analyzer=preprocessor.text_process).fit(imdb_dataset['text'])
    messages_bow = bow_transformer.transform(imdb_dataset['text'])
    print("Dataset cleaned!")
    return imdb_dataset, bow_transformer, messages_bow
def train_and_save_model(X_train, y_train, parameters, model_path="model.pkl"):
    pipeline = Pipeline([
        ('bow', CountVectorizer(strip_accents='ascii', stop_words='english', lowercase=True)),
        ('tfidf', TfidfTransformer()),
        ('classifier', MultinomialNB()),
    ])
    grid = GridSearchCV(pipeline, cv=10, param_grid=parameters, verbose=1)
    grid.fit(X_train, y_train)
    joblib.dump(grid, model_path)
    print(f"Model saved to {model_path}")
def load_model(model_path="model.pkl"):
    return joblib.load(model_path)
def evaluate_model(model, X_test, y_test):
    y_preds = model.predict(X_test)
    print(f'Accuracy from train/test split: {accuracy_score(y_test, y_preds) * 100:.2f}%')
    print('Confusion matrix:\n', confusion_matrix(y_test, y_preds))
    print(classification_report(y_test, y_preds))
def predict_and_save_results(model, imdb_dataset, result_path="test_ulang_dataset.csv"):
    text_ = []
    label_ = []
    for review in imdb_dataset['text']:
        prediction = model.predict([review])
        text_.append(review)
        label_.append(prediction[0])
    results = pd.DataFrame({'text': text_, 'label': label_})
    results.to_csv(result_path, index=False, encoding='utf-8')
    print(f"Results saved to {result_path}")
def calculate_metrics(results, imdb_dataset):
    true_positive = false_negative = true_negative = false_positive = 0
    for i, predicted_label in enumerate(results['label']):
        actual_label = imdb_dataset['label'][i]
        if actual_label == 1:
            if predicted_label == 1:
                true_positive += 1
            else:
                false_negative += 1
        else:
            if predicted_label == 0:
                true_negative += 1
            else:
                false_positive += 1
    accuracy = ((true_positive + true_negative) / len(imdb_dataset)) * 100
    precision = (true_positive / (true_positive + false_positive)) * 100
    recall = (true_positive / (true_positive + false_negative)) * 100
    print(f"True positive: {true_positive}")
    print(f"True negative: {true_negative}")
    print(f"False positive: {false_positive}")
    print(f"False negative: {false_negative}")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Precision: {precision:.2f}%")
    print(f"Recall: {recall:.2f}%")
def main():
    nltk.download('stopwords')
    imdb_dataset = load_and_prepare_data("imdb_labelled.txt")
    preprocessor = Preprocessing()
    imdb_dataset, bow_transformer, messages_bow = preprocess_data(imdb_dataset, preprocessor)
    print("\nStarting train/test split with 80% training and 20% testing")
    X_train, X_test, y_train, y_test = train_test_split(imdb_dataset['text'], imdb_dataset['label'], test_size=0.2, random_state=42)
    parameters = {
        'bow__ngram_range': [(1, 1), (1, 2)],
        'tfidf__use_idf': (True, False),
        'classifier__alpha': (1e-2, 1e-3),
    }
    train_and_save_model(X_train, y_train, parameters)
    model_NB = load_model()
    evaluate_model(model_NB, X_test, y_test)
    predict_and_save_results(model_NB, imdb_dataset)
    results = pd.read_csv("test_ulang_dataset.csv")
    calculate_metrics(results, imdb_dataset)
    print("DONE!")
if __name__ == "__main__":
    main()