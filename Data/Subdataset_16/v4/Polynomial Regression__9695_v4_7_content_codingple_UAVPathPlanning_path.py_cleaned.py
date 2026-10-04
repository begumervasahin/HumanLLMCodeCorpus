import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib
a1 = 10
a2 = 1e-9
a3 = 1
a4 = 1.0
b1 = np.array([1.1, 1.2, 2.7, 3.2, 4.1, 4.8, 6.1, 7.5, 9.5, 9.8])
b2 = np.array([0.6, 2.5, 2.6, 3.8, 8.0, 5.9, 7.5, 5.5, 7.0, 9.8])
b3 = np.ones(a1)
b4 = tf.placeholder(tf.float32)
b5 = tf.placeholder(tf.float32)
b6 = tf.placeholder(tf.float32)
b7 = tf.Variable([-0.00029278], name='bias')
for b8 in range(1, 5):
    if b8 = = 1:
        b9 = tf.Variable([0.46918184], name=f'weight_{b8}')
    elif b8 = = 2:
        b9 = tf.Variable([1.00643885], name=f'weight_{b8}')
    elif b8 = = 3:
        b9 = tf.Variable([-0.23585591], name=f'weight_{b8}')
    elif b8 = = 4:
        b9 = tf.Variable([0.01418969], name=f'weight_{b8}')
    b7 = tf.add(tf.multiply(tf.pow(b5, b8), b9), b7)
b10 = tf.reduce_sum(tf.multiply(tf.pow(b7 - b6, 2), b4)) / (a1 - 1)
b11 = tf.train.GradientDescentOptimizer(a2).minimize(b10)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch_i in range(a3):
        for x, y, w in zip(b1, b2, b3):
            sess.run(b11, b12 = {b5: x, b6: y, b4: w})
        b13 = sess.run(b10, b12={b5: b1, b6: b2, b4: b3})
        print(f"{epoch_i} : {b13}")
        if epoch_i % b14 = = 0 and epoch_i > 100:
            b15 = np.abs(b7.eval(b12={b5: b1}, session=sess) - b2) > a4
            if not np.any(b15):
                break
            b3[b15] *= 1.1
    fig, b16 = plt.subplots(1, 1)
    b17 = np.linspace(0, 10, 1000)
    b16.plot(b17, b7.eval(b12 = {b5: b17}, session=sess), b19='red', label='CWP')
    cx, b18 = b1[3], b2[3]
    b16.plot([0, cx], [0, b18], b19 = 'blue', linestyle='dashed', label='General Path')
    b16.plot(np.concatenate([[cx], b1[3:]]), np.concatenate([[b18], b2[3:]]), b19 = 'blue', linestyle='dashed')
    b16.scatter(0.1, 0.15, b19 = 'black', marker='^', label='H-AP', s=matplotlib.rcParams['lines.markersize'] ** 2 + b14, zorder=10)
    b16.scatter(b1[:3], b2[:3], b19 = 'black', label='HGN', s=matplotlib.rcParams['lines.markersize'] ** 2 + 10, zorder=10)
    b16.scatter(b1[3:], b2[3:], b19 = 'black', marker='*', s=matplotlib.rcParams['lines.markersize'] ** 2 + b14, label='LGN', zorder=10)
    b20 = np.arange(0, 11, 1)
    b16.set_xticks(b20)
    b16.set_yticks(b20)
    b16.grid(b21 = 'both')
    b16.grid(b21 = 'minor', alpha=0.2)
    b16.grid(b21 = 'major', alpha=0.5)
    b16.set_ylim([0, 10])
    b16.set_xlim([0, 10])
    plt.xlabel('x(m)')
    plt.ylabel('y(m)')
    plt.legend(b22 = 'lower right', fontsize='small', framealpha=1)
    plt.grid(b23 = 'dashed')
    plt.savefig('test.eps', b24 = 'eps', dpi=1000)
    plt.waitforbuttonpress()
    b25 = [v.eval(session=sess) for v in tf.trainable_variables()]
    for i, wb in enumerate(b25):
        print(f"Weight/Bias {i + 1} : {wb}")