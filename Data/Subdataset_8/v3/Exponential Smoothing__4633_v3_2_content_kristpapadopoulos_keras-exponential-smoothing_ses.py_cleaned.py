import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
class SES(tf.keras.layers.Layer):
    def __init__(self, min_constraint=0.01, max_constraint=0.5, dtype=tf.float32):
        super(SES, self).__init__()
        self.min_constraint = min_constraint
        self.max_constraint = max_constraint
    def build(self, input_shape):
        self.alpha = self.add_weight('alpha',
                                     shape=[1,],
                                     initializer=tf.keras.initializers.RandomUniform(minval=0, maxval=1),
                                     regularizer=tf.keras.regularizers.L2(0.1),
                                     constraint=tf.keras.constraints.MinMaxNorm(min_value=self.min_constraint,
                                                                                 max_value=self.max_constraint))
    def call(self, timeseries):
        def ses(y, alpha, level):
            forecast = level
            updated_level = forecast + alpha * (y - forecast)
            return forecast, updated_level
        predictions = []
        level = tf.reshape(timeseries[0], shape=(1,))
        for time_step in timeseries[1:]:
            prediction, level = ses(time_step, self.alpha, level)
            predictions.append(prediction)
        return tf.concat(predictions, axis=-1)
if __name__ == "__main__":
    y = np.log(np.arange(1, 300, 3)) + np.random.normal(0, 0.4, 100)
    timeseries = tf.convert_to_tensor(y)
    ses_layer = SES()
    pred = ses_layer(timeseries).numpy()
    plt.figure(figsize=(15, 8))
    plt.title('Simple Exponential Smoothing with Constrained Alpha Parameter')
    plt.plot(np.arange(1, 100), pred, label='Prediction')
    plt.plot(np.arange(1, 100), y[1:], label='Actual')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.legend()
    plt.show()