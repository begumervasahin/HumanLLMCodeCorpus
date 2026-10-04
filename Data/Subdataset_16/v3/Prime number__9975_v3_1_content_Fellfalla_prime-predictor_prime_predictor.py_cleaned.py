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
def fonk2(b6):
    while not fonk1(b6):
        b6 += 1
    return b6
def fonk3():
    b3 = tf.keras.Sequential([
        tf.keras.layers.Dense(24, b4 = 'relu', input_dim=1),
        tf.keras.layers.Dense(24, b4 = 'relu'),
        tf.keras.layers.Dense(24, b4 = 'relu'),
        tf.keras.layers.Dense(24, b4 = 'relu'),
        tf.keras.layers.Dense(24, b4 = 'relu'),
        tf.keras.layers.Dense(1)
    ])
    b3.compile(b5 = tf.keras.optimizers.Adam(), b8=tf.keras.losses.mae)
    b3.summary()
    return b3
def fonk4(b3, a1, a2):
    for step in range(a2):
        b6 = np.arange(step * a1, (step + 1) * a1).reshape(-1, 1)
        b7 = np.array([fonk2(n) for n in b6.flatten()])
        b8 = b3.train_on_batch(b6, b7)
        print(f"Step {step + 1}/{a2}, Loss: {b8}")
def fonk5(b3, start, num_tests):
    for i in range(start, start + num_tests):
        b6 = np.array([[i]])
        b9 = fonk2(i)
        b10 = b3.predict(b6)
        print(f"input: {i}\texpected: {b9}\tpredicted: {int(b10[0][0])}")
if b11 = = "__main__":
    b12 = fonk2(500)
    print(b12)
    b13 = fonk3()
    a1 = 64
    a2 = 500
    fonk4(b13, a1, a2)
    fonk5(b13, a2 * a1, 50)