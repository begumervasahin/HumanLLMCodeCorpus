
import pandas as pd
from sklearn.externals import joblib
rf = joblib.load('Random_Forest.pkl')
mlp = joblib.load('Neural_Network.pkl')
X_test = pd.read_csv("Test_Data_Table.csv")
y_test = X_test.label
X_test = X_test.drop(X_test.columns[0], axis=1)
X_test = X_test.drop(labels=['label'], axis=1)
X_train = pd.read_csv("Data_Table_Preprocessed.csv")
X_train = X_train.drop(X_train.columns[0], axis=1)
X_final_test = pd.DataFrame()
print len(X_train.columns)
for i in X_train.columns:
    X_final_test[i] = X_test[i]
correct = 0
no_predict = 0
incorrect = 0
for i in range(10000):
    X = pd.DataFrame(columns=X_final_test.columns)
    X.loc[0] = X_final_test.loc[i]
    y = y_test.loc[i]
    op1 = mlp.predict(X)
    op2 = rf.predict(X)
    if op1==op2 and op1==y:
        correct += 1
    elif op1!=op2:
        no_predict += 1
    elif op1==op2 and op1!=y:
        incorrect += 1
    print "Correct score - ", correct
    print "No Predictions - ", no_predict
    print "Wrong score - ", incorrect