import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
with open('dane13.txt') as f:
    x_rows, b1 = [], []
    for line in f:
        b2 = line.split()
        x_rows.append(float(b2[0]))
        b1.append(float(b2[1]))
b3 = np.array(x_rows)
b4 = np.array(b1)
b5 = len(b3)
fig, b6 = plt.subplots()
b6.scatter(b3, b4)
plt.ion()
plt.show()
plt.draw()
b7 = tf.placeholder(tf.float32)
b8 = tf.placeholder(tf.float32)
b9 = tf.Variable(tf.random_normal([1]), name='bias')
for pow_i in range(4):
    b10 = tf.Variable(tf.random_normal([1]), name=f'weight_{pow_i}')
    b9 = tf.add(tf.multiply(tf.pow(b7, pow_i), b10), b9)
b11 = tf.reduce_sum(tf.pow(b9 - b8, 2)) / (b5 - 1)
a1 = 0.01
b12 = tf.train.GradientDescentOptimizer(a1).minimize(b11)
a2 = 2000
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    a3 = 0.0
    for epoch_i in range(a2):
        for (x, y) in zip(b3, b4):
            sess.run(b12, b13 = {b7: x, b8: y})
        b14 = sess.run(b11, b13={b7: b3, b8: b4})
        print(f'Epoch {epoch_i}, Cost: {b14}')
        if epoch_i % b15 = = 0:
            b6.plot(b3, b9.eval(b13 = {b7: b3}, session=sess), 'k', alpha=epoch_i / a2)
            plt.draw()
        if np.abs(a3 - b14) < 1e-7:
            break
        a3 = b14
b6.set_ylim([-5, 5])
plt.show()
plt.waitforbuttonpress()