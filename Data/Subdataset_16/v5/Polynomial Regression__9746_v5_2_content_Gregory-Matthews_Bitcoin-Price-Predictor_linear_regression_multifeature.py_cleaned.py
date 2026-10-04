from __future__ import print_function
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import data
a1 = 0.3
a2 = 10000
a3 = 500
b1 = ["BCHAIN/MWNUS", "BCHAIN/BLCHS"]
b2 = len(b1)
_, b3 = data.get_data("BCHAIN/MKPRU", 365)
b4 = b3.shape[0]
b5 = np.zeros([b2, b4])
b6 = np.zeros([b2, b4])
for i, feature in enumerate(b1):
    _, b7 = data.get_data(feature, 365)
    b6[i, :] = (b7 - np.mean(b7)) / np.std(b7, b8 = 0)
    b5[i, :] = b7
b9 = tf.Variable(tf.random.uniform([1, b2], -1.0, 1.0, dtype=tf.float64), name="b9")
b10 = tf.Variable(tf.random.uniform([1], -1.0, 1.0, dtype=tf.float64), name="b10")
b11 = tf.matmul(b9, b6) + b10
b12 = tf.reduce_mean(tf.square(b11 - b3)) / (2 * b4)
b13 = tf.compat.v1.train.GradientDescentOptimizer(a1).minimize(b12)
with tf.compat.v1.Session() as sess:
    sess.run(tf.compat.v1.global_variables_initializer())
    for epoch in range(a2):
        sess.run(b13)
        if (epoch + 1) % a3 = = 0:
            b14 = sess.run(b12)
            b15 = sess.run(b9)
            b16 = sess.run(b10)
            print(f"Epoch: {epoch+1:04d}, b12 = {b14:.9f}, b9={b15}, b10={b16}")
    b17 = sess.run(b12)
    b18 = sess.run(b9)
    b19 = sess.run(b10)
    print(f"Training b12 = {b17}, b9={b18}, b10={b19}\n")
    b20 = np.reshape([12000000.0, 100000.0], (2, 1))
    b20[0] = (b20[0] - np.mean(b5[0])) / np.max(b5[0], b8 = 0)
    b20[1] = (b20[1] - np.mean(b5[1])) / np.max(b5[1], b8 = 0)
    b21 = sess.run(tf.matmul(b9, b20) + b10)
    print(b21)