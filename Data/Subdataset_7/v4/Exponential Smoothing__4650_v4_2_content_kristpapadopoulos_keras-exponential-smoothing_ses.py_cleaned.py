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
                                     b8 = tf.keras.constraints.MinMaxNorm(min_value=self.b2,
                                                                                 b9 = self.b3))
    def fonk3(self, timeseries):
        def fonk4(y, b4, b13):
            '''Apply simple exponential smoothing'''
            b10 = b13
            b11 = b10 + b4 * (y - b10)
            return b10, b11
        b12 = []
        b13 = tf.reshape(timeseries[0], b5=(1,))
        for time_step in timeseries[1:]:
            prediction, b13 = fonk4(time_step, self.b4, b13)
            b12.append(prediction)
        return tf.concat(b12, b14 = -1)