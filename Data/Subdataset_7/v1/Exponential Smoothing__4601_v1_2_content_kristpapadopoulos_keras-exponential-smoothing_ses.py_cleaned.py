import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
class class1(tf.keras.layers.Layer):
    def fonk1(self, b2, b3, b1 = tf.float32):
        super(class1, self).fonk1()
        self.b2 = b2
        self.b3 = b3
    def fonk2(self, input_shape):
        self.b4 = self.add_weight('b4',
                                     b5 = [1,],
                                     b6 = tf.keras.initializers.random_uniform(0,1),
                                     b7 = tf.keras.regularizers.L2(0.1),
                                     b8 = tf.keras.constraints.min_max_norm(self.b2,
                                                                                  self.b3))
    def fonk3(self, b15):
        def fonk4(b14, b4, b12):
            '''Apply simple exponential smoothing'''
            b9 = b12
            b10 = b9 + b4 * (b14 - b9)
            return b9, b10
        b11 = []
        b12 = tf.reshape(b15[0], 1)
        for time_step in b15[1:]:
            prediction, b12 = fonk4(time_step, self.b4, b12)
            b11.append(prediction)
        return tf.concat(b11, -1)
if b13 = = "__main__":
    b14 = np.log(np.arange(1, 300, 3)) + np.random.normal(0, 0.4, 100)
    b15 = tf.convert_to_tensor(b14)
    b16 = class1(b2=0.01, b3=0.5)
    b17 = b16(b15).numpy()
    plt.figure(b18 = (15, 8))
    plt.title('Simple exponential smoothing layer results with constrained learned parameter')
    plt.plot(list(range(99)), b17, b19 = 'Prediction')
    plt.plot(list(range(99)), b14[1:], b19 = 'Actual')
    plt.grid(True)
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.show()