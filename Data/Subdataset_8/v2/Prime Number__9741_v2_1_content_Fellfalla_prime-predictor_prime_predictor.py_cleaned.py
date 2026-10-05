import tensorflow as tf
import numpy as np
prime_states = {
    2: True,
    3: True,
    4: False
}
def is_prime(given_number):
    if given_number not in prime_states:
        prime_states[given_number] = True
        for num in range(2, int(given_number ** 0.5) + 1):
            if given_number % num == 0:
                prime_states[given_number] = False
                break
    return prime_states[given_number]
def get_next_prime(x):
    while not is_prime(x):
        x += 1
    return x
if __name__ == "__main__":
    a = get_next_prime(500)
    print("Next prime after 500:", a)
    prime_model = tf.keras.Sequential([
        tf.keras.layers.Dense(24, activation='relu', input_dim=1),
        tf.keras.layers.Dense(24, activation='relu'),
        tf.keras.layers.Dense(24, activation='relu'),
        tf.keras.layers.Dense(24, activation='relu'),
        tf.keras.layers.Dense(24, activation='relu'),
        tf.keras.layers.Dense(1)
    ])
    opt = tf.keras.optimizers.Adam()
    loss = tf.keras.losses.mae
    prime_model.compile(optimizer=opt, loss=loss)
    prime_model.summary()
    batch_size = 64
    steps = 500
    for i in range(steps):
        x = np.array(range(i * batch_size))
        y = np.array([get_next_prime(n) for n in x])
        loss_value = prime_model.train_on_batch(x, y)
        print("Step:", i, "Loss:", loss_value)
    for i in range(steps * batch_size, steps * batch_size + 50):
        x = np.array(i).reshape((1, 1))
        expected = get_next_prime(i)
        pred = prime_model.predict(x)
        print("Input:", i, "\tExpected:", expected, "\tPredicted:", pred[0])