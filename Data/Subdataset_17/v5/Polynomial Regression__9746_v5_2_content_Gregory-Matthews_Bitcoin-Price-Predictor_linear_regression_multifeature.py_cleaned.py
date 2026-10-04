from __future__ import print_function
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import data
LEARNING_RATE = 0.3
TRAINING_EPOCHS = 10000
DISPLAY_STEP = 500
FEATURES = ["BCHAIN/MWNUS", "BCHAIN/BLCHS"]
NUM_FEATURES = len(FEATURES)
_, train_Y = data.get_data("BCHAIN/MKPRU", 365)
NUM_SAMPLES = train_Y.shape[0]
X_data = np.zeros([NUM_FEATURES, NUM_SAMPLES])
train_X = np.zeros([NUM_FEATURES, NUM_SAMPLES])
for i, feature in enumerate(FEATURES):
    _, X = data.get_data(feature, 365)
    train_X[i, :] = (X - np.mean(X)) / np.std(X, axis=0)
    X_data[i, :] = X
theta = tf.Variable(tf.random.uniform([1, NUM_FEATURES], -1.0, 1.0, dtype=tf.float64), name="theta")
bias = tf.Variable(tf.random.uniform([1], -1.0, 1.0, dtype=tf.float64), name="bias")
hypothesis = tf.matmul(theta, train_X) + bias
cost = tf.reduce_mean(tf.square(hypothesis - train_Y)) / (2 * NUM_SAMPLES)
optimizer = tf.compat.v1.train.GradientDescentOptimizer(LEARNING_RATE).minimize(cost)
with tf.compat.v1.Session() as sess:
    sess.run(tf.compat.v1.global_variables_initializer())
    for epoch in range(TRAINING_EPOCHS):
        sess.run(optimizer)
        if (epoch + 1) % DISPLAY_STEP == 0:
            current_cost = sess.run(cost)
            current_theta = sess.run(theta)
            current_bias = sess.run(bias)
            print(f"Epoch: {epoch+1:04d}, cost={current_cost:.9f}, theta={current_theta}, bias={current_bias}")
    final_cost = sess.run(cost)
    final_theta = sess.run(theta)
    final_bias = sess.run(bias)
    print(f"Training cost={final_cost}, theta={final_theta}, bias={final_bias}\n")
    test_X = np.reshape([12000000.0, 100000.0], (2, 1))
    test_X[0] = (test_X[0] - np.mean(X_data[0])) / np.max(X_data[0], axis=0)
    test_X[1] = (test_X[1] - np.mean(X_data[1])) / np.max(X_data[1], axis=0)
    prediction = sess.run(tf.matmul(theta, test_X) + bias)
    print(prediction)