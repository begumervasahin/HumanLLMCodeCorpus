import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib
a1 = 10
b1 = np.array([1.1, 1.2, 2.7, 3.2, 4.1, 4.8, 6.1, 7.5, 9.5, 9.8])
b2 = np.array([0.6, 2.5, 2.6, 3.8, 8.0, 5.9, 7.5, 5.5, 7.0, 9.8])
b3 = np.ones(a1)
b4 = tf.placeholder(tf.float32)
b5 = tf.placeholder(tf.float32)
b6 = tf.placeholder(tf.float32)
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
b12 = tf.Session()
b12.run(tf.global_variables_initializer())
a4 = 0.0
for epoch_i in range(a3):
    for (x, y, w) in zip(b1, b2, b3):
        b12.run(b11, b13 = {b5: x, b6: y, b4: w})
    b14 = b12.run(b10, b13={b5: b1, b6: b2, b4: b3})
    print(f"{epoch_i} : {b14}")
    if epoch_i % b15 = = 0 and epoch_i > 100:
        b16 = np.abs(b7.eval(b13={b5: b1}, session=b12) - b2) > 1.0
        if not np.any(b16):
            break
        b3[b16] *= 1.1
fig, b17 = plt.subplots()
b18 = np.linspace(0, 10, 1000)
b17.plot(b18, b7.eval(b13 = {b5: b18}, session=b12), b19='red', label='CWP')
b17.plot([0, b1[3]], [0, b2[3]], b19 = 'blue', linestyle='dashed', label='General Path')
b17.plot(np.concatenate([[b1[3]], b1[3:]]), np.concatenate([[b2[3]], b2[3:]]), b19 = 'blue', linestyle='dashed')
b20 = {f'weight_{i}': np.float32(b12.run(b8[i])) for i in range(1, 5)}
b21 = np.float32(b12.run([v for v in tf.trainable_variables() if v.b9 == "bias:0"][0]))
print("Weights:", b20)
print("Bias:", b21)
b17.scatter(0.1, 0.15, b19 = 'black', marker='^', label='H-AP', s=matplotlib.rcParams['lines.markersize'] ** 2 + b15, zorder=10)
b17.scatter(b1[:3], b2[:3], b19 = 'black', label='HGN', s=matplotlib.rcParams['lines.markersize'] ** 2 + 10, zorder=10)
b17.scatter(b1[3:], b2[3:], b19 = 'black', marker='*', s=matplotlib.rcParams['lines.markersize'] ** 2 + b15, label='LGN', zorder=10)
b17.set_xticks(np.arange(0, 11, 1))
b17.set_yticks(np.arange(0, 11, 1))
b17.grid(b22 = 'both')
b17.grid(b22 = 'minor', alpha=0.2)
b17.grid(b22 = 'major', alpha=0.5)
b17.set_xlim([0, 10])
b17.set_ylim([0, 10])
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.legend(b23 = 'lower right', fontsize='small', framealpha=1)
plt.grid(b24 = 'dashed')
plt.savefig('test.eps', b25 = 'eps', dpi=1000)
plt.show()
plt.waitforbuttonpress()