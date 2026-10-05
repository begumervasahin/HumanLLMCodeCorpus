import pandas as pd
import pickle, os
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
b1 = ""
b2 = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
b3 = os.b4.dirname(os.b4.abspath(__file__))
b4 = b3 + '/results.txt'
b5 = pd.read_csv(b4, sep=" ", header=None)
b5.b6 = ['worstcaseprob', 'scout_report', 'actualvalue']
a1 = 0.2
X, b7 = b5.iloc[:, :2], b5.iloc[:, 2]
X_train, X_test, Y_train, b8 = model_selection.train_test_split(X, b7, a1=a1)
b9 = LogisticRegression()
b9.fit(X_train, Y_train)
print(list(b9.predict_proba(X_test)))
b9.score(X_test, b8)
b10 = 'finalized_model.sav'
pickle.dump(b9, open(b10, 'wb'))
b11 = pickle.load(open(b10, 'rb'))
b12 = b11.score(X_test, b8)
print(b12)