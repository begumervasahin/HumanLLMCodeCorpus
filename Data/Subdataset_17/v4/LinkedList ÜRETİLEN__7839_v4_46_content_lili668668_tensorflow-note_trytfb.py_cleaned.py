import tensorflow as tf
import numpy as np
xd = np.random.rand(100).astype(np.float32)
yd = xd * 0.1 + 0.3
tf.compat.v1.disable_eager_execution()
with tf.compat.v1.name_scope('inputs'):
    xs = tf.compat.v1.placeholder(tf.float32, name='x_input')
    ys = tf.compat.v1.placeholder(tf.float32, name='y_input')
with tf.compat.v1.name_scope('layer'):
    with tf.compat.v1.name_scope('weights'):
        Weights = tf.Variable(tf.random.uniform([1], -1.0, 1.0), name="W")
        tf.compat.v1.summary.histogram('weights', Weights)
    with tf.compat.v1.name_scope('biases'):
        biases = tf.Variable(tf.zeros([1]), name="b")
        tf.compat.v1.summary.histogram('biases', biases)
    with tf.compat.v1.name_scope('Wx_add_b'):
        y = Weights * xs + biases
with tf.compat.v1.name_scope('loss'):
    loss = tf.reduce_mean(tf.square(y - ys))
    tf.compat.v1.summary.scalar('loss', loss)
with tf.compat.v1.name_scope('train'):
    optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.5)
    train = optimizer.minimize(loss)
init = tf.compat.v1.global_variables_initializer()
saver = tf.compat.v1.train.Saver()
with tf.compat.v1.Session() as sess:
    merged = tf.compat.v1.summary.merge_all()
    writer = tf.compat.v1.summary.FileWriter("logs/", sess.graph)
    sess.run(init)
    for step in range(2017):
        sess.run(train, feed_dict={xs: xd, ys: yd})
        if step % 20 == 0:
            result = sess.run(merged, feed_dict={xs: xd, ys: yd})
            writer.add_summary(result, step)
            print(step, sess.run(Weights), sess.run(biases))
    feed_dict = {xs: [10, 20, 40]}
    prediction = sess.run(y, feed_dict)
    print("Predictions:", prediction)
    save_path = saver.save(sess, "output/save.ckpt")
    print("Model saved in path: %s" % save_path)