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
    pred_prob = regress(X, theta)
    return np.where(pred_prob > 0.5, 1, 0)
def regress(X, theta):
    return sigmoid(np.dot(X, theta[1].T) + theta[0])
def bernoulli_log_likelihood(p, y):
    return -y * np.log(p) - (1 - y) * np.log(1 - p)
def compute_cost(X, y, theta, beta):
    f = regress(X, theta)
    log_likelihood = bernoulli_log_likelihood(f, y)
    cost = np.sum(log_likelihood)
    theta_squares = np.sum(np.square(theta[1]))
    return (0.5 / len(X)) * (cost + beta * theta_squares)
def compute_grad(X, y, theta, beta):
    reg_error = regress(X, theta) - y
    dL_dw = np.dot(reg_error.T, X) + beta * theta[1]
    dL_db = np.sum(reg_error)
    return dL_db / len(X), dL_dw / len(X)
def preprocess_data(data, degree):
    x1 = data['Test 1']
    x2 = data['Test 2']
    for i in range(1, degree + 1):
        for j in range(i + 1):
            data[f'F{i}{j}'] = np.power(x1, i - j) * np.power(x2, j)
    data.drop(['Test 1', 'Test 2'], axis=1, inplace=True)
    return data
data_path = os.path.join(os.getcwd(), 'data', 'DecisionBoundaryData.dat')
data = pd.read_csv(data_path, header=None, names=['Test 1', 'Test 2', 'Accepted'])
data = preprocess_data(data, degree)
X = data.iloc[:, 1:].values
y = data.iloc[:, 0:1].values
w = np.zeros((1, X.shape[1]))
b = np.array([0])
theta = (b, w)
for epoch in range(n_epoch):
    dL_db, dL_dw = compute_grad(X, y, theta, beta)
    b -= alpha * dL_db
    w -= alpha * dL_dw
    theta = (b, w)
    if epoch % 1000 == 0:
        cost = compute_cost(X, y, theta, beta)
        print(f"Epoch {epoch}, Cost: {cost}")
predictions = predict(X, theta)
accuracy = np.mean(predictions == y) * 100
print(f'Accuracy: {accuracy}%')
xx, yy = np.mgrid[-1.2:1.2:.01, -1.2:1.2:.01]
grid = np.c_[xx.ravel(), yy.ravel()]
grid_nl = np.array([np.power(xx.ravel(), i - j) * np.power(yy.ravel(), j) for i in range(1, degree + 1) for j in range(i + 1)]).T
probs = regress(grid_nl, theta).reshape(xx.shape)
fig, ax = plt.subplots(figsize=(8, 6))
ax.contour(xx, yy, probs, levels=[0.5], cmap="Greys", vmin=0, vmax=0.6)
ax.scatter(data['F10'], data['F01'], c=y.ravel(), s=50, cmap="RdBu", vmin=-0.2, vmax=1.2, edgecolor="white", linewidth=1)
ax.set(aspect="equal", xlim=(-1.5, 1.5), ylim=(-1.5, 1.5), xlabel="$X_1$", ylabel="$X_2$")
plt.show()