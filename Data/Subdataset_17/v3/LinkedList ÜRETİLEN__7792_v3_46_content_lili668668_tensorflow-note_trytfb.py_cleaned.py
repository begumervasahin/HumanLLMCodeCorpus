import tensorflow as tf
import numpy as np
xd = np.random.rand(100).astype(np.float32)
yd = xd * 0.1 + 0.3
def create_model():
    with tf.name_scope('inputs'):
        xs = tf.placeholder(tf.float32, name='x_input')
        ys = tf.placeholder(tf.float32, name='y_input')
    with tf.name_scope('layer'):
        with tf.name_scope('weights'):
            weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0), name="W")
            tf.summary.histogram('weights', weights)
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1]), name="b")
            tf.summary.histogram('biases', biases)
        with tf.name_scope('Wx_plus_b'):
            y_pred = weights * xs + biases
    with tf.name_scope('loss'):
        loss = tf.reduce_mean(tf.square(y_pred - ys))
        tf.summary.scalar('loss', loss)
    with tf.name_scope('train'):
        optimizer = tf.train.GradientDescentOptimizer(0.5)
        train_step = optimizer.minimize(loss)
    return xs, ys, y_pred, weights, biases, loss, train_step
def train_model(xs, ys, train_step, merged, writer):
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for step in range(2017):
            sess.run(train_step, feed_dict={xs: xd, ys: yd})
            if step % 20 == 0:
                summary = sess.run(merged, feed_dict={xs: xd, ys: yd})
                writer.add_summary(summary, step)
                current_weights, current_biases = sess.run([weights, biases])
                print(f"Step {step}: Weights = {current_weights}, Biases = {current_biases}")
        return sess
def make_predictions(sess, xs, y_pred, test_xs):
    prediction = sess.run(y_pred, feed_dict={xs: test_xs})
    print("Predictions:", prediction)
def save_model(sess, saver, path):
    save_path = saver.save(sess, path)
    print(f"Model saved in path: {save_path}")
if __name__ == "__main__":
    tf.reset_default_graph()
    xs, ys, y_pred, weights, biases, loss, train_step = create_model()
    saver = tf.train.Saver()
    merged = tf.summary.merge_all()
    writer = tf.summary.FileWriter("logs/", tf.get_default_graph())
    with train_model(xs, ys, train_step, merged, writer) as sess:
        test_xs = [10, 20, 40]
        make_predictions(sess, xs, y_pred, test_xs)
        save_model(sess, saver, "output/save.ckpt")