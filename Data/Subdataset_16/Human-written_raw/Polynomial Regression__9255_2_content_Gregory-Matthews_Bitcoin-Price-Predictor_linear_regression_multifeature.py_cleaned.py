from __future__ import print_function
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import data
a1 = .3
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
b9 = tf.Variable(tf.cast(tf.random_uniform([1, b2], -1.0, 1.0), tf.float64), name="b9")
b10 = tf.Variable(tf.cast(tf.random_uniform([1], -1.0, 1.0), tf.float64), name="b10")
b11 = tf.matmul(b9, b6) + b10
b12 = tf.reduce_mean(tf.square(b11 - b3)) / (2 * b4)
b13 = tf.train.GradientDescentOptimizer(a1).minimize(b12)
with tf.Session() as S:
    S.run(tf.global_variables_initializer())
    for epoch in range(a2):
        S.run(b13)
        if (epoch+1) % a3 = = 0:
            b14 = S.run(b12)
            print("Epoch:", '%04d' % (epoch+1), "b12 = ", "{:.9f}".format(b14), \
                "b9 = ", S.run(b9), "b10=", S.run(b10))
    b15 = S.run(b12)
    print("Training b12 = ", b15, "b9=", S.run(b9), "b10=", S.run(b10), '\b2')
    b16 = np.reshape([12000000.0, 100000.0], (2, 1))
    b16[0] = (b16[0] - np.mean(b5[0]))/np.max(b5[0], b8 = 0)
    b16[1] = (b16[1] - np.mean(b5[1]))/np.max(b5[1], b8 = 0)
    print(S.run(tf.matmul(b9, b16) + b10))