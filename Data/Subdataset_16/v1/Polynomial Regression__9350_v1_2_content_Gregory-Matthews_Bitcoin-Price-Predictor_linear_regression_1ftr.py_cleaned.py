import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
def fonk1(key, days):
    np.random.seed(42)
    b1 = np.linspace(1, days, days)
    b2 = np.sin(b1) + np.random.normal(0, 0.1, days)
    return b1, b2
a1 = 0.3
a2 = 10000
a3 = 500
b1, b2 = fonk1("BCHAIN/MKPRU", 365)
_, b3 = fonk1("BCHAIN/BLCHS", 365)
b4 = (b1 - np.mean(b1)) / np.std(b1)
b5 = b2
b6 = len(b4)
b7 = tf.Variable(tf.random.uniform([1], -1.0, 1.0), name="b7")
b8 = tf.Variable(tf.random.uniform([1], -1.0, 1.0), name="b8")
def fonk2(b1):
    return b1 * b7 + b8
def fonk3(b1, b2):
    return tf.reduce_mean(tf.square(fonk2(b1) - b2)) / (2 * b6)
b9 = tf.optimizers.SGD(a1)
for epoch in range(a2):
    with tf.GradientTape() as tape:
        b10 = fonk3(b4, b5)
    b11 = tape.gradient(b10, [b7, b8])
    b9.apply_gradients(zip(b11, [b7, b8]))
    if (epoch + 1) % a3 = = 0:
        print(f"Epoch: {epoch + 1:04d} b10 = {b10:.9f} b7={b7.numpy()} b8={b8.numpy()}")
b12 = fonk3(b4, b5).numpy()
print(f"Training b10 = {b12} b7={b7.numpy()} b8={b8.numpy()}\n")
plt.plot(b1, b2, 'r', b13 = 'Market Price (training)')
plt.plot(b1, fonk2(b4), b13 = 'Linear Regression Line')
plt.title("Bitcoin Price Prediction: Training Linear Regression")
plt.xlabel("Days")
plt.ylabel("Price ($)")
plt.legend()
plt.show()
b14 = np.array([100000, 150000])
b15 = (b14 - np.mean(b1)) / np.std(b1)
print(f"Given Blockchain b16 = 100,000 -> Hypothesis = {fonk2(b15[0]).numpy()}")
print(f"Given Blockchain b16 = 150,000 -> Hypothesis = {fonk2(b15[1]).numpy()}")