import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.optimizers import SGD
import data
learning_rate = 0.3
training_epochs = 20000
display_step = 500
degree = 4
_, Y = data.get_data("BCHAIN/MKPRU", 365)
_, X = data.get_data("BCHAIN/BLCHS", 365)
m = Y.shape[0]
def prepare_training_data(X, degree):
    train_X = np.zeros((m, degree))
    for i in range(degree):
        X_temp = np.power(X, i + 1)
        train_X[:, i] = (X_temp - np.mean(X_temp)) / np.std(X_temp, axis=0)
    return train_X
train_X = prepare_training_data(X, degree)
Y = Y.reshape(-1, 1)
theta = tf.Variable(tf.random.uniform([degree, 1], -1.0, 1.0, dtype=tf.float64), name="theta")
bias = tf.Variable(tf.random.uniform([1], -1.0, 1.0, dtype=tf.float64), name="bias")
def hypothesis(X):
    return tf.matmul(X, theta) + bias
def cost_fn():
    return tf.reduce_mean(tf.square(hypothesis(train_X) - Y)) / (2 * m)
optimizer = SGD(learning_rate=learning_rate)
def train_model(epochs, display_step):
    for epoch in range(epochs):
        with tf.GradientTape() as tape:
            cost = cost_fn()
        grads = tape.gradient(cost, [theta, bias])
        optimizer.apply_gradients(zip(grads, [theta, bias]))
        if (epoch + 1) % display_step == 0:
            print(f"Epoch: {epoch + 1:04d}, cost={cost.numpy():.9f}, theta={theta.numpy().T}, bias={bias.numpy()}")
train_model(training_epochs, display_step)
training_cost = cost_fn().numpy()
print(f"Training cost={training_cost}, theta={theta.numpy().T}, bias={bias.numpy()}\n")
plt.plot(X, Y, 'r', label='Market Price (training)')
plt.plot(X, hypothesis(train_X).numpy(), label='Polynomial Regression Line')
plt.title("Bitcoin Price Prediction: Training Polynomial Regression")
plt.xlabel("BlockChain Size")
plt.ylabel("Price ($)")
plt.legend()
plt.show()
def test_hypothesis(test_values, X, degree):
    test_X_scaled = (test_values - np.mean(X)) / np.std(X, axis=0)
    for test_value in test_X_scaled:
        test_polynomial = np.array([test_value ** i for i in range(1, degree + 1)])
        prediction = np.dot(test_polynomial, theta.numpy().flatten()) + bias.numpy()
        original_value = test_value * np.std(X, axis=0) + np.mean(X)
        print(f"Given Blockchain Size = {original_value} -> Hypothesis = {prediction}")
test_X = np.array([100000, 150000])
test_hypothesis(test_X, X, degree)