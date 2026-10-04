from __future__ import print_function
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import data
learning_rate = 0.3
training_epochs = 10000
display_step = 500
features = ["BCHAIN/MWNUS", "BCHAIN/BLCHS"]
n = len(features)
_, train_Y = data.get_data("BCHAIN/MKPRU", 365)
m = train_Y.shape[0]
X_data = np.zeros([n, m])
train_X = np.zeros([n, m])
for i, feature in enumerate(features):
    _, X = data.get_data(feature, 365)
    train_X[i, :] = (X - np.mean(X)) / np.std(X, axis=0)
    X_data[i, :] = X
theta = tf.Variable(tf.random.uniform([1, n], -1.0, 1.0, dtype=tf.float64), name="theta")
bias = tf.Variable(tf.random.uniform([1], -1.0, 1.0, dtype=tf.float64), name="bias")
hypothesis = tf.matmul(theta, train_X) + bias
cost = tf.reduce_mean(tf.square(hypothesis - train_Y)) / (2 * m)
optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate).minimize(cost)
with tf.compat.v1.Session() as sess:
    sess.run(tf.compat.v1.global_variables_initializer())
    for epoch in range(training_epochs):
        sess.run(optimizer)
        if (epoch + 1) % display_step == 0:
            c = sess.run(cost)
            print(f"Epoch: {epoch+1:04d}, cost={c:.9f}, theta={sess.run(theta)}, bias={sess.run(bias)}")
    training_cost = sess.run(cost)
    print(f"Training cost={training_cost}, theta={sess.run(theta)}, bias={sess.run(bias)}\n")
    test_X = np.reshape([12000000.0, 100000.0], (2, 1))
    test_X[0] = (test_X[0] - np.mean(X_data[0])) / np.max(X_data[0], axis=0)
    test_X[1] = (test_X[1] - np.mean(X_data[1])) / np.max(X_data[1], axis=0)
    prediction = sess.run(tf.matmul(theta, test_X) + bias)
    print(prediction)