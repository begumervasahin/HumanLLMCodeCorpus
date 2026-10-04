import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
b1 = open('dane13.txt')
b2 = []
b3 = []
for line in b1:
    b4 = line.split()
    b2.append(float(b4[0]))
    b3.append(float(b4[1]))
b5 = len(b2)
fig, b6 = plt.subplots(1, 1)
b7 = b2
b8 = b3
plt.ion()
b6.scatter(b7, b8)
fig.show()
plt.draw()
b9 = tf.placeholder(tf.float32)
b10 = tf.placeholder(tf.float32)
b11 = tf.Variable(tf.random_normal([1]), name='bias')
for pow_i in range(0, 4):
    b12 = tf.Variable(tf.random_normal([1]), name='weight_%d' % pow_i)
    b11 = tf.add(tf.multiply(tf.pow(b9, pow_i), b12), b11)
b13 = tf.reduce_sum(tf.pow(b11 - b10, 2)) / (b5 - 1)
a1 = 0.01
b14 = tf.train.GradientDescentOptimizer(a1).minimize(b13)
a2 = 2000
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    a3 = 0.0
    for epoch_i in range(a2):
        for (x, y) in zip(b7, b8):
            sess.run(b14, b15 = {b9: x, b10: y})
        b16 = sess.run(
            b13, b15 = {b9: b7, b10: b8})
        print(b16)
        if epoch_i % b17 = = 0:
            b6.plot(b7, b11.eval(
                b15 = {b9: b7}, session=sess),
                    'k', b18 = epoch_i / a2)
            fig.show()
            plt.draw()
        if np.abs(a3 - b16) < 0.0000001:
            break
        a3 = b16
b6.set_ylim([-5, 5])
fig.show()
plt.waitforbuttonpress()