import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.optimizers import SGD
import data
a1 = 0.3
a2 = 20000
a3 = 500
a4 = 4
_, b1 = data.get_data("BCHAIN/MKPRU", 365)
_, b2 = data.get_data("BCHAIN/BLCHS", 365)
b3 = b1.shape[0]
b4 = np.zeros((b3, a4))
for i in range(a4):
    b5 = np.power(b2, i + 1)
    b4[:, i] = (b5 - np.mean(b5)) / np.std(b5, b6 = 0)
b1 = b1.reshape(-1, 1)
b7 = tf.Variable(tf.random.uniform([a4, 1], -1.0, 1.0, dtype=tf.float64), name="b7")
b8 = tf.Variable(tf.random.uniform([1], -1.0, 1.0, dtype=tf.float64), name="b8")
def fonk1(b2):
    return tf.matmul(b2, b7) + b8
def fonk2():
    return tf.reduce_mean(tf.square(fonk1(b4) - b1)) / (2 * b3)
b9 = SGD(a1=a1)
for epoch in range(a2):
    with tf.GradientTape() as tape:
        b10 = fonk2()
    b11 = tape.gradient(b10, [b7, b8])
    b9.apply_gradients(zip(b11, [b7, b8]))
    if (epoch + 1) % a3 = = 0:
        print(f"Epoch: {epoch + 1:04d}, b10 = {b10.numpy():.9f}, b7={b7.numpy().T}, b8={b8.numpy()}")
b12 = fonk2().numpy()
print(f"Training b10 = {b12}, b7={b7.numpy().T}, b8={b8.numpy()}\n")
plt.plot(b2, b1, 'r', b13 = 'Market Price (training)')
plt.plot(b2, fonk1(b4).numpy(), b13 = 'Polynomial Regression Line')
plt.title("Bitcoin Price Prediction: Training Polynomial Regression")
plt.xlabel("BlockChain b19")
plt.ylabel("Price ($)")
plt.legend()
plt.show()
b14 = np.array([100000, 150000])
b15 = (b14 - np.mean(b2)) / np.std(b2, b6=0)
for test_value in b15:
    b16 = np.array([test_value ** i for i in range(1, a4 + 1)])
    b17 = np.dot(b16, b7.numpy().flatten()) + b8.numpy()
    b18 = test_value * np.std(b2, b6=0) + np.mean(b2)
    print(f"Given Blockchain b19 = {b18} -> Hypothesis = {b17}")