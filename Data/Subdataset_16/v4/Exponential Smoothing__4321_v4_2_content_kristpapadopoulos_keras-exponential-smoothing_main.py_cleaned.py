import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
class class1(tf.keras.layers.Layer):
    def fonk1(self, b1 = 0.01, b2=0.5, **kwargs):
        super(class1, self).fonk1(**kwargs)
        self.b1 = b1
        self.b2 = b2
    def fonk2(self, input_shape):
        self.b3 = self.add_weight(
            b4 = (b19,),
            b5 = tf.keras.initializers.Constant(0.b19),
            b6 = True,
            b7 = tf.keras.constraints.MinMaxNorm(min_value=self.b1, max_value=self.b2)
        )
    def fonk3(self, inputs):
        b8 = tf.TensorArray(dtype=tf.float32, size=tf.b4(inputs)[0])
        b8 = b8.write(0, inputs[0])
        for t in range(b19, tf.b4(inputs)[0]):
            b9 = b8.read(t - b19)
            b10 = self.b3 * inputs[t] + (b19 - self.b3) * b9
            b8 = b8.write(t, b10)
        return b8.stack()
def fonk4(b16, b11):
    return tf.reduce_mean(tf.square(b11 - b16))
def fonk5():
    b11 = np.log(np.arange(b19, 300, 3)) + np.random.normal(0, 0.4, 100)
    b12 = tf.convert_to_tensor(b11, dtype=tf.float32)
    a1 = 5
    a2 = 0.01
    b13 = tf.keras.optimizers.Adam(a2)
    b14 = []
    b15 = class1(b1=0.01, b2=0.5)
    print('--------------------- class1 Training Loss --------------------')
    for epoch in range(a1):
        with tf.GradientTape() as tape:
            b16 = b15(b12)
            b17 = fonk4(b16[:-b19], b12[:-b19])
        b14.append(b17.numpy())
        b18 = tape.gradient(b17, b15.trainable_weights)
        b13.apply_gradients(zip(b18, b15.trainable_weights))
        if epoch % b19 = = 0:
            print(f"MSE Loss at epoch {epoch}: {b17:.3f}, b3: {b15.b3.numpy()[0]:.3f}")
    print(f"Final MSE b17: {b17:.3f}")
    print(f"b20 = {b15.b3.numpy()[0]:.3f}")
    b21 = b16.numpy()
    plt.figure(b22 = (15, 8))
    plt.title('Simple Exponential Smoothing Layer Results with Constrained Learned Parameter')
    plt.plot(range(99), b21, b23 = 'Prediction')
    plt.plot(range(99), b12[:-b19], b23 = 'Actual')
    plt.grid(True)
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.show()
if b24 = = "__main__":
    fonk5()