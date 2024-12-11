import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from ses import SES
def fonk1(b8, b3):
    b1 = tf.losses.mean_squared_error(y_true=b3, y_pred=b8)
    return tf.reshape(b1, 1)
if b2 = = "__main__":
    b3 = np.log(np.arange(1, 300, 3)) + np.random.normal(0, 0.4, 100)
    b4 = tf.convert_to_tensor(b3)
    a1 = b10
    a2 = 0.01
    b5 = tf.keras.optimizers.Adam(a2)
    b6 = []
    b7 = SES(min_constraint=0.01, max_constraint=0.b10)
    print('--------------------- SES training b1 --------------------')
    for epoch in range(a1):
        with tf.GradientTape() as tape:
            b8 = b7(b4)
            b1 = fonk1(b8, b4[:-1])
        b6.append(b1.numpy())
        b9 = tape.gradient(b1, b7.trainable_weights)
        b5.apply_gradients(zip(b9, b7.trainable_weights))
        if epoch % b10 = = 0:
            print("MSE Loss at epoch {}: {:.3f}, b11: {:.3f}".format(epoch, b1[0], b7.weights[0].numpy()[0]))
    print("Final MSE b1: {:.3f}".format(b1[0]))
    print("b11 = {:.3f}".format(b7.weights[0].numpy()[0]))
    b12 = b8.numpy()
    plt.figure(b13 = (15, 8))
    plt.title('Simple exponential smoothing layer results with constrained learned parameter')
    plt.plot(list(range(99)), b12, b14 = 'b12')
    plt.plot(list(range(99)), b4[:-1], b14 = 'actual')
    plt.grid(True)
    plt.legend()
    plt.xlabel('time')
    plt.ylabel('amplitude')
    plt.show()