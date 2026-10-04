import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
def nfoldpolyfit(X, Y, maxK, n, verbose):
    setsize = len(X)
    polyfits = [[None for _ in range(maxK + 1)] for _ in range(n)]
    mean_squared_errors = [[0.0 for _ in range(maxK + 1)] for _ in range(n)]
    for nf in range(n):
        start, end = nf * setsize, (nf + 1) * setsize
        Xtrain = np.concatenate((X[:start], X[end:]))
        Ytrain = np.concatenate((Y[:start], Y[end:]))
        Xtest, Ytest = X[start:end], Y[start:end]
        for deg in range(maxK + 1):
            polyfits[nf][deg] = np.poly1d(np.polyfit(Xtrain, Ytrain, deg))
            square_error_sum = sum((Ytest[tr_ex] - polyfits[nf][deg](Xtest[tr_ex])) ** 2 for tr_ex in range(setsize))
            mean_squared_errors[nf][deg] = square_error_sum / float(setsize)
    if verbose:
        average_MSEs = np.mean(mean_squared_errors, axis=0)
        plt.figure(figsize=(15, 5))
        plt.subplot(121)
        plt.plot(range(maxK + 1), average_MSEs, '.-')
        plt.ylim(0, 0.5)
        plt.xlabel('Degree of Polynomial (k)')
        plt.ylabel('Average MSE')
        plt.title('Mean Squared Error vs. Degree of Polynomial')
        bestfit_index = np.argmin(average_MSEs)
        bestfit_function = np.polyfit(X, Y, bestfit_index)
        p = np.poly1d(bestfit_function)
        xp = np.linspace(np.min(X), np.max(X), 100)
        plt.subplot(122)
        plt.plot(X, Y, '.', xp, p(xp), '-')
        plt.ylim(np.min(Y), np.max(Y))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Best-Fitting Polynomial Regression')
        plt.show()
        return bestfit_function
def main():
    if len(sys.argv) != 5:
        print("Usage: python nfold_polyfit.py <path_to_csv_file> <maxK> <nFolds> <verbose>")
        sys.exit(1)
    rfile = sys.argv[1]
    maxK = int(sys.argv[2])
    nFolds = int(sys.argv[3])
    verbose = bool(int(sys.argv[4]))
    X, Y = [], []
    with open(rfile, 'r') as csvfile:
        dat = csv.reader(csvfile, delimiter=',')
        next(dat)
        for row in dat:
            X.append(float(row[0]))
            Y.append(float(row[1]))
    X = np.array(X)
    Y = np.array(Y)
    nfoldpolyfit(X, Y, maxK, nFolds, verbose)
if __name__ == "__main__":
    main()