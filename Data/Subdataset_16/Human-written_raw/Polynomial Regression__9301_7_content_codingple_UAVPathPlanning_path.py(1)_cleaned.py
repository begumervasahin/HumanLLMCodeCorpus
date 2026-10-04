import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.lines as mlines
from matplotlib.patches import Circle
a1 = 10
fig, b1 = plt.subplots(1, 1)
b2 = np.array([ 1.1,  1.2,  2.7,  3.2,  4.1,
  4.8,  6.1,  7.5,  9.5,  9.8 ])
b3 = np.array([ 0.6,  2.5,  2.6,  3.8,  8.0,
  5.9,  7.5,  5.5,  7.0,  9.8 ])
b4 = np.ones(a1)
b5 = tf.placeholder(tf.float32)
a2 = 1.0
b6 = tf.placeholder(tf.float32)
b7 = tf.placeholder(tf.float32)
b8 = tf.Variable([-0.00029278], name='bias')
for b9 in range(1, 5):
    if b9 = = 1:
        b10 = tf.Variable([ 0.46918184], name='weight_%d' % b9)
    if b9 = = 2:
        b10 = tf.Variable([ 1.00643885], name='weight_%d' % b9)
    if b9 = = 3:
        b10 = tf.Variable([-0.23585591], name='weight_%d' % b9)
    if b9 = = 4:
        b10 = tf.Variable([ 0.01418969], name='weight_%d' % b9)
    b8 = tf.add(tf.multiply(tf.pow(b6, b9), b10), b8)
b11 = tf.reduce_sum(tf.multiply(tf.pow(b8 - b7, 2), b5))  /  (a1 - 1)
b12 = tf.Session()
b13 = b2[3]
b14 = b3[3]
a3 = 0.1e-8
b15 = tf.train.GradientDescentOptimizer(a3).minimize(b11)
a4 = 1
b12.run(tf.global_variables_initializer())
a5 = 0.0
for epoch_i in range(a4):
    for (x, y, w) in zip(b2, b3, b4):
        b12.run(b15, b16 = {b6: x, b7: y, b5: w})
    b17 = b12.run(
        b11, b16 = {b6: b2, b7: b3, b5: b4})
    print(str(epoch_i) + " : " + str(b17))
    if epoch_i % b18 = = 0 and epoch_i > 100:
        b19 = np.abs( b8.eval(b16={b6: testx}, session=b12) - testy ) > a2
        if True not in b19:
            break
        b4[b19] *= 1.1
    a5 = b17
b20 = np.linspace(0, 10, 1000)
b1.plot(b20, b8.eval(b16 = {b6: b20}, session=b12), b21='red', label='CWP')
b1.plot([0,b13], [0, b14], b21 = 'blue', linestyle='dashed', label='General Path')
b1.plot(np.concatenate([[b13], b2[3:]]), np.concatenate([[b14], b3[3:]]), b21 = 'blue', linestyle='dashed')
b22 = [0,0,0,0,0]
b23 = [v for v in tf.trainable_variables() if v.name == "bias:0"][0]
b22[4] = np.float32(b12.run(b23))
for b9 in range(1, 5):
    b23 = [v for v in tf.trainable_variables() if v.name == "weight_"+str(b9)+":0"][0]
    b22[(b9)-1] = np.float32(b12.run(b23))
    print("Weight" + str(b9) + " : " + str(b22[(b9)-1]))
print("bias : " + str(b22[4]))
fig.show()
plt.draw()
b1.scatter(0.1,0.15, b21 = 'black', marker='^', label='H-AP', s=matplotlib.rcParams['lines.markersize'] ** 2 + b18, zorder=10)
b1.scatter(b2[:3], b3[:3], b21 = 'black', label='HGN', s=matplotlib.rcParams['lines.markersize'] ** 2 + 10, zorder=10)
b1.scatter(b2[3:], b3[3:], b21 = 'black', marker='*', s=matplotlib.rcParams['lines.markersize'] ** 2 + b18, label='LGN', zorder=10)
b24 = np.arange(0, 11, 1)
b1.set_xticks(b24)
b1.set_yticks(b24)
b1.grid(b25 = 'both')
b1.grid(b25 = 'minor', alpha=0.2)
b1.grid(b25 = 'major', alpha=0.5)
b1.set_ylim([0, 10])
b1.set_xlim([0, 10])
plt.xlabel('x(m)')
plt.ylabel('y(m)')
plt.legend(b26 = 'lower right', fontsize='small', framealpha=1)
plt.grid(b27 = 'dashed')
plt.savefig('test.eps', b28 = 'eps', dpi=1000)
plt.waitforbuttonpress()