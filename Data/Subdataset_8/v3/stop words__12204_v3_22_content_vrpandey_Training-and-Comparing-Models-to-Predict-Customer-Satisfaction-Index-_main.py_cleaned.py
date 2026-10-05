import pandas as pd
import sqlite3
import nltk
import numpy as np
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()
def lemmatize_words(word_list):
    return [lemmatizer.lemmatize(word) for word in word_list]
def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix', cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')
    print(cm)
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j], horizontalalignment="center", color="grey" if cm[i, j] > thresh else "black")
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
connection = sqlite3.connect('database.sqlite')
reviews_below_3 = pd.read_sql_query(, connection)
reviews_above_3 = pd.read_sql_query(, connection)
total_rows, _ = reviews_above_3.shape
reviews_above_3_subset = reviews_above_3.head(math.ceil(total_rows/4))
combined_data = [reviews_below_3, reviews_above_3_subset]
reviews_dataset = pd.concat(combined_data).sample(frac=1).reset_index(drop=True)
scores = reviews_dataset['Score']
sentiment_labels = ['negative' if score < 3 else 'positive' for score in scores]
corpus = []
for text in reviews_dataset['Text']:
    text = text.lower()
    text = word_tokenize(text)
    text = lemmatize_words(text)
    text = ' '.join(text)
    corpus.append(text)
X_train, X_test, y_train, y_test = train_test_split(corpus, sentiment_labels, test_size=0.3, random_state=43)
vectorizer = TfidfVectorizer(max_features=None, ngram_range=(1, 2))
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)
ch2 = SelectKBest(chi2, k=2000)
X_train_tfidf = ch2.fit_transform(X_train_tfidf, y_train)
X_test_tfidf = ch2.transform(X_test_tfidf)
models = {
    'MultinomialNB': MultinomialNB(),
    'LogisticRegression': LogisticRegression(C=1e5),
    'LinearSVC': LinearSVC(),
    'ExtraTreesClassifier': ExtraTreesClassifier(),
    'RandomForestClassifier': RandomForestClassifier()
}
predictions = {}
for model_name, model in models.items():
    model.fit(X_train_tfidf, y_train)
    predictions[model_name] = model.predict(X_test_tfidf)
    print("Classification Report for", model_name)
    print(classification_report(y_test, predictions[model_name], target_names=['negative', 'positive']))
    cnf_matrix = confusion_matrix(y_test, predictions[model_name])
    plt.figure()
    plot_confusion_matrix(cnf_matrix, classes=['negative', 'positive'], title=model_name + ' Confusion Matrix')
plt.figure()
cmp = 0
colors = ['b', 'g', 'y', 'm', 'k']
for model_name, predicted in predictions.items():
    false_positive_rate, true_positive_rate, thresholds = roc_curve(np.array(y_test_mapping), np.array(format(predicted)))
    roc_auc = auc(false_positive_rate, true_positive_rate)
    plt.plot(false_positive_rate, true_positive_rate, colors[cmp], label='%s: AUC %0.2f' % (model_name, roc_auc))
    cmp += 1
plt.title('Classifiers Comparison with ROC')
plt.legend(loc='lower right')
plt.plot([0, 1], [0, 1], 'r--')
plt.xlim([-0.1, 1.2])
plt.ylim([-0.1, 1.2])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()