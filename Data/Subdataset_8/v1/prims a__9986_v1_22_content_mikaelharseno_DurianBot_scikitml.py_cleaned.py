import pandas as pd
import pickle
import os
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
basePath = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(basePath, 'results.txt')
df = pd.read_csv(path, sep=" ", header=None)
df.columns = ['worstcaseprob', 'scout_report', 'actualvalue']
X, Y = df.iloc[:, :2], df.iloc[:, 2]
test_size = 0.2
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size)
model = LogisticRegression()
model.fit(X_train, Y_train)
print(list(model.predict_proba(X_test)))
accuracy = model.score(X_test, Y_test)
print("Accuracy:", accuracy)
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))
loaded_model = pickle.load(open(filename, 'rb'))
loaded_model_accuracy = loaded_model.score(X_test, Y_test)
print("Loaded Model Accuracy:", loaded_model_accuracy)