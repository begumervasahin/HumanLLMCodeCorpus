import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
with open('dane13.txt') as f:
    x_rows = []
    y_rows = []
    for line in f:
        row = line.split()
        x_rows.append(float(row[0]))
        y_rows.append(float(row[1]))
n_observations = len(x_rows)
xs = np.array(x_rows)
ys = np.array(y_rows)
fig, ax = plt.subplots(1, 1)
ax.scatter(xs, ys)
plt.ion()
fig.show()
plt.draw()
class PolynomialModel(tf.Module):
    def __init__(self):
        self.W = [tf.Variable(tf.random.normal([1]), name=f'weight_{i}') for i in range(4)]
        self.b = tf.Variable(tf.random.normal([1]), name='bias')
    def __call__(self, x):
        y_pred = self.b
        for i, W in enumerate(self.W):
            y_pred += W * tf.pow(x, i)
        return y_pred
model = PolynomialModel()
def loss(y_true, y_pred):
    return tf.reduce_mean(tf.square(y_true - y_pred))
optimizer = tf.optimizers.SGD(learning_rate=0.01)
n_epochs = 2000
prev_training_cost = 0.0
for epoch_i in range(n_epochs):
    with tf.GradientTape() as tape:
        y_pred = model(xs)
        current_loss = loss(ys, y_pred)
    grads = tape.gradient(current_loss, model.trainable_variables)
    optimizer.apply_gradients(zip(grads, model.trainable_variables))
    print(current_loss.numpy())
    if epoch_i % 100 == 0:
        ax.plot(xs, y_pred.numpy(), 'k', alpha=epoch_i / n_epochs)
        fig.show()
        plt.draw()
    if np.abs(prev_training_cost - current_loss.numpy()) < 0.0000001:
        break
    prev_training_cost = current_loss.numpy()
ax.set_ylim([-5, 5])
fig.show()
plt.waitforbuttonpress()