
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
my_data =pd.read_csv('CMP3751M_ML_Assignment 1_Task1 - dataset - pol_regression.csv')
x = my_data['x'].values
y = my_data['y'].values
def getPolynomialDataMatrix(x, degree):
    X = np.ones(x.shape)
    for i in range(1, degree + 1):
        X = np.column_stack((X, x ** i))
    return X
def pol_regression(features_train,y_train,degree):
    X = getPolynomialDataMatrix(features_train, degree)
    XX = X.transpose().dot(X)
    w = np.linalg.solve(XX, X.transpose().dot(y_train))
    return w
def train_test_split(X,Y,train_split):
    X_train = []
    X_test = []
    Y_train = []
    Y_test = []
    for position in range(len(X)):
        if position >= len(X)*train_split:
            X_test.append(X[position])
            Y_test.append(Y[position])
        else:
            X_train.append(X[position])
            Y_train.append(Y[position])
    return X_train, X_test, Y_train, Y_test
def eval_pol_regression(x, y, degree):
    X_train, X_test, Y_train, Y_test = train_test_split(x,y,0.7)
    RMSEtrain = np.zeros((degree, 1))
    RMSEtest = np.zeros((degree,1))
    for i in range(1, degree +1):
        Xtrain = getPolynomialDataMatrix(np.asarray(X_train), i)
        Xtest = getPolynomialDataMatrix(np.asarray(X_test), i)
        param = pol_regression(np.asarray(X_train),np.asarray(Y_train), i)
        RMSEtrain[i - 1] = np.sqrt((Xtrain.dot(param) - np.asarray(Y_train))**2).mean()
        RMSEtest[i - 1] = np.sqrt((Xtest.dot(param) - np.asarray(Y_test))**2).mean()
    plt.figure();
    plt.title(str(degree) + ' Degree')
    plt.semilogy(range(1,len(RMSEtrain) + 1), RMSEtrain)
    plt.semilogy(range(1,len(RMSEtest) + 1), RMSEtest)
    return RMSEtrain, RMSEtest
def plotGraph(x,x_test,y,weight, color):
    if weight == 0:
        w1 = np.mean(y)
    else:
        w1 = pol_regression(x,y,weight)
    Xtest1 =getPolynomialDataMatrix(x_test, weight)
    ytest1 = Xtest1.dot(w1)
    plt.figure()
    plt.plot(x,y, 'bo')
    plt.plot(x_test, ytest1,color=color)
    plt.title(str(weight) + ' Degrees')
    plt.xlabel("Range of Polynomials")
    plt.ylabel("Points of Polynomial")
    plt.ylabel("Points of Polynomial")
    plt.show()
def plotEval(x,y,degree):
    RMSEtrain, RMSEtest = eval_pol_regression(x,y,degree)
    plt.figure();
    plt.semilogy(range(1,len(RMSEtrain) + 1), RMSEtrain)
    plt.semilogy(range(1,len(RMSEtest) + 1), RMSEtest)
    plt.title((str(degree) + ' Degrees'))
    plt.xlabel("Degree of RMSE")
    plt.ylabel("Points of RSME")
    plt.legend(('RMSE on training set', 'RMSE on test set'))
    plt.show()
x_test = np.linspace(-5,5,len(x))
y_test = np.linspace(-5,5,len(x))
for i in range(0,4):
    plotGraph(x,x_test,y,i, 'r')
plotGraph(x,x_test,y,5, 'r')
plotGraph(x,x_test,y,10, 'r')
for i in range(0,4):
    eval_pol_regression(x,y, i)
eval_pol_regression(x,y,5)
eval_pol_regression(x,y,10)