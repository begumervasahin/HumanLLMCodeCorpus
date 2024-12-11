import pandas as pd
import sqlite3
import nltk
import itertools
import numpy as np
import matplotlib.pyplot as plt
import math
from nltk.b21 import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.b22 import TfidfVectorizer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
b1 = set(stopwords.words("english"))
b2 = WordNetLemmatizer()
def fonk1(word_lemma):
    b3 = []
    for word in word_lemma:
        b4 = b2.lemmatize(word)
        b3.append(b4)
    return b3
def fonk2(b9, b33, b5 = False, title='Confusion matrix', cmap=plt.b9.Blues):
    plt.imshow(b9, b6 = 'nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    b7 = np.arange(len(b33))
    plt.xticks(b7, b33, b8 = 45)
    plt.yticks(b7, b33)
    if b5:
        b9 = b9.astype('float') / b9.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')
    print(b9)
    b10 = b9.max() / 2.
    for i, j in itertools.product(range(b9.shape[0]), range(b9.shape[1])):
        plt.b22(j, i, b9[i, j],b11 = "center", color="grey" if b9[i, j] > b10 else "black")
    plt.tight_layout()
    plt.ylabel('True b37')
    plt.xlabel('Predicted b37')
b12 = sqlite3.connect('database.sqlite')
b13 = pd.read_sql_query(, b12)
b14 = pd.read_sql_query(, b12)
r2, b15 = b14.shape
b16 = b14.head(math.ceil(r2/4))
b17 = [b13, b16]
b18 = pd.concat(b17)
b18 = b18.sample(frac=1).reset_index(drop=True)
b19 = b18['Score']
b20 = ['negative' if score < 3 else 'positive' for score in b19]
b21 = []
for b22 in b18['Text']:
    b22 = b22.lower()
    b22 = word_tokenize(b22)
    b22 = fonk1(b22)
    b22 = ' '.join(b22)
    b21.append(b22)
x_train, x_test, y_train, b23 = train_test_split(b21, b20, test_size=0.3, random_state=43)
b24 = TfidfVectorizer(max_features=None, ngram_range=(1, 2))
b25 = b24.fit_transform(x_train)
b26 = b24.transform(x_test)
b27 = SelectKBest(chi2, k=2000)
b25 = b27.fit_transform(b25, y_train)
b26 = b27.transform(b26)
b28 = {
    'MultinomialNB': MultinomialNB(),
    'LogisticRegression': LogisticRegression(b29 = 1e5),
    'LinearSVC': LinearSVC(),
    'ExtraTreesClassifier': ExtraTreesClassifier(),
    'RandomForestClassifier': RandomForestClassifier()
}
b30 = {}
for model_name, model in b28.items():
    model.fit(b25, y_train)
    b30[model_name] = model.predict(b26)
    print("Classification Report for", model_name)
    print(classification_report(b23, b30[model_name], b31 = ['negative', 'positive']))
    b32 = confusion_matrix(b23, b30[model_name])
    plt.figure()
    fonk2(b32, b33 = ['negative', 'positive'], title=model_name + ' Confusion Matrix')
plt.figure()
a1 = 0
b34 = ['b', 'g', 'y', 'm', 'k']
for model_name, predicted in b30.items():
    false_positive_rate, true_positive_rate, b35 = roc_curve(np.array(y_test_mapping), np.array(format(predicted)))
    b36 = auc(false_positive_rate, true_positive_rate)
    plt.plot(false_positive_rate, true_positive_rate, b34[a1], b37 = '%s: AUC %0.2f' % (model_name, b36))
    a1 += 1
plt.title('Classifiers Comparison with ROC')
plt.legend(b38 = 'lower right')
plt.plot([0, 1], [0, 1], 'r--')
plt.xlim([-0.1, 1.2])
plt.ylim([-0.1, 1.2])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()