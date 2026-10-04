import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
f = open('dane13.txt')
x_rows = []
y_rows = []
for line in f:
    row = line.split()
    x_rows.append(float(row[0]))
    y_rows.append(float(row[1]))
n_observations = len(x_rows)
fig, ax = plt.subplots(1, 1)
xs = x_rows
ys = y_rows
plt.ion()
ax.scatter(xs, ys)
fig.show()
plt.draw()
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)
Y_pred = tf.Variable(tf.random_normal([1]), name='bias')
for pow_i in range(0, 4):
    W = tf.Variable(tf.random_normal([1]), name='weight_%d' % pow_i)
    Y_pred = tf.add(tf.multiply(tf.pow(X, pow_i), W), Y_pred)
cost = tf.reduce_sum(tf.pow(Y_pred - Y, 2)) / (n_observations - 1)
learning_rate = 0.01
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
n_epochs = 2000
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    prev_training_cost = 0.0
    for epoch_i in range(n_epochs):
        for (x, y) in zip(xs, ys):
            sess.run(optimizer, feed_dict={X: x, Y: y})
        training_cost = sess.run(
            cost, feed_dict={X: xs, Y: ys})
        print(training_cost)
        if epoch_i % 100 == 0:
            ax.plot(xs, Y_pred.eval(
                feed_dict={X: xs}, session=sess),
                    'k', alpha=epoch_i / n_epochs)
            fig.show()
            plt.draw()
        if np.abs(prev_training_cost - training_cost) < 0.0000001:
            break
        prev_training_cost = training_cost
ax.set_ylim([-5, 5])
fig.show()
plt.waitforbuttonpress()