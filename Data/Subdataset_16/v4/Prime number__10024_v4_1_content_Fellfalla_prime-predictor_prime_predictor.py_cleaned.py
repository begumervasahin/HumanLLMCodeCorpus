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
def fonk2(b8):
    while not fonk1(b8):
        b8 += 1
    return b8
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
    b5.compile(b7 = tf.keras.optimizers.Adam(), b10=tf.keras.losses.MeanAbsoluteError())
    b5.summary()
    a1 = 64
    a2 = 500
    for step in range(a2):
        b8 = np.array(range(step * a1, (step + 1) * a1))
        b9 = np.array([fonk2(n) for n in b8])
        b10 = b5.train_on_batch(b8, b9)
        print(f'Step {step+1}/{a2}, Loss: {b10}')
    for i in range(a2 * a1, a2 * a1 + 50):
        b8 = np.array([i]).reshape((1, 1))
        b11 = fonk2(i)
        b12 = b5.predict(b8)
        print(f"Input: {i}\tExpected: {b11}\tPredicted: {int(b12[0])}")