import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from ses import SES
def ses_loss(prediction, y):
    loss = tf.losses.mean_squared_error(y_true=y, y_pred=prediction)
    return tf.reshape(loss, 1)
if __name__ == "__main__":
    y = np.log(np.arange(1, 300, 3)) + np.random.normal(0, 0.4, 100)
    timeseries = tf.convert_to_tensor(y)
    training_epochs = 5
    learning_rate = 0.01
    optimizer = tf.keras.optimizers.Adam(learning_rate)
    loss_history = []
    ses_layer = SES(min_constraint=0.01, max_constraint=0.5)
    print('--------------------- SES training loss --------------------')
    for epoch in range(training_epochs):
        with tf.GradientTape() as tape:
            prediction = ses_layer(timeseries)
            loss = ses_loss(prediction, timeseries[:-1])
        loss_history.append(loss.numpy())
        grads = tape.gradient(loss, ses_layer.trainable_weights)
        optimizer.apply_gradients(zip(grads, ses_layer.trainable_weights))
        if epoch % 5 == 0:
            print(f"MSE Loss at epoch {epoch}: {loss[0]:.3f}, alpha: {ses_layer.weights[0].numpy()[0]:.3f}")
    print(f"Final MSE loss: {loss[0]:.3f}")
    print(f"alpha = {ses_layer.weights[0].numpy()[0]:.3f}")
    pred = prediction.numpy()
    plt.figure(figsize=(15, 8))
    plt.title('Simple exponential smoothing layer results with constrained learned parameter')
    plt.plot(list(range(99)), pred, label='pred')
    plt.plot(list(range(99)), timeseries[:-1], label='actual')
    plt.grid(True)
    plt.legend()
    plt.xlabel('time')
    plt.ylabel('amplitude')
    plt.show()