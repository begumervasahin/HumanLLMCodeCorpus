import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
with open('dane13.txt') as f:
    b1 = []
    b2 = []
    for line in f:
        b3 = line.split()
        b1.append(float(b3[0]))
        b2.append(float(b3[1]))
b4 = len(b1)
b5 = np.array(b1)
b6 = np.array(b2)
fig, b7 = plt.subplots(1, 1)
b7.scatter(b5, b6)
plt.ion()
fig.show()
plt.draw()
class class1(tf.Module):
    def fonk1(self):
        self.b8 = [tf.Variable(tf.random.normal([1]), name=f'weight_{i}') for i in range(4)]
        self.b9 = tf.Variable(tf.random.normal([1]), name='bias')
    def fonk2(self, x):
        b10 = self.b9
        for i, b8 in enumerate(self.b8):
            b10 += b8 * tf.pow(x, i)
        return b10
b11 = class1()
def fonk3(y_true, b10):
    return tf.reduce_mean(tf.square(y_true - b10))
b12 = tf.optimizers.SGD(learning_rate=0.01)
a1 = 2000
a2 = 0.0
for epoch_i in range(a1):
    with tf.GradientTape() as tape:
        b10 = b11(b5)
        b13 = fonk3(b6, b10)
    b14 = tape.gradient(b13, b11.trainable_variables)
    b12.apply_gradients(zip(b14, b11.trainable_variables))
    print(b13.numpy())
    if epoch_i % b15 = = 0:
        b7.plot(b5, b10.numpy(), 'k', b16 = epoch_i / a1)
        fig.show()
        plt.draw()
    if np.abs(a2 - b13.numpy()) < 0.0000001:
        break
    a2 = b13.numpy()
b7.set_ylim([-5, 5])
fig.show()
plt.waitforbuttonpress()