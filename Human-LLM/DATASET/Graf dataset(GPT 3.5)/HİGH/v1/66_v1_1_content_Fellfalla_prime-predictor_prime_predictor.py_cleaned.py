import tensorflow as tf
import numpy as np
b1 = {
    2: True,
    3: True,
    4: False
}
def fonk1(givenNumber):
    if givenNumber not in b1:
        b1[givenNumber] = True
        for b2 in range(2, int(givenNumber ** 0.5) + 1):
            if givenNumber % b2 = = 0:
                b1[givenNumber] = False
                break
    return b1[givenNumber]
def fonk2(b3):
    while not fonk1(b3):
        b3 = b3 + 1
    return b3
if b4 = = "__main__":
    b5 = fonk2(500)
    print(b5)
    b6 = tf.keras.Sequential([
        tf.keras.layers.Dense(24, b7 = 'relu', input_dim=1),
        tf.keras.layers.Dense(24, b7 = 'relu'),
        tf.keras.layers.Dense(24, b7 = 'relu'),
        tf.keras.layers.Dense(24, b7 = 'relu'),
        tf.keras.layers.Dense(24, b7 = 'relu'),
        tf.keras.layers.Dense(1)
    ])
    b8 = tf.keras.optimizers.Adam()
    b9 = tf.keras.losses.mae
    b6.compile(b10 = b8, b9=b9)
    b6.summary()
    a1 = 64
    a2 = 500
    for i in range(a2):
        b3 = np.array(range(i * a1))
        b11 = np.array([fonk2(n) for n in b3])
        b12 = b6.train_on_batch(b3, b11)
        print(b12)
    for i in range(a2 * a1, a2 * a1 + 50):
        b3 = np.array(i).reshape((1, 1))
        b13 = fonk2(i)
        b14 = b6.predict(b3)
        print("input: %i\texpected: %i\tpredicted %i" % (i, b13, b14[0]))