import numpy as np
import pandas as pd
from random import seed, normalvariate
seed(1234)
def rmse(Y, Ypred):
    return np.sqrt(np.mean((Y - Ypred) ** 2))
def r2Score(Y, Y_pred):
    mean_y = np.mean(Y)
    ss_tot = np.sum((Y - mean_y) ** 2)
    ss_res = np.sum((Y - Y_pred) ** 2)
    r2 = 1 - (ss_res / ss_tot)
    return r2
def costFunction(X, Y, W):
    N = len(Y)
    C = np.sum((X.dot(W) - Y) ** 2) / (2 * N)
    return C
def gradientDescent(X, Y, W, alpha, maxNumIterations=10000):
    N = len(Y)
    costHistory = []
    wHistory = []
    iteration = 0
    while iteration < maxNumIterations:
        h = X.dot(W)
        loss = h - Y
        gradient = X.T.dot(loss) / N
        W = W - alpha * gradient
        cost = costFunction(X, Y, W)
        costHistory.append(cost)
        iteration += 1
        wHistory.append(W)
    return W, costHistory, wHistory
def showResults(X, Y, W, newW, costHistory, maxNumIterations, wHistory):
    initial_cost = costFunction(X, Y, W)
    Y_pred = X.dot(newW)
    dash = '=' * 80
    print(dash)
    print("MULTI LINEAR REGRESSION USING GRADIENT DESCENT TERMINATION RESULTS")
    print(dash)
    print(f"Initial Weights:    {W[0]:>12.1f}, {W[1]:>2.1f}, {W[2]:>2.1f}.")
    print(f"Initial Cost:        {initial_cost:>12,.1f}")
    print()
    print(f"Final Weights:       w0:{newW[0]:>+0.2f}, w1:{newW[1]:>+3.2f}, w2:{newW[2]:>+3.3f}")
    print(f"Final Cost:         {costHistory[-1]:>+12.1f}")
    print(f"RMSE:              {rmse(Y, Y_pred):>+12.1f}, R-Squared: {r2Score(Y, Y_pred):>+12.1f}")
    print(dash)
def programBody(data, alpha, maxNumIterations):
    numXColumns = data.shape[1] - 1
    W = np.zeros(numXColumns + 1)
    x0 = np.ones(data.shape[0])
    X = np.column_stack((x0, data.iloc[:, 1:(numXColumns + 1)].values))
    Y = np.array(data.iloc[:, 0])
    newW, costHistory, wHistory = gradientDescent(X, Y, W, alpha, maxNumIterations)
    showResults(X, Y, W, newW, costHistory, maxNumIterations, wHistory)
def run():
    alpha = 0.0001
    maxNumIterations = 2500000
    numDataPoints = 500
    means = [70, 70]
    stds = [9, 9]
    corr = 0.8
    covs = [[stds[0] ** 2, stds[0] * stds[1] * corr], [stds[0] * stds[1] * corr, stds[1] ** 2]]
    data1 = np.random.multivariate_normal(means, covs, numDataPoints).T
    JobProbabilities = (data1[0] + data1[1]) / 2.5 + normalvariate(25, 4)
    data = np.vstack((JobProbabilities, data1)).T
    data = pd.DataFrame({"JobPotential": data[:, 0], "AI": data[:, 1], "MachineLearning": data[:, 2]})
    programBody(data, alpha, maxNumIterations)
    print("Finished")
if __name__ == '__main__':
    run()