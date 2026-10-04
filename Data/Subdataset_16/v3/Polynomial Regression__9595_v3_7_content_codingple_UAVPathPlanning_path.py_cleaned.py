import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib
a1 = 10
b1 = np.array([1.1, 1.2, 2.7, 3.2, 4.1, 4.8, 6.1, 7.5, 9.5, 9.8])
b2 = np.array([0.6, 2.5, 2.6, 3.8, 8.0, 5.9, 7.5, 5.5, 7.0, 9.8])
b3 = np.ones(a1)
b4 = tf.placeholder(tf.float32, b9="b4")
b5 = tf.placeholder(tf.float32, b9="b5")
b6 = tf.placeholder(tf.float32, b9="b6")
b7 = tf.Variable([-0.00029278], b9='b7')
b8 = {
    1: tf.Variable([0.46918184], b9 = 'weight_1'),
    2: tf.Variable([1.00643885], b9 = 'weight_2'),
    3: tf.Variable([-0.23585591], b9 = 'weight_3'),
    4: tf.Variable([0.01418969], b9 = 'weight_4')
}
b10 = b7
for pow_i in range(1, 5):
    b10 += tf.multiply(tf.pow(b5, pow_i), b8[pow_i])
b11 = tf.reduce_sum(tf.multiply(tf.pow(b10 - b6, 2), b4)) / (a1 - 1)
a2 = 1e-9
b12 = tf.train.GradientDescentOptimizer(a2).minimize(b11)
a3 = 1
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch_i in range(a3):
        for (x, y, w) in zip(b1, b2, b3):
            sess.run(b12, b13 = {b5: x, b6: y, b4: w})
        b14 = sess.run(b11, b13={b5: b1, b6: b2, b4: b3})
        print(f"Epoch {epoch_i}: {b14}")
    b15 = sess.run(b7)
    b16 = {pow_i: sess.run(b8[pow_i]) for pow_i in range(1, 5)}
    for pow_i in range(1, 5):
        print(f"Weight {pow_i}: {b16[pow_i]}")
    print(f"Bias: {b15}")
    fig, b17 = plt.subplots()
    b18 = np.linspace(0, 10, 1000)
    b19 = sess.run(b10, b13={b5: b18})
    b17.plot(b18, b19, b20 = 'red', label='CWP')
    cx, b21 = b1[3], b2[3]
    b17.plot([0, cx], [0, b21], b20 = 'blue', linestyle='dashed', label='General Path')
    b17.plot(np.concatenate([[cx], b1[3:]]), np.concatenate([[b21], b2[3:]]), b20 = 'blue', linestyle='dashed')
    b17.scatter(0.1, 0.15, b20 = 'black', marker='^', label='H-AP', s=matplotlib.rcParams['lines.markersize'] ** 2 + 50, zorder=10)
    b17.scatter(b1[:3], b2[:3], b20 = 'black', label='HGN', s=matplotlib.rcParams['lines.markersize'] ** 2 + 10, zorder=10)
    b17.scatter(b1[3:], b2[3:], b20 = 'black', marker='*', label='LGN', s=matplotlib.rcParams['lines.markersize'] ** 2 + 50, zorder=10)
    b17.set_xticks(np.arange(0, 11, 1))
    b17.set_yticks(np.arange(0, 11, 1))
    b17.grid(b22 = 'both')
    b17.grid(b22 = 'minor', alpha=0.2)
    b17.grid(b22 = 'major', alpha=0.5)
    b17.set_ylim([0, 10])
    b17.set_xlim([0, 10])
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.legend(b23 = 'lower right', fontsize='small', framealpha=1)
    plt.grid(b24 = 'dashed')
    plt.savefig('test.eps', b25 = 'eps', dpi=1000)
    plt.show()
    plt.waitforbuttonpress()