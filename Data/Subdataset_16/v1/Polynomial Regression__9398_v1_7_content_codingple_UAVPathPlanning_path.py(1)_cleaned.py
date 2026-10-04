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
b7 = tf.Variable([-0.00029278], name='bias')
for pow_i in range(1, 5):
    b8 = tf.Variable([0.46918184, 1.00643885, -0.23585591, 0.01418969][pow_i-1], name='weight_%d' % pow_i)
    b7 = tf.add(tf.multiply(tf.pow(b4, pow_i), b8), b7)
b9 = tf.reduce_sum(tf.multiply(tf.pow(b7 - b5, 2), b6)) / (a1 - 1)
b10 = tf.train.GradientDescentOptimizer(learning_rate=0.1e-8).minimize(b9)
b11 = tf.Session()
b11.run(tf.global_variables_initializer())
a2 = 1
a3 = 0.0
for epoch_i in range(a2):
    for (x, y, w) in zip(b1, b2, b3):
        b11.run(b10, b12 = {b4: x, b5: y, b6: w})
    b13 = b11.run(b9, b12={b4: b1, b5: b2, b6: b3})
    print(str(epoch_i) + " : " + str(b13))
    a3 = b13
fig, b14 = plt.subplots(1, 1)
b15 = np.linspace(0, 10, 1000)
b16 = [b11.run(b7, b12={b4: x}) for x in b15]
b14.plot(b15, b16, b17 = 'red', label='CWP')
cx, b18 = b1[3], b2[3]
b14.plot([0, cx], [0, b18], b17 = 'blue', linestyle='dashed', label='General Path')
b14.plot(np.concatenate([[cx], b1[3:]]), np.concatenate([[b18], b2[3:]]), b17 = 'blue', linestyle='dashed')
b14.scatter(0.1, 0.15, b17 = 'black', marker='^', label='H-AP', s=matplotlib.rcParams['lines.markersize'] ** 2 + 50, zorder=10)
b14.scatter(b1[:3], b2[:3], b17 = 'black', label='HGN', s=matplotlib.rcParams['lines.markersize'] ** 2 + 10, zorder=10)
b14.scatter(b1[3:], b2[3:], b17 = 'black', marker='*', s=matplotlib.rcParams['lines.markersize'] ** 2 + 50, label='LGN', zorder=10)
b19 = np.arange(0, 11, 1)
b14.set_xticks(b19)
b14.set_yticks(b19)
b14.grid(b20 = 'both')
b14.grid(b20 = 'minor', alpha=0.2)
b14.grid(b20 = 'major', alpha=0.5)
b14.set_ylim([0, 10])
b14.set_xlim([0, 10])
plt.xlabel('x(m)')
plt.ylabel('y(m)')
plt.legend(b21 = 'lower right', fontsize='small', framealpha=1)
plt.grid(b22 = 'dashed')
plt.savefig('test.eps', b23 = 'eps', dpi=1000)
plt.show()
b24 = [b11.run(var) for var in tf.trainable_variables()]
print("Weights and bias:", b24)