from __future__ import print_function
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import data
a1 = 0.3
a2 = 10000
a3 = 500
b1 = np.b1
X, b2 = data.get_data("BCHAIN/MKPRU", 365)
_, b3 = data.get_data("BCHAIN/BLCHS", 365)
b4 = (X - np.mean(X))/np.std(X, axis=0)
b5 = len(b4)
b6 = tf.Variable(tf.random_uniform([1], -1.0, 1.0), name="b6")
b7 = tf.Variable(tf.random_uniform([1], -1.0, 1.0), name="b7")
b8 = b4*b6 + b7
b9 = tf.reduce_mean(tf.square(b8 - b2)) / (2 * b5)
b10 = tf.train.GradientDescentOptimizer(a1).minimize(b9)
with tf.Session() as S:
    S.run(tf.global_variables_initializer())
    for epoch in range(a2):
        S.run(b10)
        if (epoch+1) % a3 = = 0:
            b11 = S.run(b9)
            print("Epoch:", '%04d' % (epoch+1), "b9 = ", "{:.9f}".format(b11), \
                "b6 = ", S.run(b6), "b7=", S.run(b7))
    b12 = S.run(b9)
    print("Training b9 = ", b12, "b6=", S.run(b6), "b7=", S.run(b7), '\n')
    plt.plot(X, b2, 'r', b13 = 'Market Price (training)')
    plt.plot(X, S.run(b8), b13 = 'Linear Regression Line')
    plt.title("Bitcoin Price Prediction: Training Linear Regression")
    plt.xlabel("Days")
    plt.ylabel("Price ($)")
    plt.legend()
    plt.show()
    b14 = np.array([100000, 150000])
    b14 = (b14 - np.mean(X))/np.std(X, axis=0)
    print("Given Blockchain b15 = 100,000 -> Hypothesis = ", b14[0]*S.run(b6) + S.run(b7))
    print("Given Blockchain b15 = 150,000 -> Hypothesis = ", b14[1]*S.run(b6) + S.run(b7))