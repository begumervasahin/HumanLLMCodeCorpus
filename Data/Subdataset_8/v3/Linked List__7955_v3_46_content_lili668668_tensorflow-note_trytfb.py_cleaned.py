import tensorflow as tf
import numpy as np
def generate_data():
    x_data = np.random.rand(100).astype(np.float32)
    y_data = x_data * 0.1 + 0.3
    return x_data, y_data
def define_placeholders():
    with tf.name_scope('inputs'):
        x_input = tf.placeholder(tf.float32, name='x_input')
        y_input = tf.placeholder(tf.float32, name='y_input')
    return x_input, y_input
def define_computation_graph(x_input, y_input):
    with tf.name_scope('layer'):
        with tf.name_scope('weights'):
            weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0), name="W")
            tf.summary.histogram('weights', weights)
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1]), name="b")
            tf.summary.histogram('biases', biases)
        with tf.name_scope('Wx_plus_b'):
            y_output = weights * x_input + biases
    return y_output
def define_loss_function(y_output, y_input):
    with tf.name_scope('loss'):
        loss = tf.reduce_mean(tf.square(y_output - y_input))
        tf.summary.scalar('loss', loss)
    return loss
def define_optimizer(loss):
    with tf.name_scope('train'):
        optimizer = tf.train.GradientDescentOptimizer(0.5)
        train_op = optimizer.minimize(loss)
    return train_op
def train_model(train_op, x_data, y_data, x_input, y_input, merged_summary, writer, sess):
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    for step in range(2017):
        sess.run(train_op, feed_dict={x_input: x_data, y_input: y_data})
        if step % 20 == 0:
            result = sess.run(merged_summary, feed_dict={x_input: x_data, y_input: y_data})
            writer.add_summary(result, step)
            print(step, sess.run(weights), sess.run(biases))
def make_predictions(sess, x_input, y_output):
    feed_dict = {x_input: [10, 20, 40]}
    prediction = sess.run(y_output, feed_dict)
    print("Prediction:", prediction)
def save_model(sess, saver):
    save_path = saver.save(sess, "output/save.ckpt")
    print("Model saved in path:", save_path)
def main():
    print("=== TensorFlow Linear Regression ===")
    x_data, y_data = generate_data()
    x_input, y_input = define_placeholders()
    y_output = define_computation_graph(x_input, y_input)
    loss = define_loss_function(y_output, y_input)
    train_op = define_optimizer(loss)
    with tf.Session() as sess:
        merged_summary = tf.summary.merge_all()
        writer = tf.summary.FileWriter("logs/", sess.graph)
        train_model(train_op, x_data, y_data, x_input, y_input, merged_summary, writer, sess)
        make_predictions(sess, x_input, y_output)
        saver = tf.train.Saver()
        save_model(sess, saver)
if __name__ == '__main__':
    main()