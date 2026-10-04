import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
def load_data(file_path):
    x_rows, y_rows = [], []
    with open(file_path) as f:
        for line in f:
            row = line.split()
            x_rows.append(float(row[0]))
            y_rows.append(float(row[1]))
    return np.array(x_rows), np.array(y_rows)
def plot_initial_data(xs, ys):
    fig, ax = plt.subplots()
    ax.scatter(xs, ys)
    plt.ion()
    plt.show()
    plt.draw()
    return fig, ax
def build_model(X, degree=3):
    Y_pred = tf.Variable(tf.random_normal([1]), name='bias')
    for pow_i in range(degree + 1):
        W = tf.Variable(tf.random_normal([1]), name=f'weight_{pow_i}')
        Y_pred = tf.add(tf.multiply(tf.pow(X, pow_i), W), Y_pred)
    return Y_pred
def train_model(xs, ys, learning_rate=0.01, n_epochs=2000):
    X = tf.placeholder(tf.float32)
    Y = tf.placeholder(tf.float32)
    Y_pred = build_model(X)
    cost = tf.reduce_sum(tf.pow(Y_pred - Y, 2)) / (len(xs) - 1)
    optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        prev_training_cost = 0.0
        for epoch_i in range(n_epochs):
            for x, y in zip(xs, ys):
                sess.run(optimizer, feed_dict={X: x, Y: y})
            training_cost = sess.run(cost, feed_dict={X: xs, Y: ys})
            print(f'Epoch {epoch_i}, Cost: {training_cost}')
            if epoch_i % 100 == 0:
                ax.plot(xs, Y_pred.eval(feed_dict={X: xs}, session=sess), 'k', alpha=epoch_i / n_epochs)
                plt.draw()
            if np.abs(prev_training_cost - training_cost) < 1e-7:
                break
            prev_training_cost = training_cost
if __name__ == "__main__":
    xs, ys = load_data('dane13.txt')
    fig, ax = plot_initial_data(xs, ys)
    train_model(xs, ys)
    ax.set_ylim([-5, 5])
    plt.show()
    plt.waitforbuttonpress()