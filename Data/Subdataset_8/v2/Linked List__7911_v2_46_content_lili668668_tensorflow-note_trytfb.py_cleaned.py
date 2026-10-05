import tensorflow as tf
import numpy as np
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3
with tf.name_scope('inputs'):
    x_input = tf.placeholder(tf.float32, name='x_input')
    y_input = tf.placeholder(tf.float32, name='y_input')
with tf.name_scope('layer'):
    with tf.name_scope('weights'):
        weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0), name="W")
        tf.summary.histogram('weights', weights)
    with tf.name_scope('biases'):
        biases = tf.Variable(tf.zeros([1]), name="b")
        tf.summary.histogram('biases', biases)
    with tf.name_scope('Wx_plus_b'):
        y_output = weights * x_input + biases
with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.square(y_output - y_input))
    tf.summary.scalar('loss', loss)
with tf.name_scope('train'):
    optimizer = tf.train.GradientDescentOptimizer(0.5)
    train_op = optimizer.minimize(loss)
init_op = tf.global_variables_initializer()
saver = tf.train.Saver()
with tf.Session() as sess:
    merged_summary = tf.summary.merge_all()
    writer = tf.summary.FileWriter("logs/", sess.graph)
    sess.run(init_op)
    for step in range(2017):
        sess.run(train_op, feed_dict={x_input: x_data, y_input: y_data})
        if step % 20 == 0:
            result = sess.run(merged_summary, feed_dict={x_input: x_data, y_input: y_data})
            writer.add_summary(result, step)
            print(step, sess.run(weights), sess.run(biases))
    feed_dict = {x_input: [10, 20, 40]}
    prediction = sess.run(y_output, feed_dict)
    print("Prediction:", prediction)
    save_path = saver.save(sess, "output/save.ckpt")
    print("Model saved in path:", save_path)