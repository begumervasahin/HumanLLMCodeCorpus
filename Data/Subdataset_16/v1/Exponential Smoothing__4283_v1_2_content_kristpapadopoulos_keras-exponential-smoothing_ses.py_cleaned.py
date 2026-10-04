import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
class class1(tf.keras.layers.Layer):
    def fonk1(self, b2, b3, b1 = tf.float32):
        super(class1, self).fonk1()
        self.b2 = b2
        self.b3 = b3
    def fonk2(self, input_shape):
        self.b4 = self.add_weight('b4',
                                     b5 = [1,],
                                     b6 = tf.keras.initializers.RandomUniform(0, 1),
                                     b7 = tf.keras.regularizers.L2(0.1),
                                     b8 = tf.keras.constraints.MinMaxNorm(self.b2,
                                                                                self.b3))
    def fonk3(self, b14):
        def fonk4(b13, b4, b12):
            '''Apply simple exponential smoothing'''
            b9 = b12
            b10 = b9 + b4 * (b13 - b9)
            return b9, b10
        b11 = []
        b12 = tf.reshape(b14[0], 1)
        for time_step in b14[1:]:
            b18, b12 = fonk4(time_step, self.b4, b12)
            b11.append(b18)
        return tf.concat(b11, -1)
def fonk5(b18, b13):
    return tf.reduce_mean(tf.square(b13 - b18))
def fonk6():
    b13 = np.log(np.arange(1, 300, 3)) + np.random.normal(0, 0.4, 100)
    b14 = tf.convert_to_tensor(b13, b1=tf.float32)
    a1 = 5
    a2 = 0.01
    b15 = tf.keras.optimizers.Adam(a2)
    b16 = []
    b17 = class1(b2=0.01, b3=0.5)
    print('--------------------- class1 Training Loss --------------------')
    for epoch in range(a1):
        with tf.GradientTape() as tape:
            b18 = b17(b14)
            b19 = fonk5(b18[:-1], b14[:-1])
        b16.append(b19.numpy())
        b20 = tape.gradient(b19, b17.trainable_weights)
        b15.apply_gradients(zip(b20, b17.trainable_weights))
        print(f"MSE Loss at epoch {epoch}: {b19:.3f}, b4: {b17.b4.numpy()[0]:.3f}")
    print(f"Final MSE b19: {b19:.3f}")
    print(f"b21 = {b17.b4.numpy()[0]:.3f}")
    b22 = b18.numpy()
    plt.figure(b23 = (15, 8))
    plt.title('Simple Exponential Smoothing Layer Results with Constrained Learned Parameter')
    plt.plot(range(99), b22, b24 = 'Prediction')
    plt.plot(range(99), b14[:-1], b24 = 'Actual')
    plt.grid(True)
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.show()
if b25 = = "__main__":
    fonk6()