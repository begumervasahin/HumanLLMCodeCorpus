import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib
a1 = 10
b1 = np.array([1.1, 1.2, 2.7, 3.2, 4.1, 4.8, 6.1, 7.5, 9.5, 9.8])
b2 = np.array([0.6, 2.5, 2.6, 3.8, 8.0, 5.9, 7.5, 5.5, 7.0, 9.8])
b3 = np.ones(a1)
b4 = tf.placeholder(tf.float32, b9='b4')
b5 = tf.placeholder(tf.float32, b9='b5')
b6 = tf.placeholder(tf.float32, b9='b6')
b7 = tf.Variable([-0.00029278], b9='bias')
b8 = {
    1: tf.Variable([0.46918184], b9 = 'weight_1'),
    2: tf.Variable([1.00643885], b9 = 'weight_2'),
    3: tf.Variable([-0.23585591], b9 = 'weight_3'),
    4: tf.Variable([0.01418969], b9 = 'weight_4')
}
for pow_i in range(1, 5):
    b7 = tf.add(tf.multiply(tf.pow(b5, pow_i), b8[pow_i]), b7)
b10 = tf.reduce_sum(tf.multiply(tf.pow(b7 - b6, 2), b4)) / (a1 - 1)
a2 = 0.1e-8
b11 = tf.train.GradientDescentOptimizer(a2).minimize(b10)
a3 = 1
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch_i in range(a3):
        for (x, y, w) in zip(b1, b2, b3):
            sess.run(b11, b12 = {b5: x, b6: y, b4: w})
        b13 = sess.run(b10, b12={b5: b1, b6: b2, b4: b3})
        print(f"Epoch {epoch_i}: Training b10 = {b13}")
        if epoch_i % b14 = = 0 and epoch_i > 100:
            b15 = np.abs(sess.run(b7, b12={b5: b1}) - b2) > 1.0
            if not np.any(b15):
                break
            b3[b15] *= 1.1
    b16 = {f'weight_{i}': np.float32(sess.run(b8[i])) for i in range(1, 5)}
    b17 = np.float32(sess.run(tf.trainable_variables(scope="bias")[0]))
    print("Weights:", b16)
    print("Bias:", b17)
    fig, b18 = plt.subplots()
    b19 = np.linspace(0, 10, 1000)
    b18.plot(b19, sess.run(b7, b12 = {b5: b19}), b20='red', label='CWP')
    b18.plot([0, b1[3]], [0, b2[3]], b20 = 'blue', linestyle='dashed', label='General Path')
    b18.plot(np.concatenate([[b1[3]], b1[3:]]), np.concatenate([[b2[3]], b2[3:]]), b20 = 'blue', linestyle='dashed')
    b18.scatter(0.1, 0.15, b20 = 'black', marker='^', label='H-AP', s=matplotlib.rcParams['lines.markersize'] ** 2 + b14, zorder=10)
    b18.scatter(b1[:3], b2[:3], b20 = 'black', label='HGN', s=matplotlib.rcParams['lines.markersize'] ** 2 + 10, zorder=10)
    b18.scatter(b1[3:], b2[3:], b20 = 'black', marker='*', s=matplotlib.rcParams['lines.markersize'] ** 2 + b14, label='LGN', zorder=10)
    b18.set_xticks(np.arange(0, 11, 1))
    b18.set_yticks(np.arange(0, 11, 1))
    b18.grid(b21 = 'both')
    b18.grid(b21 = 'minor', alpha=0.2)
    b18.grid(b21 = 'major', alpha=0.5)
    b18.set_xlim([0, 10])
    b18.set_ylim([0, 10])
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.legend(b22 = 'lower right', fontsize='small', framealpha=1)
    plt.grid(b23 = 'dashed')
    plt.savefig('test.eps', b24 = 'eps', dpi=1000)
    plt.show()
    plt.waitforbuttonpress()