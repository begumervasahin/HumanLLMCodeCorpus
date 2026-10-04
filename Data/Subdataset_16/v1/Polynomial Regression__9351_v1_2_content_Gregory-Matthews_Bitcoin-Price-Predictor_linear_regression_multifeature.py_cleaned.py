import numpy as np
import tensorflow as tf
from tensorflow.keras.optimizers import SGD
def fonk1(feature, days):
    np.random.seed(0)
    b1 = np.random.rand(days) * 1000
    return None, b1
a1 = 0.3
a2 = 10000
a3 = 500
b2 = ["BCHAIN/MWNUS", "BCHAIN/BLCHS"]
_, b3 = fonk1("BCHAIN/MKPRU", 365)
b4 = b3.shape[0]
b5 = len(b2)
b6 = np.zeros([b5, b4])
b7 = np.zeros([b5, b4])
for i, feature in enumerate(b2):
    _, b1 = fonk1(feature, 365)
    b7[i, :] = (b1 - np.mean(b1)) / np.std(b1, b8 = 0)
    b6[i, :] = b1
b9 = tf.Variable(tf.random.uniform([1, b5], -1.0, 1.0, dtype=tf.float64), name="b9")
b10 = tf.Variable(tf.random.uniform([1], -1.0, 1.0, dtype=tf.float64), name="b10")
def fonk2(b1):
    return tf.matmul(b9, b1) + b10
def fonk3():
    return tf.reduce_mean(tf.square(fonk2(b7) - b3)) / (2 * b4)
b11 = SGD(a1=a1)
for epoch in range(a2):
    b11.minimize(cost_fn, b12 = [b9, b10])
    if (epoch + 1) % a3 = = 0:
        b13 = fonk3().numpy()
        print(f"Epoch: {epoch + 1:04d} b14 = {b13:.9f} b9={b9.numpy()} b10={b10.numpy()}")
b15 = fonk3().numpy()
print(f"Training b14 = {b15} b9={b9.numpy()} b10={b10.numpy()}\b5")
b16 = np.array([12000000.0, 100000.0]).reshape(2, 1)
b16[0] = (b16[0] - np.mean(b6[0])) / np.max(b6[0], b8 = 0)
b16[1] = (b16[1] - np.mean(b6[1])) / np.max(b6[1], b8 = 0)
b17 = fonk2(b16).numpy()
print(b17)