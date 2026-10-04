import numpy as np
import tensorflow as tf
from tensorflow.keras.optimizers import SGD
def get_data(feature, days):
    np.random.seed(0)
    X = np.random.rand(days) * 1000
    return None, X
learning_rate = 0.3
training_epochs = 10000
display_step = 500
features = ["BCHAIN/MWNUS", "BCHAIN/BLCHS"]
_, train_Y = get_data("BCHAIN/MKPRU", 365)
m = train_Y.shape[0]
n = len(features)
X_data = np.zeros([n, m])
train_X = np.zeros([n, m])
for i, feature in enumerate(features):
    _, X = get_data(feature, 365)
    train_X[i, :] = (X - np.mean(X)) / np.std(X, axis=0)
    X_data[i, :] = X
theta = tf.Variable(tf.random.uniform([1, n], -1.0, 1.0, dtype=tf.float64), name="theta")
bias = tf.Variable(tf.random.uniform([1], -1.0, 1.0, dtype=tf.float64), name="bias")
def hypothesis(X):
    return tf.matmul(theta, X) + bias
def cost_fn():
    return tf.reduce_mean(tf.square(hypothesis(train_X) - train_Y)) / (2 * m)
optimizer = SGD(learning_rate=learning_rate)
for epoch in range(training_epochs):
    optimizer.minimize(cost_fn, var_list=[theta, bias])
    if (epoch + 1) % display_step == 0:
        c = cost_fn().numpy()
        print(f"Epoch: {epoch + 1:04d} cost={c:.9f} theta={theta.numpy()} bias={bias.numpy()}")
training_cost = cost_fn().numpy()
print(f"Training cost={training_cost} theta={theta.numpy()} bias={bias.numpy()}\n")
test_X = np.array([12000000.0, 100000.0]).reshape(2, 1)
test_X[0] = (test_X[0] - np.mean(X_data[0])) / np.max(X_data[0], axis=0)
test_X[1] = (test_X[1] - np.mean(X_data[1])) / np.max(X_data[1], axis=0)
predicted_value = hypothesis(test_X).numpy()
print(predicted_value)