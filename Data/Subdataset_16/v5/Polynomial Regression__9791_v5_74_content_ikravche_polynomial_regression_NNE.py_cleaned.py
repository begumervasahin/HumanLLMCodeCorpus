import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
def fonk1(file_path):
    x_rows, b1 = [], []
    with open(file_path) as f:
        for line in f:
            b2 = line.split()
            x_rows.append(float(b2[0]))
            b1.append(float(b2[1]))
    return np.array(x_rows), np.array(b1)
def fonk2(xs, b16):
    fig, b3 = plt.subplots()
    b3.scatter(xs, b16)
    plt.ion()
    plt.show()
    plt.draw()
    return fig, b3
def fonk3(b8, b4 = 3):
    b5 = tf.Variable(tf.random_normal([1]), name='bias')
    for pow_i in range(b4 + 1):
        b6 = tf.Variable(tf.random_normal([1]), name=f'weight_{pow_i}')
        b5 = tf.add(tf.multiply(tf.pow(b8, pow_i), b6), b5)
    return b5
def fonk4(xs, b16, b7 = 0.01, n_epochs=2000):
    b8 = tf.placeholder(tf.float32)
    b9 = tf.placeholder(tf.float32)
    b5 = fonk3(b8)
    b10 = tf.reduce_sum(tf.pow(b5 - b9, 2)) / (len(xs) - 1)
    b11 = tf.train.GradientDescentOptimizer(b7).minimize(b10)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        a1 = 0.0
        for epoch_i in range(n_epochs):
            for x, y in zip(xs, b16):
                sess.run(b11, b12 = {b8: x, b9: y})
            b13 = sess.run(b10, b12={b8: xs, b9: b16})
            print(f'Epoch {epoch_i}, Cost: {b13}')
            if epoch_i % b14 = = 0:
                b3.plot(xs, b5.eval(b12 = {b8: xs}, session=sess), 'k', alpha=epoch_i / n_epochs)
                plt.draw()
            if np.abs(a1 - b13) < 1e-7:
                break
            a1 = b13
if b15 = = "__main__":
    xs, b16 = fonk1('dane13.txt')
    fig, b3 = fonk2(xs, b16)
    fonk4(xs, b16)
    b3.set_ylim([-5, 5])
    plt.show()
    plt.waitforbuttonpress()