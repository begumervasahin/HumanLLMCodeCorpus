import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib
N_OBSERVATIONS = 10
LEARNING_RATE = 1e-9
N_EPOCHS = 1
COVERAGE = 1.0
xs = np.array([1.1, 1.2, 2.7, 3.2, 4.1, 4.8, 6.1, 7.5, 9.5, 9.8])
ys = np.array([0.6, 2.5, 2.6, 3.8, 8.0, 5.9, 7.5, 5.5, 7.0, 9.8])
ws = np.ones(N_OBSERVATIONS)
TW = tf.placeholder(tf.float32, name='TW')
X = tf.placeholder(tf.float32, name='X')
Y = tf.placeholder(tf.float32, name='Y')
Y_pred = tf.Variable([-0.00029278], name='bias')
def build_model(Y_pred, X):
    weights = {
        1: tf.Variable([0.46918184], name='weight_1'),
        2: tf.Variable([1.00643885], name='weight_2'),
        3: tf.Variable([-0.23585591], name='weight_3'),
        4: tf.Variable([0.01418969], name='weight_4')
    }
    for pow_i, W in weights.items():
        Y_pred = tf.add(tf.multiply(tf.pow(X, pow_i), W), Y_pred)
    return Y_pred
Y_pred = build_model(Y_pred, X)
cost = tf.reduce_sum(tf.multiply(tf.pow(Y_pred - Y, 2), TW)) / (N_OBSERVATIONS - 1)
optimizer = tf.train.GradientDescentOptimizer(LEARNING_RATE).minimize(cost)
def train_model(sess, xs, ys, ws, n_epochs):
    for epoch_i in range(n_epochs):
        for x, y, w in zip(xs, ys, ws):
            sess.run(optimizer, feed_dict={X: x, Y: y, TW: w})
        training_cost = sess.run(cost, feed_dict={X: xs, Y: ys, TW: ws})
        print(f"{epoch_i} : {training_cost}")
        if epoch_i % 50 == 0 and epoch_i > 100:
            normal = np.abs(Y_pred.eval(feed_dict={X: xs}, session=sess) - ys) > COVERAGE
            if not np.any(normal):
                break
            ws[normal] *= 1.1
def plot_results(sess, xs, ys, Y_pred):
    fig, ax = plt.subplots(1, 1)
    xss = np.linspace(0, 10, 1000)
    ax.plot(xss, Y_pred.eval(feed_dict={X: xss}, session=sess), color='red', label='CWP')
    cx, cy = xs[3], ys[3]
    ax.plot([0, cx], [0, cy], color='blue', linestyle='dashed', label='General Path')
    ax.plot(np.concatenate([[cx], xs[3:]]), np.concatenate([[cy], ys[3:]]), color='blue', linestyle='dashed')
    ax.scatter(0.1, 0.15, color='black', marker='^', label='H-AP', s=matplotlib.rcParams['lines.markersize'] ** 2 + 50, zorder=10)
    ax.scatter(xs[:3], ys[:3], color='black', label='HGN', s=matplotlib.rcParams['lines.markersize'] ** 2 + 10, zorder=10)
    ax.scatter(xs[3:], ys[3:], color='black', marker='*', s=matplotlib.rcParams['lines.markersize'] ** 2 + 50, label='LGN', zorder=10)
    major_ticks = np.arange(0, 11, 1)
    ax.set_xticks(major_ticks)
    ax.set_yticks(major_ticks)
    ax.grid(which='both', linestyle='dashed', alpha=0.5)
    ax.set_ylim([0, 10])
    ax.set_xlim([0, 10])
    plt.xlabel('x(m)')
    plt.ylabel('y(m)')
    plt.legend(loc='lower right', fontsize='small', framealpha=1)
    plt.savefig('test.eps', format='eps', dpi=1000)
    plt.show()
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    train_model(sess, xs, ys, ws, N_EPOCHS)
    plot_results(sess, xs, ys, Y_pred)
    weights_bias = {v.name: sess.run(v) for v in tf.trainable_variables()}
    for name, value in weights_bias.items():
        print(f"{name} : {value}")