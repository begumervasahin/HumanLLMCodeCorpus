import tensorflow as tf
import numpy as np
prime_states = {
    2: True,
    3: True,
    4: False
}
def is_prime(number):
    if number not in prime_states:
        prime_states[number] = True
        for num in range(2, int(number ** 0.5) + 1):
            if number % num == 0:
                prime_states[number] = False
                break
    return prime_states[number]
def get_next_prime(x):
    while not is_prime(x):
        x += 1
    return x
def build_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(24, activation='relu', input_dim=1),
        tf.keras.layers.Dense(24, activation='relu'),
        tf.keras.layers.Dense(24, activation='relu'),
        tf.keras.layers.Dense(24, activation='relu'),
        tf.keras.layers.Dense(24, activation='relu'),
        tf.keras.layers.Dense(1)
    ])
    model.compile(optimizer=tf.keras.optimizers.Adam(), loss=tf.keras.losses.MeanAbsoluteError())
    return model
def train_model(model, batch_size=64, steps=500):
    for step in range(steps):
        x = np.array(range(step * batch_size, (step + 1) * batch_size))
        y = np.array([get_next_prime(n) for n in x])
        loss = model.train_on_batch(x, y)
        print(f'Step {step + 1}/{steps}, Loss: {loss}')
def test_model(model, start, count=50):
    for i in range(start, start + count):
        x = np.array([i]).reshape((1, 1))
        expected = get_next_prime(i)
        pred = model.predict(x)
        print(f"Input: {i}\tExpected: {expected}\tPredicted: {int(pred[0])}")
if __name__ == "__main__":
    next_prime = get_next_prime(500)
    print(next_prime)
    prime_model = build_model()
    prime_model.summary()
    batch_size = 64
    steps = 500
    train_model(prime_model, batch_size, steps)
    test_start = steps * batch_size
    test_model(prime_model, test_start)