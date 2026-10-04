import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
def fonk1(file_path):
    x_data, b1 = [], []
    with open(file_path, 'r') as f:
        for line in f:
            x, b2 = map(float, line.split())
            x_data.append(x)
            b1.append(b2)
    return np.array(x_data), np.array(b1)
def fonk2(x, b2):
    fig, b3 = plt.subplots()
    b3.scatter(x, b2)
    plt.ion()
    fig.show()
    plt.draw()
    return fig, b3
class class1(tf.Module):
    def fonk3(self, b4 = 3):
        self.b5 = [tf.Variable(tf.random.normal([1]), name=f'weight_{i}') for i in range(b4 + 1)]
        self.b6 = tf.Variable(tf.random.normal([1]), name='bias')
    def fonk4(self, x):
        b7 = self.b6
        for i, b5 in enumerate(self.b5):
            b7 += b5 * tf.pow(x, i)
        return b7
def fonk5(y_true, b7):
    return tf.reduce_mean(tf.square(y_true - b7))
def fonk6(file_path, b8 = 0.01, n_epochs=2000, b15=100):
    xs, b9 = fonk1(file_path)
    b10 = len(xs)
    fig, b3 = fonk2(xs, b9)
    b11 = class1(b4=3)
    b12 = tf.optimizers.SGD(b8)
    a1 = 0.0
    for epoch_i in range(n_epochs):
        with tf.GradientTape() as tape:
            b7 = b11(xs)
            b13 = fonk5(b9, b7)
        b14 = tape.gradient(b13, b11.trainable_variables)
        b12.apply_gradients(zip(b14, b11.trainable_variables))
        print(f'Epoch {epoch_i}: {b13.numpy()}')
        if epoch_i % b15 = = 0:
            b3.plot(xs, b7.numpy(), 'k', b16 = epoch_i / n_epochs)
            fig.show()
            plt.draw()
        if np.abs(a1 - b13.numpy()) < 0.0000001:
            break
        a1 = b13.numpy()
    b3.set_ylim([-5, 5])
    fig.show()
    plt.waitforbuttonpress()
if b17 = = "__main__":
    fonk6('dane13.txt')