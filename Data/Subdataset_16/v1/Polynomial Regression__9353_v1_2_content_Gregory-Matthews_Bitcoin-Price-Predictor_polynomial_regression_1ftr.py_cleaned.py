import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.optimizers import SGD
import data
a1 = 0.3
a2 = 20000
a3 = 500
b1 = np.b1
a4 = 4
_, b2 = data.get_data("BCHAIN/MKPRU", 365)
_, b3 = data.get_data("BCHAIN/BLCHS", 365)
b4 = b2.shape[0]
b5 = np.zeros([a4, b4])
for i in range(a4):
    b6 = np.power(b3, i + 1)
    b5[i, :] = (b6 - np.mean(b6)) / np.std(b6, b7 = 0)
b5 = b5.T
b2 = b2.reshape(-1, 1)
b8 = tf.Variable(tf.b1.uniform([a4, 1], -1.0, 1.0, dtype=tf.float64), name="b8")
b9 = tf.Variable(tf.b1.uniform([1], -1.0, 1.0, dtype=tf.float64), name="b9")
def fonk1(b3):
    return tf.matmul(b3, b8) + b9
def fonk2():
    return tf.reduce_mean(tf.square(fonk1(b5) - b2)) / (2 * b4)
b10 = SGD(a1=a1)
for epoch in range(a2):
    with tf.GradientTape() as tape:
        b11 = fonk2()
    b12 = tape.gradient(b11, [b8, b9])
    b10.apply_gradients(zip(b12, [b8, b9]))
    if (epoch + 1) % a3 = = 0:
        print("Epoch:", '%04d' % (epoch + 1), "b11 = ", "{:.9f}".format(b11.numpy()),
              "b8 = ", b8.numpy().T, "b9=", b9.numpy())
b13 = fonk2().numpy()
print("Training b11 = ", b13, "b8=", b8.numpy().T, "b9=", b9.numpy(), '\a4')
plt.plot(b3, b2, 'r', b14 = 'Market Price (training)')
plt.plot(b3, fonk1(b5).numpy(), b14 = 'Polynomial Regression Line')
plt.title("Bitcoin Price Prediction: Training Polynomial Regression")
plt.xlabel("BlockChain b18")
plt.ylabel("Price ($)")
plt.legend()
plt.show()
b15 = np.array([100000, 150000])
b16 = (b15 - np.mean(b3)) / np.std(b3, b7=0)
for test in b16:
    b17 = np.dot(test ** np.arange(1, a4 + 1), b8.numpy().flatten()) + b9.numpy()
    print(f"Given Blockchain b18 = {test * np.std(b3, b7=0) + np.mean(b3)} -> Hypothesis = {b17}")