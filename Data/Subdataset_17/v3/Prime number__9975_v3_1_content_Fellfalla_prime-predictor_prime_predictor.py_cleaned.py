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
def build_and_compile_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(24, activation='relu', input_dim=1),
        tf.keras.layers.Dense(24, activation='relu'),
        tf.keras.layers.Dense(24, activation='relu'),
        tf.keras.layers.Dense(24, activation='relu'),
        tf.keras.layers.Dense(24, activation='relu'),
        tf.keras.layers.Dense(1)
    ])
    model.compile(optimizer=tf.keras.optimizers.Adam(), loss=tf.keras.losses.mae)
    model.summary()
    return model
def train_model(model, batch_size, steps):
    for step in range(steps):
        x = np.arange(step * batch_size, (step + 1) * batch_size).reshape(-1, 1)
        y = np.array([get_next_prime(n) for n in x.flatten()])
        loss = model.train_on_batch(x, y)
        print(f"Step {step + 1}/{steps}, Loss: {loss}")
def test_model(model, start, num_tests):
    for i in range(start, start + num_tests):
        x = np.array([[i]])
        expected = get_next_prime(i)
        predicted = model.predict(x)
        print(f"input: {i}\texpected: {expected}\tpredicted: {int(predicted[0][0])}")
if __name__ == "__main__":
    a = get_next_prime(500)
    print(a)
    prime_model = build_and_compile_model()
    batch_size = 64
    steps = 500
    train_model(prime_model, batch_size, steps)
    test_model(prime_model, steps * batch_size, 50)