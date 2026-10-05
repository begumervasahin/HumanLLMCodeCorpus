import pandas as pd
import pickle
import os
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
b1 = os.b2.dirname(os.b2.abspath(__file__))
b2 = os.b2.join(b1, 'results.txt')
b3 = pd.read_csv(b2, sep=" ", header=None)
b3.b4 = ['worstcaseprob', 'scout_report', 'actualvalue']
X, b5 = b3.iloc[:, :2], b3.iloc[:, 2]
a1 = 0.2
X_train, X_test, Y_train, b6 = model_selection.train_test_split(X, b5, a1=a1)
b7 = LogisticRegression()
b7.fit(X_train, Y_train)
print(list(b7.predict_proba(X_test)))
b8 = b7.score(X_test, b6)
print("Accuracy:", b8)
b9 = 'finalized_model.sav'
pickle.dump(b7, open(b9, 'wb'))
b10 = pickle.load(open(b9, 'rb'))
b11 = b10.score(X_test, b6)
print("Loaded Model Accuracy:", b11)