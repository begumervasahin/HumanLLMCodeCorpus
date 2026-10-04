import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
def get_data(key, days):
    np.random.seed(42)
    X = np.linspace(1, days, days)
    Y = np.sin(X) + np.random.normal(0, 0.1, days)
    return X, Y
learning_rate = 0.3
training_epochs = 10000
display_step = 500
def prepare_data():
    X, Y = get_data("BCHAIN/MKPRU", 365)
    _, X1 = get_data("BCHAIN/BLCHS", 365)
    train_X = (X - np.mean(X)) / np.std(X)
    train_Y = Y
    return train_X, train_Y, X, Y
train_X, train_Y, X, Y = prepare_data()
m = len(train_X)
theta = tf.Variable(tf.random.uniform([1], -1.0, 1.0), name="theta")
bias = tf.Variable(tf.random.uniform([1], -1.0, 1.0), name="bias")
def hypothesis(X):
    return X * theta + bias
def compute_cost(X, Y):
    return tf.reduce_mean(tf.square(hypothesis(X) - Y)) / (2 * m)
optimizer = tf.optimizers.SGD(learning_rate)
def train_model():
    for epoch in range(training_epochs):
        with tf.GradientTape() as tape:
            cost = compute_cost(train_X, train_Y)
        gradients = tape.gradient(cost, [theta, bias])
        optimizer.apply_gradients(zip(gradients, [theta, bias]))
        if (epoch + 1) % display_step == 0:
            print(f"Epoch: {epoch + 1:04d} cost={cost:.9f} theta={theta.numpy()} bias={bias.numpy()}")
    training_cost = compute_cost(train_X, train_Y).numpy()
    print(f"Training cost={training_cost} theta={theta.numpy()} bias={bias.numpy()}\n")
train_model()
def plot_results():
    plt.plot(X, Y, 'r', label='Market Price (training)')
    plt.plot(X, hypothesis(train_X), label='Linear Regression Line')
    plt.title("Bitcoin Price Prediction: Training Linear Regression")
    plt.xlabel("Days")
    plt.ylabel("