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
            b11 = b7.weights[0].numpy()[0]
            print(f"MSE Loss at epoch {epoch}: {b1[0]:.3f}, alpha: {b11:.3f}")
    b12 = b1[0].numpy()
    b13 = b7.weights[0].numpy()[0]
    print(f"Final MSE b1: {b12:.3f}")
    print(f"Final alpha: {b13:.3f}")
    b14 = b8.numpy()
    plt.figure(b15 = (15, 8))
    plt.title('Simple exponential smoothing layer results with constrained learned parameter')
    plt.plot(list(range(99)), b14, b16 = 'Prediction')
    plt.plot(list(range(99)), b4[:-1], b16 = 'Actual')
    plt.grid(True)
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.show()