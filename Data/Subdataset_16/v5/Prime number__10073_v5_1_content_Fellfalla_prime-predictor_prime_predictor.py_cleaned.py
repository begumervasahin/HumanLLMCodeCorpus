import tensorflow as tf
import numpy as np
b1 = {
    2: True,
    3: True,
    4: False
}
def fonk1(number):
    if number not in b1:
        b1[number] = True
        for b2 in range(2, int(number ** 0.5) + 1):
            if number % b2 = = 0:
                b1[number] = False
                break
    return b1[number]
def fonk2(b7):
    while not fonk1(b7):
        b7 += 1
    return b7
def fonk3():
    b3 = tf.keras.Sequential([
        tf.keras.layers.Dense(24, b4 = 'relu', input_dim=1),
        tf.keras.layers.Dense(24, b4 = 'relu'),
        tf.keras.layers.Dense(24, b4 = 'relu'),
        tf.keras.layers.Dense(24, b4 = 'relu'),
        tf.keras.layers.Dense(24, b4 = 'relu'),
        tf.keras.layers.Dense(1)
    ])
    b3.compile(b5 = tf.keras.optimizers.Adam(), b9=tf.keras.losses.MeanAbsoluteError())
    return b3
def fonk4(b3, b6 = 64, a1=500):
    for step in range(a1):
        b7 = np.array(range(step * b6, (step + 1) * b6))
        b8 = np.array([fonk2(n) for n in b7])
        b9 = b3.train_on_batch(b7, b8)
        print(f'Step {step + 1}/{a1}, Loss: {b9}')
def fonk5(b3, start, b10 = 50):
    for i in range(start, start + b10):
        b7 = np.array([i]).reshape((1, 1))
        b11 = fonk2(i)
        b12 = b3.predict(b7)
        print(f"Input: {i}\tExpected: {b11}\tPredicted: {int(b12[0])}")
if b13 = = "__main__":
    b14 = fonk2(500)
    print(b14)
    b15 = fonk3()
    b15.summary()
    b6 = 64
    a1 = 500
    fonk4(b15, b6, a1)
    b16 = a1 * b6
    fonk5(b15, b16)