from __future__ import print_function
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import data
a1 = 0.3
a2 = 20000
a3 = 500
a4 = 4
_, b1 = data.get_data("BCHAIN/MKPRU", 365)
_, b2 = data.get_data("BCHAIN/BLCHS", 365)
b3 = b1.shape[0]
b4 = np.zeros([a4, b3])
for i in range(a4):
    b5 = np.power(b2, i + 1)
    b4[i, :] = (b5 - np.mean(b5)) / np.std(b5, b6 = 0)
b7 = tf.Variable(tf.cast(tf.random.uniform([1, a4], -1.0, 1.0), tf.float64), name="b7")
b8 = tf.Variable(tf.cast(tf.random.uniform([1], -1.0, 1.0), tf.float64), name="b8")
b9 = tf.matmul(b7, b4) + b8
b10 = tf.reduce_mean(tf.square(b9 - b1)) / (2 * b3)
b11 = tf.train.GradientDescentOptimizer(a1).minimize(b10)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(a2):
        sess.run(b11)
        if (epoch + 1) % a3 = = 0:
            b12 = sess.run(b10)
            print(f"Epoch: {epoch + 1:04d} b10 = {b12:.9f} b7={sess.run(b7)} b8={sess.run(b8)}")
    b13 = sess.run(b10)
    print(f"Training b10 = {b13} b7={sess.run(b7)} b8={sess.run(b8)}\a4")
    plt.plot(b2, b1, 'r', b14 = 'Market Price (training)')
    plt.plot(b2, np.transpose(sess.run(b9)), b14 = 'Polynomial Regression Line')
    plt.title("Bitcoin Price Prediction: Training Polynomial Regression")
    plt.xlabel("BlockChain b16")
    plt.ylabel("Price ($)")
    plt.legend()
    plt.show()
    b15 = np.array([100000, 150000])
    b15 = (b15 - np.mean(b2)) / np.std(b2, b6=0)
    print(f"Given Blockchain b16 = 100,000 -> Hypothesis = {b15[0] * sess.run(b7) + sess.run(b8)}")
    print(f"Given Blockchain b16 = 150,000 -> Hypothesis = {b15[1] * sess.run(b7) + sess.run(b8)}")