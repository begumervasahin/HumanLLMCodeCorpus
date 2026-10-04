import tensorflow as tf
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
    def fonk3(self, timeseries):
        def fonk4(y, b4, b12):
            '''Apply simple exponential smoothing'''
            b9 = b12
            b10 = b9 + b4 * (y - b9)
            return b9, b10
        b11 = []
        b12 = tf.reshape(timeseries[0], 1)
        for time_step in timeseries[1:]:
            prediction, b12 = fonk4(time_step, self.b4, b12)
            b11.append(prediction)
        return tf.concat(b11, -1)