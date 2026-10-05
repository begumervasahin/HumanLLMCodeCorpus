import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
class SES(tf.keras.layers.Layer):
    def __init__(self, min_constraint, max_constraint, dtype=tf.float32):
        super(SES, self).__init__()
        self.min_constraint = min_constraint
        self.max_constraint = max_constraint
    def build(self, input_shape):
        self.alpha = self.add_weight('alpha',
                                     shape=[1,],
                                     initializer=tf.keras.initializers.random_uniform(0,1),
                                     regularizer=tf.keras.regularizers.L2(0.1),
                                     constraint=tf.keras.constraints.min_max_norm(self.min_constraint,
                                                                                  self.max_constraint))
    def call(self, timeseries):
        def ses(y, alpha, level):
            forecast = level
            updated_level = forecast + alpha * (y - forecast)
            return forecast, updated_level
        predictions = []
        level = tf.reshape(timeseries[0], 1)
        for time_step in timeseries[1:]:
            prediction, level = ses(time_step, self.alpha, level)
            predictions.append(prediction)
        return tf.concat(predictions, -1)
if __name__ == "__main__":
    y = np.log(np.arange(1, 300, 3)) + np.random.normal(0, 0.4, 100)
    timeseries = tf.convert_to_tensor(y)
    ses_layer = SES(min_constraint=0.01, max_constraint=0.5)
    pred = ses_layer(timeseries).numpy()
    plt.figure(figsize=(15, 8))
    plt.title('Simple exponential smoothing layer results with constrained learned parameter')
    plt.plot(list(range(99)), pred, label='Prediction')
    plt.plot(list(range(99)), y[1:], label='Actual')
    plt.grid(True)
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.show()