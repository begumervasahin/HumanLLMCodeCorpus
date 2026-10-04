import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
with open('dane13.txt') as f:
    x_rows, y_rows = [], []
    for line in f:
        row = line.split()
        x_rows.append(float(row[0]))
        y_rows.append(float(row[1]))
xs = np.array(x_rows)
ys = np.array(y_rows)
n_observations = len(xs)
fig, ax = plt.subplots()
ax.scatter(xs, ys)
plt.ion()
plt.show()
plt.draw()
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)
Y_pred = tf.Variable(tf.random_normal([1]), name='bias')
for pow_i in range(4):
    W = tf.Variable(tf.random_normal([1]), name=f'weight_{pow_i}')
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
        training_cost = sess.run(cost, feed_dict={X: xs, Y: ys})
        print(f'Epoch {epoch_i}, Cost: {training_cost}')
        if epoch_i % 100 == 0:
            ax.plot(xs, Y_pred.eval(feed_dict={X: xs}, session=sess), 'k', alpha=epoch_i / n_epochs)
            plt.draw()
        if np.abs(prev_training_cost - training_cost) < 1e-7:
            break
        prev_training_cost = training_cost
ax.set_ylim([-5, 5])
plt.show()
plt.waitforbuttonpress()