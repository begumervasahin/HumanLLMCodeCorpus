import numpy as np
import csv
from sklearn.model_selection import train_test_split
import tensorflow as tf
def get_data(filename):
    data = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i % 2 == 0:
                data.append(row)
    return data[1:]
def process_data(filename):
    data = get_data(filename)
    data = np.array(data, dtype=np.float32)
    sorted_data, random_data, reverse_data = [], [], []
    for row in data:
        features = list(row[0:1]) + list(row[4:])
        if row[1] == 1:
            sorted_data.append(features)
        elif row[2] == 1:
            random_data.append(features)
        else:
            reverse_data.append(features)
    return np.array(sorted_data), np.array(random_data), np.array(reverse_data)
def print_data(data):
    for row in data:
        print(row)
def polynomial_regression_model(X, output_size):
    w_1 = tf.Variable(tf.zeros([output_size]))
    w_2 = tf.Variable(tf.zeros([output_size]))
    b = tf.Variable(tf.zeros([output_size]))
    term = tf.pow(X, 2)
    term = tf.add(tf.multiply(w_1, term), tf.multiply(w_2, X))
    y_model = tf.add(term, b)
    return y_model
def train_and_save_model(X_train, y_train, X_test, y_test, model_name, output_size=6):
    print(f"Training model: {model_name}")
    X = tf.placeholder(tf.float32)
    y = tf.placeholder(tf.float32, [output_size])
    y_model = polynomial_regression_model(X, output_size)
    cost = tf.reduce_mean(tf.square(y_model - y))
    train_op = tf.train.GradientDescentOptimizer(0.001).minimize(cost)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        for epoch in range(2000):
            for xt, yt in zip(X_train, y_train):
                _, training_cost = sess.run([train_op, cost], feed_dict={X: xt, y: yt})
            if epoch % 100 == 0:
                print(f"Epoch {epoch} : {training_cost}")
        saver.save(sess, f"{model_name}/{model_name}.ckpt")
        overall_cost = 0
        for xt, yt in zip(X_test, y_test):
            pred = sess.run(y_model, feed_dict={X: xt})
            overall_cost += tf.reduce_mean(tf.square(pred - yt)).eval()
        print(f"Testing cost for {model_name}: {overall_cost / len(X_test)}")
def scale_data(data, max_data=4000):
    return data / max_data
if __name__ == "__main__":
    sorted_data, random_data, reverse_data = process_data("data.csv")
    X_train, X_test, y_train, y_test = [None] * 3, [None] * 3, [None] * 3, [None] * 3
    datasets = [(sorted_data, "Sorted_data"), (random_data, "Random_data"), (reverse_data, "Reverse_data")]
    for i, (data, model_name) in enumerate(datasets):
        X_train[i], X_test[i], y_train[i], y_test[i] = train_test_split(data[:, 0], data[:, 1:], test_size=0.2)
        X_train[i] = scale_data(X_train[i])
        X_test[i] = scale_data(X_test[i])
        train_and_save_model(X_train[i], y_train[i], X_test[i], y_test[i], model_name)