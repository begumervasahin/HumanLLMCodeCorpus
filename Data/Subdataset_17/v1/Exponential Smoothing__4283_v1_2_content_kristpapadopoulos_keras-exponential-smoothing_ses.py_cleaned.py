import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
class SES(tf.keras.layers.Layer):
    def __init__(self, min_constraint, max_constraint, dtype=tf.float32):
        super(SES, self).__init__()
        self.min_constraint = min_constraint
        self.max_constraint = max_constraint
    def build(self, input_shape):
        self.alpha = self.add_weight('alpha',
                                     shape=[1,],
                                     initializer=tf.keras.initializers.RandomUniform(0, 1),
                                     regularizer=tf.keras.regularizers.L2(0.1),
                                     constraint=tf.keras.constraints.MinMaxNorm(self.min_constraint,
                                                                                self.max_constraint))
    def call(self, timeseries):
        def ses(y, alpha, level):
            '''Apply simple exponential smoothing'''
            forecast = level
            updated_level = forecast + alpha * (y - forecast)
            return forecast, updated_level
        predictions = []
        level = tf.reshape(timeseries[0], 1)
        for time_step in timeseries[1:]:
            prediction, level = ses(time_step, self.alpha, level)
            predictions.append(prediction)
        return tf.concat(predictions, -1)
def ses_loss(prediction, y):
    return tf.reduce_mean(tf.square(y - prediction))
def main():
    y = np.log(np.arange(1, 300, 3)) + np.random.normal(0, 0.4, 100)
    timeseries = tf.convert_to_tensor(y, dtype=tf.float32)
    training_epochs = 5
    learning_rate = 0.01
    optimizer = tf.keras.optimizers.Adam(learning_rate)
    loss_history = []
    ses_layer = SES(min_constraint=0.01, max_constraint=0.5)
    print('--------------------- SES Training Loss --------------------')
    for epoch in range(training_epochs):
        with tf.GradientTape() as tape:
            prediction = ses_layer(timeseries)
            loss = ses_loss(prediction[:-1], timeseries[:-1])
        loss_history.append(loss.numpy())
        grads = tape.gradient(loss, ses_layer.trainable_weights)
        optimizer.apply_gradients(zip(grads, ses_layer.trainable_weights))
        print(f"MSE Loss at epoch {epoch}: {loss:.3f}, alpha: {ses_layer.alpha.numpy()[0]:.3f}")
    print(f"Final MSE loss: {loss:.3f}")
    print(f"Alpha = {ses_layer.alpha.numpy()[0]:.3f}")
    pred = prediction.numpy()
    plt.figure(figsize=(15, 8))
    plt.title('Simple Exponential Smoothing Layer Results with Constrained Learned Parameter')
    plt.plot(range(99), pred, label='Prediction')
    plt.plot(range(99), timeseries[:-1], label='Actual')
    plt.grid(True)
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.show()
if __name__ == "__main__":
    main()