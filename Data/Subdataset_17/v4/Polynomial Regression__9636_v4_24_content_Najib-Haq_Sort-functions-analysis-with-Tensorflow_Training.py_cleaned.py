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
        if row[1] == 1:
            sorted_data.append(list(row[:1]) + list(row[4:]))
        elif row[2] == 1:
            random_data.append(list(row[:1]) + list(row[4:]))
        else:
            reverse_data.append(list(row[:1]) + list(row[4:]))
    return np.array(sorted_data), np.array(random_data), np.array(reverse_data)
def print_data(a):
    for row in a:
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
    print(f"For {model_name}")
    X = tf.placeholder(tf.float32)
    y = tf.placeholder(tf.float32, [output_size])
    y_model = polynomial_regression_model(X, output_size)
    cost = tf.reduce_mean(tf.square(y_model - y))
    train = tf.train.GradientDescentOptimizer(0.001).minimize(cost)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        for epoch in range(2000):
            for xt, yt in zip(X_train, y_train):
                c, _ = sess.run([cost, train], feed_dict={X: xt, y: yt})
            print(f"Epoch {epoch}  : {c}")
        saver.save(sess, f"{model_name}/{model_name}.ckpt")
        overall_cost = 0
        for xt, yt in zip(X_test, y_test):
            pred = sess.run(y_model, feed_dict={X: xt})
            overall_cost += tf.reduce_mean(tf.square(pred - yt)).eval()
        print(f"Testing cost {overall_cost / len(X_test)}")
def scale_data(data, max_data=4000):
    return data / max_data
if __name__ == "__main__":
    sorted_data, random_data, reverse_data = process_data("data.csv")
    X_train = [None] * 3
    X_test = [None] * 3
    y_train = [None] * 3
    y_test = [None] * 3
    X_train[0], X_test[0], y_train[0], y_test[0] = train_test_split(sorted_data[:, 0], sorted_data[:, 1:], test_size=0.2)
    X_train[1], X_test[1], y_train[1], y_test[1] = train_test_split(random_data[:, 0], random_data[:, 1:], test_size=0.2)
    X_train[2], X_test[2], y_train[2], y_test[2] = train_test_split(reverse_data[:, 0], reverse_data[:, 1:], test_size=0.2)
    model_names = ["Sorted_data", "Random_data", "Reverse_data"]
    for i in range(len(X_train)):
        X_train[i] = scale_data(X_train[i])
        X_test[i] = scale_data(X_test[i])
        train_and_save_model(X_train[i], y_train[i], X_test[i], y_test[i], model_names[i])