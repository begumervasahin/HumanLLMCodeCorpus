import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
class class1(tf.keras.layers.Layer):
    def fonk1(self, b1 = 0.01, b2=0.5, dtype=tf.float32):
        super(class1, self).fonk1()
        self.b1 = b1
        self.b2 = b2
    def fonk2(self, input_shape):
        self.b3 = self.add_weight('b3',
                                     b4 = [1,],
                                     b5 = tf.keras.initializers.RandomUniform(minval=0, maxval=1),
                                     b6 = tf.keras.regularizers.L2(0.1),
                                     b7 = tf.keras.constraints.MinMaxNorm(min_value=self.b1,
                                                                                 b8 = self.b2))
    def fonk3(self, b16):
        def fonk4(b15, b3, b12):
            b9 = b12
            b10 = b9 + b3 * (b15 - b9)
            return b9, b10
        b11 = []
        b12 = tf.reshape(b16[0], b4=(1,))
        for time_step in b16[1:]:
            prediction, b12 = fonk4(time_step, self.b3, b12)
            b11.append(prediction)
        return tf.concat(b11, b13 = -1)
if b14 = = "__main__":
    b15 = np.log(np.arange(1, 300, 3)) + np.random.normal(0, 0.4, 100)
    b16 = tf.convert_to_tensor(b15)
    b17 = class1()
    b18 = b17(b16).numpy()
    plt.figure(b19 = (15, 8))
    plt.title('Simple Exponential Smoothing with Constrained Alpha Parameter')
    plt.plot(np.arange(1, 100), b18, b20 = 'Prediction')
    plt.plot(np.arange(1, 100), b15[1:], b20 = 'Actual')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.legend()
    plt.show()