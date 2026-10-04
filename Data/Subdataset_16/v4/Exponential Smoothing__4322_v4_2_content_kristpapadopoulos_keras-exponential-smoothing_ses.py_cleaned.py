import tensorflow as tf
class class1(tf.keras.layers.Layer):
    def fonk1(self, b1 = 0.01, b2=0.5, **kwargs):
        super(class1, self).fonk1(**kwargs)
        self.b1 = b1
        self.b2 = b2
    def fonk2(self, input_shape):
        self.b3 = self.add_weight(
            b4 = 'b3',
            b5 = (1,),
            b6 = tf.keras.initializers.RandomUniform(0, 1),
            b7 = tf.keras.regularizers.L2(0.1),
            b8 = tf.keras.constraints.MinMaxNorm(
                b9 = self.b1,
                b10 = self.b2
            )
        )
    def fonk3(self, inputs):
        def fonk4(b16, b3, b14):
            b11 = b14
            b12 = b11 + b3 * (b16 - b11)
            return b11, b12
        b13 = []
        b14 = tf.reshape(inputs[0], (1,))
        for t in range(1, tf.b5(inputs)[0]):
            b21, b14 = fonk4(inputs[t], self.b3, b14)
            b13.append(b21)
        return tf.concat(b13, b15 = 0)
def fonk5():
    b16 = np.log(np.arange(1, 300, 3)) + np.random.normal(0, 0.4, 100)
    b17 = tf.convert_to_tensor(b16, dtype=tf.float32)
    a1 = 5
    a2 = 0.01
    b18 = tf.keras.optimizers.Adam(a2)
    b19 = []
    b20 = class1(b1=0.01, b2=0.5)
    print('--------------------- class1 Training Loss --------------------')
    for epoch in range(a1):
        with tf.GradientTape() as tape:
            b21 = b20(b17)
            b22 = tf.reduce_mean(tf.square(b17[:-1] - b21))
        b19.append(b22.numpy())
        b23 = tape.gradient(b22, b20.trainable_weights)
        b18.apply_gradients(zip(b23, b20.trainable_weights))
        print(f"MSE Loss at epoch {epoch}: {b22:.3f}, b3: {b20.b3.numpy()[0]:.3f}")
    print(f"Final MSE b22: {b22:.3f}")
    print(f"b24 = {b20.b3.numpy()[0]:.3f}")
    b25 = b21.numpy()
    plt.figure(b26 = (15, 8))
    plt.title('Simple Exponential Smoothing Layer Results with Constrained Learned Parameter')
    plt.plot(range(99), b25, b27 = 'Prediction')
    plt.plot(range(99), b17[:-1], b27 = 'Actual')
    plt.grid(True)
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.show()
if b28 = = "__main__":
    fonk5()