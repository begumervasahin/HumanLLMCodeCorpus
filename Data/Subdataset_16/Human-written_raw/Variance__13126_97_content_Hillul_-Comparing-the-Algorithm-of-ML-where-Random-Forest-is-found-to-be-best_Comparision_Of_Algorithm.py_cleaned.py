
import pandas
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
b1 = "https:
b2 = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
b3 = pandas.read_csv(b1, b2=b2)
b4 = b3.values
b5 = b4[:,0:8]
b6 = b4[:,8]
a1 = 7
b7 = []
b7.append(('LR', LogisticRegression()))
b7.append(('LDA', LinearDiscriminantAnalysis()))
b7.append(('KNN', KNeighborsClassifier()))
b7.append(('CART', DecisionTreeClassifier()))
b7.append(('NB', GaussianNB()))
b7.append(('SVM', SVC()))
b8 = []
b2 = []
b9 = 'accuracy'
for name, model in b7:
	b10 = model_selection.KFold(n_splits=10, random_state=a1)
	b11 = model_selection.cross_val_score(model, b5, b6, cv=b10, b9=b9)
	b8.append(b11)
	b2.append(name)
	b12 = "%s: %f (%f)" % (name, b11.mean(), b11.std())
	print(b12)
b13 = plt.figure()
b13.suptitle('Algorithm Comparison')
b14 = b13.add_subplot(111)
plt.boxplot(b8)
b14.set_xticklabels(b2)
plt.show()