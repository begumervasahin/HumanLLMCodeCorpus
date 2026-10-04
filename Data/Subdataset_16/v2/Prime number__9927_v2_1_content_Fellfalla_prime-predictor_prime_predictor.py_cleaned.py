import tensorflow as tf
import numpy as np
b1 = {
    2: True,
    3: True,
    4: False
}
def fonk1(given_number):
    if given_number not in b1:
        b1[given_number] = True
        for b2 in range(2, int(given_number ** 0.5) + 1):
            if given_number % b2 = = 0:
                b1[given_number] = False
                break
    return b1[given_number]
def fonk2(b10):
    while not fonk1(b10):
        b10 += 1
    return b10
if b3 = = "__main__":
    b4 = fonk2(500)
    print(b4)
    b5 = tf.keras.Sequential([
        tf.keras.layers.Dense(24, b6 = 'relu', input_dim=1),
        tf.keras.layers.Dense(24, b6 = 'relu'),
        tf.keras.layers.Dense(24, b6 = 'relu'),
        tf.keras.layers.Dense(24, b6 = 'relu'),
        tf.keras.layers.Dense(24, b6 = 'relu'),
        tf.keras.layers.Dense(1)
    ])
    b7 = tf.keras.optimizers.Adam()
    b8 = tf.keras.losses.mae
    b5.compile(b9 = b7, b8=b8)
    b5.summary()
    a1 = 64
    a2 = 500
    for i in range(a2):
        b10 = np.array(range(i * a1, (i + 1) * a1)).reshape(-1, 1)
        b11 = np.array([fonk2(n) for n in b10.flatten()])
        b12 = b5.train_on_batch(b10, b11)
        print(f"Step {i+1}/{a2}, Loss: {b12}")
    for i in range(a2 * a1, a2 * a1 + 50):
        b10 = np.array([[i]])
        b13 = fonk2(i)
        b14 = b5.predict(b10)
        print(f"input: {i}\texpected: {b13}\tpredicted: {int(b14[0][0])}")