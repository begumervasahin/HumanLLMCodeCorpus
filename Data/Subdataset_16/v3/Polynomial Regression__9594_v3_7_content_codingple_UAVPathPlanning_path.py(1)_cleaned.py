import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib
a1 = 10
b1 = np.array([1.1, 1.2, 2.7, 3.2, 4.1, 4.8, 6.1, 7.5, 9.5, 9.8])
b2 = np.array([0.6, 2.5, 2.6, 3.8, 8.0, 5.9, 7.5, 5.5, 7.0, 9.8])
b3 = np.ones(a1)
b4 = tf.placeholder(tf.float32, name='b4')
b5 = tf.placeholder(tf.float32, name='b5')
b6 = tf.placeholder(tf.float32, name='b6')
a2 = -0.00029278
b7 = tf.Variable([a2], name='bias')
b8 = [0.46918184, 1.00643885, -0.23585591, 0.01418969]
for pow_i, weight in enumerate(b8, 1):
    b9 = tf.Variable(weight, name=f'weight_{pow_i}')
    b7 = tf.add(tf.multiply(tf.pow(b4, pow_i), b9), b7)
b10 = tf.reduce_sum(tf.multiply(tf.pow(b7 - b5, 2), b6)) / (a1 - 1)
b11 = tf.train.GradientDescentOptimizer(learning_rate=0.1e-8).minimize(b10)
def fonk1(sess, a3, b1, b2, b3):
    for epoch_i in range(a3):
        for x, y, w in zip(b1, b2, b3):
            sess.run(b11, b12 = {b4: x, b5: y, b6: w})
        b13 = sess.run(b10, b12={b4: b1, b5: b2, b6: b3})
        print(f"Epoch {epoch_i}: {b13}")
def fonk2(b21, sess, b22, cx, b23, b1, b2):
    b14 = [sess.run(b7, b12={b4: x}) for x in b22]
    b21.plot(b22, b14, b15 = 'red', label='CWP')
    b21.plot([0, cx], [0, b23], b15 = 'blue', linestyle='dashed', label='General Path')
    b21.plot(np.concatenate([[cx], b1[3:]]), np.concatenate([[b23], b2[3:]]), b15 = 'blue', linestyle='dashed')
    b21.scatter(0.1, 0.15, b15 = 'black', marker='^', label='H-AP',
               b16 = matplotlib.rcParams['lines.markersize'] ** 2 + 50, zorder=10)
    b21.scatter(b1[:3], b2[:3], b15 = 'black', label='HGN',
               b16 = matplotlib.rcParams['lines.markersize'] ** 2 + 10, zorder=10)
    b21.scatter(b1[3:], b2[3:], b15 = 'black', marker='*',
               b16 = matplotlib.rcParams['lines.markersize'] ** 2 + 50, label='LGN', zorder=10)
    b17 = np.arange(0, 11, 1)
    b21.set_xticks(b17)
    b21.set_yticks(b17)
    b21.grid(b18 = 'both')
    b21.grid(b18 = 'minor', alpha=0.2)
    b21.grid(b18 = 'major', alpha=0.5)
    b21.set_ylim([0, 10])
    b21.set_xlim([0, 10])
    plt.xlabel('x(m)')
    plt.ylabel('y(m)')
    plt.legend(b19 = 'lower right', fontsize='small', framealpha=1)
    plt.grid(b20 = 'dashed')
def fonk3():
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        a3 = 1
        fonk1(sess, a3, b1, b2, b3)
        fig, b21 = plt.subplots(1, 1)
        b22 = np.linspace(0, 10, 1000)
        cx, b23 = b1[3], b2[3]
        fonk2(b21, sess, b22, cx, b23, b1, b2)
        plt.savefig('test.eps', b24 = 'eps', dpi=1000)
        plt.show()
        b25 = [sess.run(var) for var in tf.trainable_variables()]
        print("Weights and bias:", b25)
if b26 = = "__main__":
    fonk3()