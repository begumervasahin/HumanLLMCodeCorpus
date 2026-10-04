from __future__ import print_function
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import data
a1 = 0.3
a2 = 10000
a3 = 500
bitcoin_price, b1 = data.get_data("BCHAIN/MKPRU", 365), data.get_data("BCHAIN/BLCHS", 365)
b2 = (bitcoin_price - np.mean(bitcoin_price)) / np.std(bitcoin_price, axis=0)
b3 = b1
b4 = len(b2)
b5 = tf.Variable(tf.random.uniform([1], -1.0, 1.0), name="b5")
b6 = tf.Variable(tf.random.uniform([1], -1.0, 1.0), name="b6")
b7 = b2 * b5 + b6
b8 = tf.reduce_mean(tf.square(b7 - b3)) / (2 * b4)
b9 = tf.train.GradientDescentOptimizer(a1).minimize(b8)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(a2):
        sess.run(b9)
        if (epoch + 1) % a3 = = 0:
            b10 = sess.run(b8)
            b11 = sess.run(b5)
            b12 = sess.run(b6)
            print(f"Epoch: {epoch+1:04d} b8 = {b10:.9f} b5= {b11} b6= {b12}")
    b13 = sess.run(b8)
    b14 = sess.run(b5)
    b15 = sess.run(b6)
    print(f"Training b8 = {b13} b5= {b14} b6= {b15}")
    plt.plot(bitcoin_price, b1, 'r', b16 = 'Market Price (training)')
    plt.plot(bitcoin_price, sess.run(b7), b16 = 'Linear Regression Line')
    plt.title("Bitcoin Price Prediction: Training Linear Regression")
    plt.xlabel("Days")
    plt.ylabel("Price ($)")
    plt.legend()
    plt.show()
    b17 = np.array([100000, 150000])
    b18 = (b17 - np.mean(bitcoin_price)) / np.std(bitcoin_price, axis=0)
    b19 = b18[0] * b14 + b15
    b20 = b18[1] * b14 + b15
    print(f"Given Blockchain b21 = 100,000 -> Hypothesis = {b19}")
    print(f"Given Blockchain b21 = 150,000 -> Hypothesis = {b20}")