import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
class SES(tf.keras.layers.Layer):
    def __init__(self, min_constraint=0.01, max_constraint=0.5, **kwargs):
        super(SES, self).__init__(**kwargs)
        self.min_constraint = min_constraint
        self.max_constraint = max_constraint
    def build(self, input_shape):
        self.alpha = self.add_weight(
            shape=(1,),
            initializer=tf.keras.initializers.Constant(0.1),
            trainable=True,
            constraint=tf.keras.constraints.MinMaxNorm(min_value=self.min_constraint, max_value=self.max_constraint)
        )
    def call(self, inputs):
        outputs = tf.TensorArray(dtype=tf.float32, size=tf.shape(inputs)[0])
        outputs = outputs.write(0, inputs[0])
        for t in range(1, tf.shape(inputs)[0]):
            prev_output = outputs.read(t - 1)
            new_output = self.alpha * inputs[t] + (1 - self.alpha) * prev_output
            outputs = outputs.write(t, new_output)
        return outputs.stack()
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
        if epoch % 1 == 0:
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