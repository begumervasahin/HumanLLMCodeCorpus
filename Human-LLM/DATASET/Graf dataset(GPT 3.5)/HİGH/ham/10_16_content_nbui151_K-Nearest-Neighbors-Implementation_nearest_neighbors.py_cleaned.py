
import numpy as np
import pandas as pd
import operator
from collections import defaultdict
def fonk1(b6, b4):
    b1 = np.inner(b6,b4)/(np.linalg.norm(b6)*np.linalg.norm(b4))
    return b1
'''
Function to find nearest neighbors and b3 the label of Y
train is a numpy ndarray containing the covariates of the training data
test is a numpy ndarray containing the covaraites of the test data
Y_train isa numpy array containing the labels of the training data
b2 is the number of neighbors we want to include in determining the lable of the test data
'''
def fonk2(train, test, Y_train, b2 = 5):
    b3 = []
    for m in range(test.shape[0]):
        b4 = test[m]
        b5 = {}
        for i in range(train.shape[0]):
            b6 = train[i]
            b7 = fonk1(b6, b4)
            b5[i] = b7
        b8 = sorted(b5.items(), key=operator.itemgetter(1), reverse=True)
        b9 = []
        for i in range(b2):
            if b2 < len(b8):
                b9.append(b8[i][0])
        b10 = []
        for item in b9:
            b10.append(Y_train[item])
        b11 = defaultdict(int)
        for i in b10:
            b11[i] += 1
        b12 = sorted(b11.items(), key=operator.itemgetter(1), reverse=True)
        b13 = b12[0][0]
        b3.append(b13)
    return b3
'''
We then test the algorithm on the iris dataset, we shuffle
the iris dataset, split the data into 120 training and 30 test items,
and calculate the accuracy level. We do this 20 times over and calculate
the average accuracy level for those 20 trials
'''
from sklearn import datasets
b14 = datasets.load_iris()
b15 = pd.DataFrame(b14.data)
b15['target'] = b14.target
b16 = []
for i in range(20):
    b17 = b15.sample(frac=1).reset_index(drop=True)
    b18 = np.array(b17.target)
    b19 = np.array(b17.drop('target', axis = 1))
    b20 = b19[0:120]
    b21 = b18[0:120]
    b22 = b19[120:151]
    b23 = b18[120:151]
    b24 = fonk2(b20, b22, b21, b2 = 5)
    b25 = np.mean(b24 == b23) *100
    b16.append(b25)
print("Average accuracy for iris dataset is ", np.mean(b16))
'''
The average accuracy level that I got was about 97%
The Iris data is an easy test case since the data is closely clustered together
Let's test the algorithm on a harder case, predicting wine quality which takes
values of 3, 4, 5, 6, 7, 8 on a scale of 1 (fairly bad) to 10 (very good wine)
based on 11 different features. The data set comes of the UC Irvine Machine Learning
Data Archives. Again, we do this for 20 trials with reshuffled data.
Here the algorithm has a harder time, producing an accuracy level of around 54%.
However, if we allow for some fuzziness in the prediction, giving the algorithm a
score when the prediction is +-1 of the true value, we get an accuracy level of around 91%.
'''
b26 = pd.read_csv("redwinequality.csv")
b27 = []
b28 = []
for i in range(20):
    b29 = b26.sample(frac=1).reset_index(drop=True)
    b30 = np.array(b29.quality)
    b31 = np.array(b29.drop('quality', axis = 1))
    b32 = b31[0:1500]
    b33 = b30[0:1500]
    b34 = b31[1500:1600]
    b35 = b30[1500:1600]
    b36 = fonk2(b32, b34, b33, b2 = 5)
    b37 = np.mean(b36==b35) * 100
    b27.append(b37)
    b38 = np.mean(abs(b36-b35)<2) * 100
    b28.append(b38)
print("Average strict accuracy for red wine dataset is ", np.mean(b27))
print("Average fuzzy accuracy for red wine dataset is ", np.mean(b28))