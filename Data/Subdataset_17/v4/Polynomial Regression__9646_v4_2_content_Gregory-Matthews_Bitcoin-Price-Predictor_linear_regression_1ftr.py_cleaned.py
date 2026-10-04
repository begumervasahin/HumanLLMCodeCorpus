from __future__ import print_function
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import data
learning_rate = 0.3
training_epochs = 10000
display_step = 500
X, Y = data.get_data("BCHAIN/MKPRU", 365)
_, X1 = data.get_data("BCHAIN/BLCHS", 365)
train_X = (X - np.mean(X)) / np.std(X, axis=0)
m = len(train_X)
theta = tf.Variable(tf.random.uniform([1], -1.0, 1.0), name="theta")
bias = tf.Variable(tf.random.uniform([1], -1.0, 1.0), name="bias")
hypothesis = train_X * theta + bias
cost = tf.reduce_mean(tf.square(hypothesis - Y)) / (2 * m)
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(training_epochs):
        sess.run(optimizer)
        if (epoch + 1) % display_step == 0:
            current_cost = sess.run(cost)
            current_theta = sess.run(theta)
            current_bias = sess.run(bias)
            print(f"Epoch: {epoch+1:04d} cost= {current_cost:.9f} theta= {current_theta} bias= {current_bias}")
    training_cost = sess.run(cost)
    final_theta = sess.run(theta)
    final_bias = sess.run(bias)
    print(f"Training cost= {training_cost} theta= {final_theta} bias= {final_bias}")
    plt.plot(X, Y, 'r', label='Market Price (training)')
    plt.plot(X, sess.run(hypothesis), label='Linear Regression Line')
    plt.title("Bitcoin Price Prediction: Training Linear Regression")
    plt.xlabel("Days")
    plt.ylabel("Price ($)")
    plt.legend()
    plt.show()
    test_X = np.array([100000, 150000])
    test_X = (test_X - np.mean(X)) / np.std(X, axis=0)
    prediction_100k = test_X[0] * final_theta + final_bias
    prediction_150k = test_X[1] * final_theta + final_bias
    print(f"Given Blockchain Size = 100,000 -> Hypothesis = {prediction_100k}")
    print(f"Given Blockchain Size = 150,000 -> Hypothesis = {prediction_150k}")