import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib
n_observations = 10
xs = np.array([1.1, 1.2, 2.7, 3.2, 4.1, 4.8, 6.1, 7.5, 9.5, 9.8])
ys = np.array([0.6, 2.5, 2.6, 3.8, 8.0, 5.9, 7.5, 5.5, 7.0, 9.8])
ws = np.ones(n_observations)
TW = tf.placeholder(tf.float32)
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)
Y_pred = tf.Variable([-0.00029278], name='bias')
for pow_i in range(1, 5):
    if pow_i == 1:
        W = tf.Variable([0.46918184], name='weight_%d' % pow_i)
    elif pow_i == 2:
        W = tf.Variable([1.00643885], name='weight_%d' % pow_i)
    elif pow_i == 3:
        W = tf.Variable([-0.23585591], name='weight_%d' % pow_i)
    elif pow_i == 4:
        W = tf.Variable([0.01418969], name='weight_%d' % pow_i)
    Y_pred = tf.add(tf.multiply(tf.pow(X, pow_i), W), Y_pred)
cost = tf.reduce_sum(tf.multiply(tf.pow(Y_pred - Y, 2), TW)) / (n_observations - 1)
learning_rate = 0.1e-8
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
n_epochs = 1
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    prev_training_cost = 0.0
    for epoch_i in range(n_epochs):
        for (x, y, w) in zip(xs, ys, ws):
            sess.run(optimizer, feed_dict={X: x, Y: y, TW: w})
        training_cost = sess.run(cost, feed_dict={X: xs, Y: ys, TW: ws})
        print(f"{epoch_i} : {training_cost}")
    hi = [0, 0, 0, 0, 0]
    var = [v for v in tf.trainable_variables() if v.name == "bias:0"][0]
    hi[4] = np.float32(sess.run(var))
    for pow_i in range(1, 5):
        var = [v for v in tf.trainable_variables() if v.name == f"weight_{pow_i}:0"][0]
        hi[(pow_i)-1] = np.float32(sess.run(var))
        print(f"Weight{pow_i} : {hi[(pow_i)-1]}")
    print(f"bias : {hi[4]}")
    fig, ax = plt.subplots(1, 1)
    xss = np.linspace(0, 10, 1000)
    y_pred_vals = sess.run(Y_pred, feed_dict={X: xss})
    ax.plot(xss, y_pred_vals, color='red', label='CWP')
    cx = xs[3]
    cy = ys[3]
    ax.plot([0, cx], [0, cy], color='blue', linestyle='dashed', label='General Path')
    ax.plot(np.concatenate([[cx], xs[3:]]), np.concatenate([[cy], ys[3:]]), color='blue', linestyle='dashed')
    ax.scatter(0.1, 0.15, color='black', marker='^', label='H-AP', s=matplotlib.rcParams['lines.markersize'] ** 2 + 50, zorder=10)
    ax.scatter(xs[:3], ys[:3], color='black', label='HGN', s=matplotlib.rcParams['lines.markersize'] ** 2 + 10, zorder=10)
    ax.scatter(xs[3:], ys[3:], color='black', marker='*', s=matplotlib.rcParams['lines.markersize'] ** 2 + 50, label='LGN', zorder=10)
    major_ticks = np.arange(0, 11, 1)
    ax.set_xticks(major_ticks)
    ax.set_yticks(major_ticks)
    ax.grid(which='both')
    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)
    ax.set_ylim([0, 10])
    ax.set_xlim([0, 10])
    plt.xlabel('x(m)')
    plt.ylabel('y(m)')
    plt.legend(loc='lower right', fontsize='small', framealpha=1)
    plt.grid(ls='dashed')
    plt.savefig('test.eps', format='eps', dpi=1000)
    plt.show()
    plt.waitforbuttonpress()