import pandas as pd
import sqlite3
import nltk
from nltk.b26 import stopwords
from sklearn.model_selection import train_test_split, KFold
from sklearn.feature_extraction.b22 import TfidfVectorizer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc, mean_squared_error
from sklearn.utils import shuffle
import numpy as np
import matplotlib.pyplot as plt
import math
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
b1 = set(stopwords.words("english"))
b2 = TfidfVectorizer(max_features=None, ngram_range=(1, 2))
def fonk1(word_lemma):
    b3 = []
    for b4 in word_lemma:
        b4 = nltk.WordNetLemmatizer().lemmatize(b4)
        b3.append(b4)
    return b3
def fonk2(b9, b41, b5 = False, title='Confusion matrix', cmap=plt.b9.Blues):
    plt.imshow(b9, b6 = 'nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    b7 = np.arange(len(b41))
    plt.xticks(b7, b41, b8 = 45)
    plt.yticks(b7, b41)
    if b5:
        b9 = b9.astype('float') / b9.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')
    print(b9)
    b10 = b9.max() / 2.
    for i, j in itertools.product(range(b9.shape[0]), range(b9.shape[1])):
        plt.b22(j, i, b9[i, j], b11 = "center", color="grey" if b9[i, j] > b10 else "black")
    plt.tight_layout()
    plt.ylabel('True b46')
    plt.xlabel('Predicted b46')
b12 = sqlite3.connect('database.sqlite')
b13 = pd.read_sql_query(, b12)
b14 = pd.read_sql_query(, b12)
r2, b15 = b14.shape
b16 = b14.head(math.ceil(r2/4))
b17 = [b13, b16]
b18 = pd.concat(b17)
b18 = shuffle(b18)
b19 = b18['Score']
b20 = b18['Summary']
b21 = b18['Text']
b22 = b21.str.replace('[^a-zA-Z]'," ")
b23 = b20.str.replace('[^a-zA-Z]'," ")
b24 = []
for score in b19:
    if score < 3:
        b25 = 'negative'
    else:
        b25 = 'positive'
    b24.append(b25)
b26 = []
for b4 in b22:
    b4 = b4.lower()
    b4 = nltk.word_tokenize(b4)
    b4 = fonk1(b4)
    b26.append(' '.join(b4))
b27 = dict()
b28 = dict()
b29 = dict()
b30 = KFold(n=len(b26), n_folds=2)
for k in [500000]:
    for train_indices, test_indices in b30:
        b31 = [b26[i] for i in train_indices]
        b32 = [b24[i] for i in train_indices]
        b33 = [b26[j] for j in test_indices]
        b34 = [b24[j] for j in test_indices]
        b35 = b2.fit_transform(b31)
        b36 = b2.transform(b33)
        b37 = SelectKBest(chi2, k=k)
        b35 = b37.fit_transform(b35, b32)
        b36 = b37.transform(b36)
        b38 = LogisticRegression(C=1e5).fit(b35, b32)
        b27['LR'] = b38.predict(b36)
        print("Logistic Regression:")
        print(classification_report(b34, b27['LR'], b39 = ["positive", "negative"]))
        b38 = MultinomialNB().fit(b35, b32)
        b27['Multinomial'] = b38.predict(b36)
        print("Multinomial Naive Bayes:")
        print(classification_report(b34, b27['Multinomial'], b39 = ["positive", "negative"]))
        b40 = confusion_matrix(b34, b27['Multinomial'])
        b28['Multinomial'] = b28.get('Multinomial', np.zeros((2, 2))) + b40
        b29['LR'] = b29.get('LR', 0) + mean_squared_error(format(list(b34)), format(b27['LR']))
plt.figure()
fonk2(b28['Multinomial'], b41 = ['positive', 'negative'], title='Multinomial Naive Bayes Confusion Matrix (Without Normalization)')
plt.show()
print("Accuracy of Logistic Regression:", (b28['LR'].item((0, 0)) + b28['LR'].item((1, 1))) / np.sum(b28['LR']))
print("Root Mean Square Error of Logistic Regression:", b29['LR'] / np.sum(b28['LR']))
b31, b33, b32, b34 = train_test_split(b26, b24, test_size=0.3, random_state=43)
b2 = TfidfVectorizer(max_features=None, ngram_range=(1, 2))
b35 = b2.fit_transform(b31)
b36 = b2.transform(b33)
b37 = SelectKBest(chi2, k=2000)
b35 = b37.fit_transform(b35, b32)
b36 = b37.transform(b36)
b27 = dict()
b38 = MultinomialNB().fit(b35, b32)
b27['Multinomial'] = b38.predict(b36)
b38 = LogisticRegression(C=1e5).fit(b35, b32)
b27['LR'] = b38.predict(b36)
b38 = LinearSVC().fit(b35, b32)
b27['SVM'] = b38.predict(b36)
b38 = ensemble.ExtraTreesClassifier().fit(b35, b32)
b27['Extra Trees Classifier'] = b38.predict(b36)
b38 = ensemble.RandomForestClassifier().fit(b35, b32)
b27['Random Forest Classifier'] = b38.predict(b36)
b42 = [0 if score == 'negative' else 1 for score in b34]
a1 = 0
b43 = ['b', 'g', 'y', 'm', 'k']
for b38, predicted in b27.items():
    false_positive_rate, true_positive_rate, b44 = roc_curve(np.array(b42), np.array(format(predicted)))
    b45 = auc(false_positive_rate, true_positive_rate)
    plt.plot(false_positive_rate, true_positive_rate, b43[a1], b46 = '%s: AUC %0.2f'% (b38, b45))
    a1 += 1
plt.title('Classifiers Comparison with ROC')
plt.legend(b47 = 'lower right')
plt.plot([0,1],[0,1],'r--')
plt.xlim([-0.1,1.2])
plt.ylim([-0.1,1.2])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()