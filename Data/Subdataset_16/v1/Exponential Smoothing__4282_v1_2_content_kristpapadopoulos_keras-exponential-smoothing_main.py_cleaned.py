import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
class class1(tf.keras.layers.Layer):
    def fonk1(self, b1 = 0.01, b2=0.b20, **kwargs):
        super(class1, self).fonk1(**kwargs)
        self.b1 = b1
        self.b2 = b2
    def fonk2(self, input_shape):
        self.b3 = self.add_weight(
            b4 = (1,),
            b5 = tf.keras.initializers.Constant(0.1),
            b6 = True,
            b7 = tf.keras.constraints.MinMaxNorm(min_value=self.b1, max_value=self.b2)
        )
    def fonk3(self, inputs):
        b8 = tf.TensorArray(dtype=tf.float32, size=tf.b4(inputs)[0])
        b8 = b8.write(0, inputs[0])
        for t in range(1, tf.b4(inputs)[0]):
            b9 = b8.read(t - 1)
            b10 = self.b3 * inputs[t] + (1 - self.b3) * b9
            b8 = b8.write(t, b10)
        return b8.stack()
def fonk4(b18, b13):
    b11 = tf.losses.mean_squared_error(y_true=b13, y_pred=b18)
    return tf.reshape(b11, (1,))
if b12 = = "__main__":
    b13 = np.log(np.arange(1, 300, 3)) + np.random.normal(0, 0.4, 100)
    b14 = tf.convert_to_tensor(b13, dtype=tf.float32)
    a1 = b20
    a2 = 0.01
    b15 = tf.keras.optimizers.Adam(a2)
    b16 = []
    b17 = class1(b1=0.01, b2=0.b20)
    print('--------------------- class1 training b11 --------------------')
    for epoch in range(a1):
        with tf.GradientTape() as tape:
            b18 = b17(b14)
            b11 = fonk4(b18, b14[:-1])
        b16.append(b11.numpy())
        b19 = tape.gradient(b11, b17.trainable_weights)
        b15.apply_gradients(zip(b19, b17.trainable_weights))
        if epoch % b20 = = 0:
            print(f"MSE Loss at epoch {epoch}: {b11[0]:.3f}, b3: {b17.b3.numpy()[0]:.3f}")
    print(f"Final MSE b11: {b11[0]:.3f}")
    print(f"b3 = {b17.b3.numpy()[0]:.3f}")
    b21 = b18.numpy()
    plt.figure(b22 = (15, 8))
    plt.title('Simple exponential smoothing layer results with constrained learned parameter')
    plt.plot(range(99), b21, b23 = 'b21')
    plt.plot(range(99), b14[:-1], b23 = 'actual')
    plt.grid(True)
    plt.legend()
    plt.xlabel('time')
    plt.ylabel('amplitude')
    plt.show()