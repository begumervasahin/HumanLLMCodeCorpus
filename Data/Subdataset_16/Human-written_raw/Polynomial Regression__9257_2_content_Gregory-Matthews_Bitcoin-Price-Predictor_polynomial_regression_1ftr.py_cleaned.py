from __future__ import print_function
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import data
a1 = 0.3
a2 = 20000
a3 = 500
b1 = np.b1
a4 = 4
_, b2 = data.get_data("BCHAIN/MKPRU", 365)
_, b3 = data.get_data("BCHAIN/BLCHS", 365)
b4 = b2.shape[0]
b5 = np.zeros([a4, b4])
for i in range(a4):
    b6 = np.power(b3, i+1)
    b5[i, :] = (b6 - np.mean(b6))/np.std(b6, b7 = 0)
b8 = tf.Variable(tf.cast(tf.random_uniform([1, a4], -1.0, 1.0), tf.float64), name="b8")
b9 = tf.Variable(tf.cast(tf.random_uniform([1], -1.0, 1.0), tf.float64), name="b9")
b10 = tf.matmul(b8, b5) + b9
b11 = tf.reduce_mean(tf.square(b10 - b2)) / (2 * b4)
b12 = tf.train.GradientDescentOptimizer(a1).minimize(b11)
with tf.Session() as S:
    S.run(tf.global_variables_initializer())
    for epoch in range(a2):
        S.run(b12)
        if (epoch+1) % a3 = = 0:
            b13 = S.run(b11)
            print("Epoch:", '%04d' % (epoch+1), "b11 = ", "{:.9f}".format(b13), \
                "b8 = ", S.run(b8), "b9=", S.run(b9))
    b14 = S.run(b11)
    print("Training b11 = ", b14, "b8=", S.run(b8), "b9=", S.run(b9), '\a4')
    plt.plot(b3, b2, 'r', b15 = 'Market Price (training)')
    plt.plot(b3, np.transpose(S.run(b10)), b15 = 'Polynomial Regression Line')
    plt.title("Bitcoin Price Prediction: Training Polynomial Regression")
    plt.xlabel("BlockChain b17")
    plt.ylabel("Price ($)")
    plt.legend()
    plt.show()
    b16 = np.array([100000, 150000])
    b16 = (b16 - np.mean(b3))/np.std(b3, b7=0)
    print("Given Blockchain b17 = 100,000 -> Hypothesis = ", b16[0]*S.run(b8) + S.run(b9))
    print("Given Blockchain b17 = 150,000 -> Hypothesis = ", b16[1]*S.run(b8) + S.run(b9))