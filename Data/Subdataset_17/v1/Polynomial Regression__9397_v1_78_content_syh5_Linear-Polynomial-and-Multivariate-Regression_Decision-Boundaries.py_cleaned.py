import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
trial_name = 'p6_reg0'
degree = 6
beta = 1
alpha = 0.01
n_epoch = 10000
eps = 0.0
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
def predict(X, theta):
    prediction = np.zeros([X.shape[0], 1])
    predict = regress(X, theta)
    for i in range(len(predict)):
        prediction[i] = 1 if predict[i] > 0.5 else 0
    return prediction
def regress(X, theta):
    return sigmoid(theta[0] + np.dot(X, np.transpose(theta[1])))
def bernoulli_log_likelihood(p, y):
    log_1 = np.log(p)
    log_2 = np.log(1 - p)
    G1 = np.multiply(-y, log_1)
    G2 = np.multiply(-(np.ones(y.shape) - y), log_2)
    return G1 + G2
def computeCost(X, y, theta, beta):
    f = regress(X, theta)
    G = bernoulli_log_likelihood(f, y)
    cost = np.sum(G)
    thetaSquares = np.sum(np.square(theta[1]))
    return (0.5 / len(X)) * (cost + beta * thetaSquares)
def computeGrad(X, y, theta, beta):
    regress_y = regress(X, theta) - y
    don = np.multiply(regress_y, X)
    dL_dw = np.sum(don, axis=0)
    dL_db = np.sum(regress_y)
    nabla = ((dL_db) / len(X), (dL_dw + beta * theta[1]) / len(X))
    return nabla
path = os.path.join(os.getcwd(), 'data', 'DecisionBoundaryData.dat')
data2 = pd.read_csv(path, header=None, names=['Test 1', 'Test 2', 'Accepted'])
x1 = data2['Test 1']
x2 = data2['Test 2']
for i in range(1, degree + 1):
    for j in range(0, i + 1):
        data2[f'F{i}{j}'] = np.power(x1, i - j) * np.power(x2, j)
data2.drop(['Test 1', 'Test 2'], axis=1, inplace=True)
cols = data2.shape[1]
X2 = data2.iloc[:, 1:cols].values
y2 = data2.iloc[:, 0:1].values
w = np.zeros((1, X2.shape[1]))
b = np.array([0])
theta = (b, w)
for i in range(n_epoch):
    dL_db, dL_dw = computeGrad(X2, y2, theta, beta)
    b = theta[0] - alpha * dL_db
    w = theta[1] - alpha * dL_dw
    L = computeCost(X2, y2, theta, beta)
    theta = (b, w)
    if i % 1000 == 0:
        print(f"Epoch {i}, Cost: {L}")
predictions = predict(X2, theta)
accuracy = np.mean(predictions == y2) * 100
print(f'Accuracy: {accuracy}%')
xx, yy = np.mgrid[-1.2:1.2:.01, -1.2:1.2:.01]
grid = np.c_[xx.ravel(), yy.ravel()]
grid_nl = np.array([np.power(xx.ravel(), i - j) * np.power(yy.ravel(), j) for i in range(1, degree + 1) for j in range(0, i + 1)]).T
probs = regress(grid_nl, theta).reshape(xx.shape)
f, ax = plt.subplots(figsize=(8, 6))
ax.contour(xx, yy, probs, levels=[0.5], cmap="Greys", vmin=0, vmax=0.6)
ax.scatter(data2['F10'], data2['F01'], c=y2, s=50, cmap="RdBu", vmin=-0.2, vmax=1.2, edgecolor="white", linewidth=1)
ax.set(aspect="equal", xlim=(-1.5, 1.5), ylim=(-1.5, 1.5), xlabel="$X_1$", ylabel="$X_2$")
plt.show()