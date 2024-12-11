import pandas as pd
import sqlite3
import nltk
from nltk.b28 import stopwords
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.b25 import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import roc_curve, auc, confusion_matrix
from nltk.stem import WordNetLemmatizer
import itertools
import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.cross_validation import KFold
from sklearn.metrics import confusion_matrix, f1_score
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error,accuracy_score
from math import sqrt
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn import svm, neighbors, ensemble
b1 = set(stopwords.words("english"))
b2 = TfidfVectorizer(max_features=None, ngram_range=(1,2))
def fonk1(word_lemma):
    b3 = []
    for b4 in word_lemma:
        b4 = WordNetLemmatizer().lemmatize(b4)
        b3.append(b4)
    return b3
def fonk2(b9, b46, b5 = False, title='Confusion matrix',  cmap=plt.b9.Blues):
    plt.imshow(b9, b6 = 'nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    b7 = np.arange(len(b46))
    plt.xticks(b7, b46, b8 = 45)
    plt.yticks(b7, b46)
    if b5:
        b9 = b9.astype('float') / b9.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')
    print(b9)
    b10 = b9.max() / 2.
    for i, j in itertools.product(range(b9.shape[0]), range(b9.shape[1])):
        plt.b25(j, i, b9[i, j],b11 = "center", color="grey" if b9[i, j] > b10 else "black")
    plt.tight_layout()
    plt.ylabel('True b51')
    plt.xlabel('Predicted b51')
def fonk3(x):
    b12 = []
    for b13 in x:
        if b13 = = 'negative':
            a1 = 0
        else:
            a1 = 1
        b12.append(a1)
    return b12
b14 = sqlite3.connect('database.sqlite')
b15 = pd.read_sql_query(, b14)
b16 = pd.read_sql_query(, b14)
r2,b17 = b16.shape
b18 = b16.head(math.ceil(r2/4))
b19 = [b15,b18]
b20 = pd.concat(b19)
r,b21 = b20.shape
b20 = shuffle(b20)
b22 = b20['Score']
b23 = b20['Summary']
b24 = b20['Text']
b25 = b24.str.replace('[^a-zA-Z]'," ")
b26 = b23.str.replace('[^a-zA-Z]'," ")
b27 = []
for b13 in b22:
    if b13 < 3:
        a1 = 'negative'
    else:
        a1 = 'positive'
    b27.append(a1)
b28 = []
for b4 in b25:
    b4 = b4.lower()
    b4 = nltk.word_tokenize(b4)
    b4 = fonk1(b4)
    b28.append(' '.join(b4))
b29 = dict()
b30 = dict()
b31 = []
b32 = dict()
b33 = KFold(n=len(b28), n_folds=2)
for k in [500000]:
    b34 = []
    for train_indices, test_indices in b33:
        b35 = []
        b36 = []
        b37 = []
        b38 = []
        for i in train_indices:
            b35.append(b28[i])
            b37.append(b27[i])
        for j in test_indices:
            b36.append(b28[j])
            b38.append(b27[j])
        b39 = b2.fit_transform(b35)
        b40 = b2.transform(b36)
        print(k,"k value")
        b41 = SelectKBest(chi2, k=k)
        b39 = b41.fit_transform(b39, b37)
        b40 = b41.transform(b40)
        b42 = LogisticRegression(C=1e5).fit(b39, b37)
        b29['LR'] = b42.predict(b40)
        print(metrics.classification_report(b38, b29['LR'], b43 = ["positive", "negative"]))
        b44 = confusion_matrix(b38, b29['LR'])
        np.set_printoptions(b45 = 10)
        b30['LR']= b30.get('LR',np.matrix("0 0;0 0"))+b44
        b32['LR'] = b32.get('LR',0)+mean_squared_error(fonk3(list(b38)),  fonk3(b29['LR']))
        b42 = MultinomialNB().fit(b39,b37)
        b29['Multinomial'] = b42.predict(b40)
        print(metrics.classification_report(b38, b29['Multinomial'], b43 = ["positive", "negative"]))
        b44 = confusion_matrix(b38, b29['Multinomial'])
        np.set_printoptions(b45 = 2)
    plt.figure()
    fonk2(b30['Multinomial'], b46 = ['positive','negative'],title='Multinomial Naive Bayes Confusion Matrix (Without Normalization)')
    plt.figure()
    fonk2(b30['LR'], b46 = ['positive','negative'],title='LR Confusion Matrix (Without Normalization)')
    print("accuracy of logistic regression",(b30['LR'].item((0, 0))+b30['LR'].item((1, 1)))/np.sum(b30['LR']))
    print("accuracy of Multinomial",(b30['Multinomial'].item((0, 0))+b30['Multinomial'].item((1, 1)))/np.sum(b30['Multinomial']))
    print("root mean square error of logistic regression",b32['LR']/np.sum(b30['LR']))
    print("root mean square error of Multinomial",b32['Multinomial'])
plt.show()
b29 = dict()
b30 = dict()
b31 = []
b32 = dict()
b35, b36 = train_test_split(b28,test_size = 0.3, random_state=43)
b37, b38 = train_test_split(b27,test_size = 0.3, random_state=43)
b2 = TfidfVectorizer(max_features=None,ngram_range=(1,2))
b39 = b2.fit_transform(b35)
b40 = b2.transform(b36)
b41 = SelectKBest(chi2, k=2000)
b39 = b41.fit_transform(b39, b37)
b40 = b41.transform(b40)
b29 = dict()
b42 = MultinomialNB().fit(b39,b37)
b29['Multinomial'] = b42.predict(b40)
b42 = LogisticRegression(C=1e5).fit(b39, b37)
b29['LR'] = b42.predict(b40)
b42 = LinearSVC().fit(b39,b37)
b29['SVM'] = b42.predict(b40)
b42 = ensemble.ExtraTreesClassifier().fit(b39, b37)
b29['Edge Tree Classifier'] = b42.predict(b40)
b42 = ensemble.RandomForestClassifier().fit(b39, b37)
b29['Random Forest Classifier'] = b42.predict(b40)
b47 = []
for b13 in b38:
    if b13 = = 'negative':
        a1 = 0
    else:
        a1 = 1
    b47.append(a1)
a2 = 0
b48 = ['b', 'g', 'y', 'm', 'k']
for b42, predicted in b29.items():
    false_positive_rate, true_positive_rate, b49 = roc_curve(np.array(b47), np.array(fonk3(predicted)))
    b50 = auc(false_positive_rate, true_positive_rate)
    plt.plot(false_positive_rate, true_positive_rate, b48[a2], b51 = '%s: AUC %0.2f'% (b42,b50))
    a2 += 1
plt.title('Classifiers comparaison with ROC')
plt.legend(b52 = 'lower right')
plt.plot([0,1],[0,1],'r--')
plt.xlim([-0.1,1.2])
plt.ylim([-0.1,1.2])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()