import pandas as pd
import sqlite3
import nltk
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split, KFold
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc, mean_squared_error
from sklearn.utils import shuffle
import numpy as np
import matplotlib.pyplot as plt
import math
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
stops = set(stopwords.words("english"))
lemmatizer = nltk.WordNetLemmatizer()
def word_lemmatize(word_lemma):
    input_lemma = []
    for word in word_lemma:
        word = lemmatizer.lemmatize(word)
        input_lemma.append(word)
    return input_lemma
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
        plt.text(j, i, cm[i, j],horizontalalignment="center", color="grey" if cm[i, j] > thresh else "black")
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
connection = sqlite3.connect('database.sqlite')
dataset1 = pd.read_sql_query(, connection)
dataset2 = pd.read_sql_query(, connection)
r2, c2 = dataset2.shape
dataset3 = dataset2.head(math.ceil(r2/4))
data = [dataset1, dataset3]
dataset = pd.concat(data)
dataset = shuffle(dataset)
score_data = dataset['Score']
summary_data = dataset['Summary']
text_data = dataset['Text']
result = ['negative' if score < 3 else 'positive' for score in score_data]
corpus = []
for text in text_data:
    text = text.lower()
    text = nltk.word_tokenize(text)
    text = word_lemmatize(text)
    text = ' '.join(text)
    corpus.append(text)
x_train, x_test, y_train, y_test = train_test_split(corpus, result, test_size=0.3, random_state=43)
vectorizer = TfidfVectorizer(max_features=None, ngram_range=(1, 2))
X_train_tfidf = vectorizer.fit_transform(x_train)
X_test_tfidf = vectorizer.transform(x_test)
ch2 = SelectKBest(chi2, k=2000)
X_train_tfidf = ch2.fit_transform(X_train_tfidf, y_train)
X_test_tfidf = ch2.transform(X_test_tfidf)
models = {
    'MultinomialNB': MultinomialNB(),
    'LogisticRegression': LogisticRegression(C=1e5),
    'LinearSVC': LinearSVC(),
    'ExtraTreesClassifier': ensemble.ExtraTreesClassifier(),
    'RandomForestClassifier': ensemble.RandomForestClassifier()
}
prediction = {}
for model_name, model in models.items():
    model.fit(X_train_tfidf, y_train)
    prediction[model_name] = model.predict(X_test_tfidf)
    print("Classification Report for", model_name)
    print(classification_report(y_test, prediction[model_name], target_names=['negative', 'positive']))
    cnf_matrix = confusion_matrix(y_test, prediction[model_name])
    plt.figure()
    plot_confusion_matrix(cnf_matrix, classes=['negative', 'positive'], title=model_name + ' Confusion Matrix')
plt.figure()
cmp = 0
colors = ['b', 'g', 'y', 'm', 'k']
for model_name, predicted in prediction.items():
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